import {
  ENGINE_VERSION,
  simulate,
  makeEvidence,
  verifyEvidence,
} from "./engine.mjs";
import { PROVENANCE, RULES } from "./provenance.mjs";

const $ = (id) => document.getElementById(id);
const canvas = $("universe");
const ctx = canvas.getContext("2d");
const STORAGE = "orbit-mission-flights-v1";
const missions = {
  home: {
    seed: "9",
    multiplier: "3",
    offset: "1",
    label: "MISSION 01 · THE WAY HOME",
  },
  voyage: {
    seed: "27",
    multiplier: "3",
    offset: "1",
    label: "MISSION 02 · THE LONG WAY ROUND",
  },
  loop: {
    seed: "5",
    multiplier: "3",
    offset: "-1",
    label: "MISSION 03 · LOST IN A LOOP",
  },
};
let run,
  cursor = 0,
  playing = false,
  elapsed = 0,
  anim = null,
  clock = 0;
let guesses = new Map(),
  lastFeedback = "",
  currentLabel = "",
  selectedMission = "home";
let view = "mission",
  flights = [],
  selectedFlights = new Set();
let build = {
  revision: null,
  dirty: null,
  engineSha256: null,
  appSha256: null,
};
let width = 700,
  height = 390,
  displayedShip = null;
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
const short = (s, n = 15) =>
  String(s).length > n
    ? String(s).slice(0, n - 4) + "…" + String(s).slice(-3)
    : String(s);
const log2 = (s) => {
  const t = String(s);
  const head = t.slice(0, 15);
  return Math.log2(Number(head)) + (t.length - head.length) * Math.log2(10);
};
const ruleText = (config) =>
  `${config.multiplier}n ${BigInt(config.offset) < 0n ? "−" : "+"} ${String(config.offset).replace("-", "")}`;
const modeText = (config) =>
  config.mode === "odd" ? "Odd moves" : "Every move";
const outcomeText = {
  home: "Home reached",
  cycle: "Repeating loop",
  limit: "Limit reached · unresolved",
  invalid: "Left positive integers",
};

function el(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

async function loadBuild() {
  try {
    const response = await fetch("./build.json");
    if (response.ok) {
      const data = await response.json();
      if (
        typeof data.revision === "string" &&
        /^[a-f0-9]{40}$/.test(data.revision)
      )
        build = data;
    }
  } catch {
    /* Static hosts can use the checked-in version metadata. */
  }
  renderHistory();
}

function provenanceLabel() {
  return `Orbit Mission ${PROVENANCE.appVersion}; engine ${ENGINE_VERSION}; ${build.dirty === false ? "clean" : "working copy"}; engine-sha256:${build.engineSha256 || "unavailable"}`;
}

function loadFlights() {
  try {
    const raw = localStorage.getItem(STORAGE);
    if (!raw) return;
    if (raw.length > 8 * 1024 * 1024)
      throw new Error("Saved flight data is too large.");
    const entries = JSON.parse(raw);
    if (!Array.isArray(entries) || entries.length > 24)
      throw new Error("Invalid saved flight collection.");
    for (const evidence of entries) {
      const checked = verifyEvidence(evidence);
      if (checked.valid) flights.push(evidence);
    }
    if (flights.length !== entries.length)
      $("import-notice").textContent =
        "Some stored flights failed arithmetic verification and were not loaded.";
  } catch {
    $("import-notice").textContent =
      "Browser storage could not be read. You can still play and export a replay.";
  }
  $("log-count").textContent = flights.length;
}

function remember(evidence) {
  if (
    flights.some(
      (f) =>
        JSON.stringify(f.run.config) === JSON.stringify(evidence.run.config) &&
        f.sourceRevision === evidence.sourceRevision &&
        f.label === evidence.label,
    )
  ) {
    return "This flight is already saved. Open Flight log to replay or compare it.";
  }
  if (flights.length >= 24)
    throw new Error(
      "Flight log is full (24 flights). Export a flight, then remove one to make room.",
    );
  const next = [evidence, ...flights];
  localStorage.setItem(STORAGE, JSON.stringify(next));
  flights = next;
  selectedFlights.clear();
  renderLog();
  return "Flight saved. Open Flight log to replay or compare it.";
}

function saveFlight() {
  try {
    const message = remember(
      makeEvidence(run, {
        sourceRevision: build.revision,
        label: provenanceLabel(),
      }),
    );
    $("save-notice").textContent = message;
    $("save-result").textContent = "Saved in flight log ✓";
  } catch (error) {
    $("save-notice").textContent =
      `${error.message} Use Export to keep a file.`;
  }
}

function launch(config, label, mission = null) {
  run = simulate(config);
  cursor = 0;
  playing = false;
  elapsed = 0;
  anim = null;
  guesses = new Map();
  lastFeedback = "";
  selectedMission = mission;
  currentLabel = label;
  $("flight-label").textContent = label;
  $("seed").value = run.config.seed;
  $("map-mode").value = run.config.mode;
  const preset = RULES.find(
    (r) =>
      String(r.multiplier) === run.config.multiplier &&
      String(r.offset) === run.config.offset,
  );
  $("rule-select").value = preset?.id || "custom";
  $("multiplier").value = run.config.multiplier;
  $("offset").value = run.config.offset;
  $("custom-rule").hidden = $("rule-select").value !== "custom";
  $("form-error").hidden = true;
  $("save-notice").textContent = "";
  $("save-result").textContent = "Save this flight";
  document.querySelectorAll("[data-mission]").forEach((button) => {
    button.classList.toggle("selected", button.dataset.mission === mission);
    button.setAttribute(
      "aria-pressed",
      String(button.dataset.mission === mission),
    );
  });
  $("timeline").max = Math.max(0, run.steps);
  $("step-total").textContent = run.steps;
  renderInfo();
  draw();
}

function setCursor(next, animate = true) {
  const previous = cursor;
  cursor = Math.max(0, Math.min(run.steps, next));
  anim =
    animate && !reducedMotion && previous !== cursor
      ? { from: previous, to: cursor, time: 0 }
      : null;
  if (cursor === run.steps) playing = false;
  renderInfo();
  draw();
}

function togglePlay() {
  if (run.steps === 0) return;
  if (cursor === run.steps) {
    setCursor(0, false);
    elapsed = 0;
  }
  playing = !playing;
  elapsed = 0;
  if (playing) lastFeedback = "";
  renderInfo();
}

function prediction(direction) {
  if (cursor >= run.steps) return;
  playing = false;
  elapsed = 0;
  if (guesses.has(cursor)) {
    lastFeedback =
      "You already predicted this move. Step forward to try a new one.";
    renderInfo();
    return;
  }
  const next = run.frames[cursor + 1];
  const right = direction === next.kind;
  guesses.set(cursor, right);
  lastFeedback = `${right ? "Correct!" : "Keep exploring."} ${next.value === run.frames[cursor].value ? "The number stays the same." : next.kind === "expand" ? "The number increases, so the ship moves outward." : "The number decreases, so the ship moves inward."}`;
  setCursor(cursor + 1);
}

function describeTransition(previous, next) {
  const odd = BigInt(previous.value) % 2n === 1n;
  const direction =
    next.kind === "expand"
      ? "gets bigger, so your ship heads outward"
      : next.kind === "contract"
        ? "gets smaller, so your ship heads inward"
        : "stays the same, so your ship stays on its ring";
  if (run.config.mode === "odd")
    return `Multiply by ${run.config.multiplier}, ${BigInt(run.config.offset) < 0n ? "subtract" : "add"} ${run.config.offset.replace("-", "")}, then divide by 2 ${next.divisions} ${next.divisions === 1 ? "time" : "times"}. The number ${direction}.`;
  return `${short(previous.value)} is ${odd ? "odd" : "even"}. ${odd ? `Multiply it by ${run.config.multiplier} and ${BigInt(run.config.offset) < 0n ? "subtract" : "add"} ${run.config.offset.replace("-", "")}` : "Divide it by 2"}. The number ${direction}.`;
}

function renderInfo() {
  const frame = run.frames[cursor];
  const end = cursor === run.steps;
  $("current-value").textContent = short(frame.value, 30);
  $("current-value").title = frame.value;
  $("exact-value-details").hidden = frame.value.length <= 30;
  $("exact-value").textContent = frame.value;
  $("current-value").style.fontSize =
    frame.value.length > 25 ? "15px" : frame.value.length > 12 ? "23px" : "";
  $("current-detail").textContent =
    end && cursor === 0
      ? outcomeText[run.outcome.type]
      : cursor === 0
        ? "Ready for the first move"
        : `${BigInt(frame.value) % 2n === 0n ? "Even" : "Odd"} number · ${frame.elementarySteps} elementary ${frame.elementarySteps === 1 ? "step" : "steps"}`;
  const classic = run.config.multiplier === "3" && run.config.offset === "1";
  $("rule-name").textContent = classic
    ? "THE CLASSIC RULE"
    : "EXPERIMENTAL RULE";
  $("odd-rule").textContent =
    `Multiply by ${run.config.multiplier}, ${BigInt(run.config.offset) < 0n ? "subtract" : "add"} ${run.config.offset.replace("-", "")}`;
  $("mode-badge").textContent = modeText(run.config);
  $("equation-label").textContent =
    cursor === 0 ? "WHAT HAPPENS NEXT?" : "THE MOVE YOU JUST SAW";
  if (cursor > 0) {
    $("equation").textContent = frame.operation;
    $("explanation").textContent = describeTransition(
      run.frames[cursor - 1],
      frame,
    );
  } else if (run.steps > 0) {
    $("equation").textContent = run.frames[1].operation;
    $("explanation").textContent = describeTransition(frame, run.frames[1]);
  } else {
    $("equation").textContent = frame.operation;
    $("explanation").textContent = run.outcome.message;
  }
  $("moves").textContent = cursor;
  const peak = run.frames
    .slice(0, cursor + 1)
    .reduce((p, f) => (BigInt(f.value) > p ? BigInt(f.value) : p), 0n)
    .toString();
  $("peak").textContent = short(peak, 17);
  $("peak").title = peak;
  $("step-counter").textContent = `Move ${cursor}`;
  $("timeline").value = cursor;
  $("play").replaceChildren(
    document.createTextNode(playing ? "Ⅱ " : "▶ "),
    el(
      "span",
      "",
      playing
        ? "Pause"
        : end && run.steps > 0
          ? "Replay mission"
          : cursor > 0
            ? "Continue"
            : "Play mission",
    ),
  );
  $("play").disabled = run.steps === 0;
  $("back").disabled = cursor === 0;
  $("next").disabled = end;
  $("flight-status").textContent = end
    ? outcomeText[run.outcome.type].toUpperCase()
    : playing
      ? "IN FLIGHT"
      : cursor === 0
        ? "READY TO LAUNCH"
        : "PAUSED";
  $("launch-hint").hidden = cursor > 0 || end || playing;
  $("prediction").hidden = end;
  $("guess-feedback").textContent =
    lastFeedback || "Make a prediction, then watch one move.";
  $("score").textContent =
    `${[...guesses.values()].filter(Boolean).length} correct / ${guesses.size} predictions`;
  ["guess-in", "guess-out", "guess-same"].forEach((id) => {
    $(id).disabled = end || guesses.has(cursor);
  });
  $("result").hidden = !end;
  $("result").className = `result result-${run.outcome.type}`;
  $("result-title").textContent = outcomeText[run.outcome.type].toUpperCase();
  $("result-text").textContent =
    run.outcome.type === "home"
      ? `Home in ${run.steps} displayed moves (${run.elementarySteps} elementary steps). We stop at 1. This journey reached home; it does not establish what every starting number does.`
      : run.outcome.type === "cycle"
        ? `You returned to ${frame.value}, first seen at move ${run.outcome.cycleStart}. The same rule now repeats those ${run.outcome.cycleLength} moves forever. This loop does not contain 1.`
        : run.outcome.message;
}

function shipPoint(value) {
  if (value === "1") return { x: width * 0.5, y: height * 0.5 + 9 };
  const scale = Math.max(6, Math.ceil(log2(run.peak)));
  const maxRadius = Math.max(60, Math.min(width * 0.43, height * 0.4));
  const radius = 23 + ((maxRadius - 23) * log2(value)) / scale;
  let hash = 0;
  for (const char of value.slice(-16))
    hash = (hash * 31 + char.charCodeAt(0)) % 10007;
  const angle = hash * 0.6180339887 * Math.PI * 2;
  return {
    x: width * 0.5 + Math.cos(angle) * radius,
    y: height * 0.5 + 9 + Math.sin(angle) * radius,
  };
}

// A move must stay inward/outward throughout its animation, not cut across home.
function arcPoint(a, b, t) {
  const cx = width * 0.5,
    cy = height * 0.5 + 9;
  const r1 = Math.hypot(a.x - cx, a.y - cy),
    r2 = Math.hypot(b.x - cx, b.y - cy);
  const start =
    r1 === 0 ? Math.atan2(b.y - cy, b.x - cx) : Math.atan2(a.y - cy, a.x - cx);
  const finish = r2 === 0 ? start : Math.atan2(b.y - cy, b.x - cx);
  const delta = Math.atan2(Math.sin(finish - start), Math.cos(finish - start));
  const angle = start + delta * t,
    radius = r1 + (r2 - r1) * t;
  return { x: cx + Math.cos(angle) * radius, y: cy + Math.sin(angle) * radius };
}

function draw() {
  if (!run) return;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.fillStyle = "#111f2b";
  ctx.fillRect(0, 0, width, height);
  const cx = width * 0.5,
    cy = height * 0.5 + 9;
  const glow = ctx.createRadialGradient(cx, cy, 4, cx, cy, height * 0.58);
  glow.addColorStop(0, "#22464a");
  glow.addColorStop(0.45, "#172e39");
  glow.addColorStop(1, "#111f2b");
  ctx.fillStyle = glow;
  ctx.fillRect(0, 0, width, height);
  for (let i = 0; i < 110; i++) {
    const sx = (((i * 7919 + 203) % 1009) / 1009) * width;
    const sy = (((i * 3571 + 173) % 997) / 997) * height;
    ctx.fillStyle = i % 7 === 0 ? "#668885" : "#3b555d";
    ctx.beginPath();
    ctx.arc(sx, sy, i % 7 === 0 ? 0.9 : 0.55, 0, Math.PI * 2);
    ctx.fill();
  }
  const scale = Math.max(6, Math.ceil(log2(run.peak)));
  const maxRadius = Math.max(60, Math.min(width * 0.43, height * 0.4));
  const ringCount = 4;
  for (let i = 1; i <= ringCount; i++) {
    const exponent = Math.round((scale * i) / ringCount);
    const radius = 23 + ((maxRadius - 23) * exponent) / scale;
    ctx.strokeStyle = "#47646a66";
    ctx.lineWidth = 0.8;
    ctx.beginPath();
    ctx.ellipse(cx, cy, radius, radius, 0, 0, Math.PI * 2);
    ctx.stroke();
    ctx.font = "9px ui-monospace, monospace";
    ctx.fillStyle = "#8ea9a6";
    ctx.textAlign = "left";
    const ringLabel = exponent <= 20 ? String(2 ** exponent) : `2^${exponent}`;
    ctx.fillText(ringLabel, cx + radius * 0.707 + 5, cy + radius * 0.707 + 3);
  }
  // Draw only the path already visited. A number always maps to the same position.
  const begin = Math.max(1, cursor - 80);
  for (let i = begin; i <= cursor; i++) {
    const a = shipPoint(run.frames[i - 1].value),
      b = shipPoint(run.frames[i].value);
    ctx.globalAlpha = 0.1 + (0.65 * (i - begin + 1)) / (cursor - begin + 1);
    ctx.strokeStyle = run.frames[i].kind === "expand" ? "#edc275" : "#80daba";
    ctx.lineWidth = i === cursor ? 1.7 : 1;
    ctx.beginPath();
    ctx.moveTo(a.x, a.y);
    for (let part = 1; part <= 24; part++) {
      const p = arcPoint(a, b, part / 24);
      ctx.lineTo(p.x, p.y);
    }
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(a.x, a.y, 2, 0, Math.PI * 2);
    ctx.fillStyle = ctx.strokeStyle;
    ctx.fill();
  }
  ctx.globalAlpha = 1;
  const homeGlow = ctx.createRadialGradient(cx, cy, 2, cx, cy, 35);
  homeGlow.addColorStop(0, "#acdfb344");
  homeGlow.addColorStop(1, "#acdfb300");
  ctx.fillStyle = homeGlow;
  ctx.beginPath();
  ctx.arc(cx, cy, 35, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#bed6a7";
  ctx.beginPath();
  ctx.arc(cx, cy, 14, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#598b7a";
  ctx.beginPath();
  ctx.ellipse(cx - 3, cy - 3, 6, 10, 0.7, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "#8eb59a";
  ctx.beginPath();
  ctx.arc(cx + 6, cy + 5, 5, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = "#d3ead1aa";
  ctx.lineWidth = 0.7;
  ctx.beginPath();
  ctx.ellipse(cx, cy, 23, 7, -0.3, 0, Math.PI * 2);
  ctx.stroke();
  ctx.font = "9px ui-monospace, monospace";
  ctx.textAlign = "center";
  ctx.fillStyle = "#b9d5c7";
  ctx.fillText("HOME · 1", cx, cy + 34);
  let p = shipPoint(run.frames[cursor].value);
  let prior =
    cursor > 0 ? arcPoint(shipPoint(run.frames[cursor - 1].value), p, 0.97) : p;
  if (anim) {
    const a = shipPoint(run.frames[anim.from].value),
      b = shipPoint(run.frames[anim.to].value);
    const raw = Math.min(
      1,
      anim.time / Math.min(480, Number($("speed").value) * 0.65),
    );
    const t = raw * raw * (3 - 2 * raw);
    p = arcPoint(a, b, t);
    prior = arcPoint(a, b, Math.max(0, t - 0.015));
  }
  displayedShip = p;
  const final = cursor === run.steps;
  if (final && run.outcome.type === "cycle") {
    ctx.strokeStyle = "#f3c67a";
    ctx.lineWidth = 1.5;
    ctx.setLineDash([3, 4]);
    ctx.beginPath();
    ctx.arc(p.x, p.y, 26, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);
  }
  ctx.save();
  ctx.translate(p.x, p.y);
  const angle = Math.atan2(p.y - prior.y, p.x - prior.x) + Math.PI / 2;
  ctx.rotate(cursor > 0 ? angle : -0.45);
  if (playing || anim) {
    ctx.fillStyle = "#77dabb";
    ctx.beginPath();
    ctx.moveTo(-4, 6);
    ctx.lineTo(0, 16 + Math.sin(clock / 70) * 3);
    ctx.lineTo(4, 6);
    ctx.fill();
  }
  ctx.shadowColor = "#baffdc";
  ctx.shadowBlur = 12;
  ctx.fillStyle = "#f0f3df";
  ctx.beginPath();
  ctx.moveTo(0, -12);
  ctx.lineTo(8, 9);
  ctx.lineTo(0, 5);
  ctx.lineTo(-8, 9);
  ctx.closePath();
  ctx.fill();
  ctx.shadowBlur = 0;
  ctx.fillStyle = "#64bdb6";
  ctx.beginPath();
  ctx.arc(0, -2, 2.5, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
  const label = short(run.frames[cursor].value, width < 400 ? 12 : 18);
  ctx.font = "600 14px ui-monospace, monospace";
  const boxWidth = ctx.measureText(label).width + 20;
  let labelX = Math.max(
    boxWidth / 2 + 6,
    Math.min(width - boxWidth / 2 - 6, p.x),
  );
  const labelY = Math.max(64, p.y - 25);
  if (
    run.frames[cursor].value !== "1" &&
    Math.abs(labelX - cx) < 60 &&
    labelY > cy + 15 &&
    labelY < cy + 60
  ) {
    labelX = Math.max(
      boxWidth / 2 + 6,
      Math.min(width - boxWidth / 2 - 6, cx + (p.x >= cx ? 70 : -70)),
    );
  }
  ctx.fillStyle = "#172e35";
  ctx.strokeStyle = "#65958b";
  ctx.lineWidth = 0.7;
  ctx.beginPath();
  ctx.roundRect(labelX - boxWidth / 2, labelY - 18, boxWidth, 27, 5);
  ctx.fill();
  ctx.stroke();
  ctx.textAlign = "center";
  ctx.fillStyle = "#daf6df";
  ctx.fillText(label, labelX, labelY);
  const operation =
    cursor === 0
      ? "PRESS PLAY TO APPLY THE RULE"
      : run.frames[cursor].operation;
  ctx.font = `${operation.length > 45 ? "10" : "12"}px ui-monospace, monospace`;
  ctx.fillStyle = "#d4e4da";
  ctx.fillText(
    short(operation, Math.max(25, Math.floor(width / 7))),
    cx,
    height - (final ? 42 : 22),
  );
  if (final) {
    ctx.font = "11px ui-monospace, monospace";
    ctx.fillStyle = run.outcome.type === "home" ? "#bceace" : "#f4cf91";
    ctx.fillText(outcomeText[run.outcome.type].toUpperCase(), cx, height - 22);
  }
}

function resize() {
  const rect = canvas.getBoundingClientRect();
  width = rect.width;
  height = rect.height;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  canvas.width = Math.round(width * dpr);
  canvas.height = Math.round(height * dpr);
  draw();
}

function update(ms) {
  clock += ms;
  if (anim) {
    anim.time += ms;
    if (anim.time > 500) anim = null;
  }
  if (playing) {
    elapsed += ms;
    while (elapsed >= Number($("speed").value) && playing) {
      elapsed -= Number($("speed").value);
      setCursor(cursor + 1);
    }
  }
  draw();
}

function showTab(name) {
  view = name;
  playing = false;
  for (const tab of ["mission", "log", "history"])
    $(tab + "-panel").hidden = tab !== name;
  document.querySelectorAll("[data-tab]").forEach((button) => {
    button.classList.toggle("active", button.dataset.tab === name);
    button.setAttribute("aria-selected", String(button.dataset.tab === name));
  });
  if (name === "log") renderLog();
  if (name === "mission") {
    resize();
    renderInfo();
  }
}

function renderLog() {
  $("log-count").textContent = flights.length;
  $("empty-log").hidden = flights.length > 0;
  $("log-list").replaceChildren();
  flights.forEach((evidence, index) => {
    const r = evidence.run;
    const row = el("article", "log-row");
    const label = el("label", "check-label");
    const checkbox = el("input");
    checkbox.type = "checkbox";
    checkbox.checked = selectedFlights.has(index);
    checkbox.setAttribute(
      "aria-label",
      `Compare flight ${index + 1}: ${ruleText(r.config)} from ${r.config.seed}`,
    );
    checkbox.addEventListener("change", () => {
      if (checkbox.checked && selectedFlights.size >= 3) {
        checkbox.checked = false;
        $("import-notice").textContent =
          "Choose up to three flights to compare.";
        return;
      }
      checkbox.checked
        ? selectedFlights.add(index)
        : selectedFlights.delete(index);
      renderComparison();
    });
    label.append(checkbox);
    row.append(label);
    const description = el("div");
    description.append(
      el("h3", "", `${ruleText(r.config)} · start ${short(r.config.seed, 22)}`),
      el(
        "p",
        "",
        `${modeText(r.config)} · ${new Date(evidence.createdAt).toLocaleString()} · arithmetic rechecked`,
      ),
      el(
        "p",
        "",
        `Recorded revision: ${evidence.sourceRevision ? short(evidence.sourceRevision, 11) : "not recorded"} · engine ${evidence.engineVersion}`,
      ),
    );
    const details = el("details");
    details.append(
      el("summary", "", "Recorded build metadata"),
      el(
        "p",
        "",
        `${evidence.label || "No build label"} · Attribution is supplied metadata, not verified authorship.`,
      ),
    );
    description.append(details);
    row.append(
      description,
      el(
        "p",
        "log-result",
        `${outcomeText[r.outcome.type]} · ${r.steps} moves`,
      ),
    );
    const actions = el("div", "log-actions");
    const replay = el("button", "secondary-button", "Replay ↗");
    replay.addEventListener("click", () => {
      launch(r.config, "REPLAY · SAVED FLIGHT");
      showTab("mission");
      $("flight-deck").scrollIntoView({
        block: "center",
        behavior: reducedMotion ? "instant" : "smooth",
      });
    });
    const remove = el("button", "text-button", "Remove");
    remove.setAttribute("aria-label", `Remove flight ${index + 1}`);
    remove.addEventListener("click", () => {
      try {
        const next = flights.filter((_, i) => i !== index);
        localStorage.setItem(STORAGE, JSON.stringify(next));
        flights = next;
        selectedFlights.clear();
        renderLog();
      } catch {
        $("import-notice").textContent = "Could not update browser storage.";
      }
    });
    actions.append(replay, remove);
    row.append(actions);
    $("log-list").append(row);
  });
  renderComparison();
}

function renderComparison() {
  const chosen = [...selectedFlights].map((i) => flights[i].run);
  $("comparison").hidden = chosen.length < 2;
  $("comparison").replaceChildren();
  if (chosen.length < 2) return;
  const wrapper = el("div", "comparison-table");
  const table = el("table");
  table.append(el("caption", "", "Same idea. Different journeys."));
  const head = el("thead"),
    tr = el("tr");
  tr.append(el("th", "", "Measure"));
  chosen.forEach((r) => tr.append(el("th", "", ruleText(r.config))));
  head.append(tr);
  table.append(head);
  const rows = [
    ["Starting number", (r) => r.config.seed],
    ["Move convention", (r) => modeText(r.config)],
    ["Calculated outcome", (r) => outcomeText[r.outcome.type]],
    ["Displayed moves", (r) => String(r.steps)],
    ["Elementary steps", (r) => String(r.elementarySteps)],
    ["Highest displayed value", (r) => r.peak],
    ["Limit (displayed moves)", (r) => String(r.config.maxSteps)],
  ];
  const body = el("tbody");
  rows.forEach(([name, get]) => {
    const row = el("tr");
    row.append(el("th", "", name));
    chosen.forEach((r) => row.append(el("td", "", get(r))));
    body.append(row);
  });
  table.append(body);
  wrapper.append(table);
  $("comparison").append(
    wrapper,
    el(
      "p",
      "comparison-note",
      "Compare matching starts and move conventions for a fair comparison. Odd-only mode omits even values, so its displayed peak can be lower. These are finite observations, not a ranking of proofs or AI models.",
    ),
  );
}

function renderHistory() {
  $("history-list").replaceChildren();
  for (const change of PROVENANCE.changes) {
    const article = el("article", "history-item");
    const time = el("time", "", change.date);
    time.dateTime = change.date;
    const content = el("div");
    content.append(
      el("h3", "", change.title),
      el("p", "", change.meaning),
      el("p", "", `Recorded author: ${change.author}`),
    );
    const link = el("a", "", change.hash.slice(0, 7) + " ↗");
    link.href = change.url;
    link.target = "_blank";
    link.rel = "noreferrer";
    article.append(time, content, link);
    $("history-list").append(article);
  }
  $("build-note").textContent =
    `App ${PROVENANCE.appVersion} · engine ${ENGINE_VERSION} · research baseline ${PROVENANCE.sourceRevision.slice(0, 7)} · app revision ${build.revision ? build.revision.slice(0, 7) : "unavailable on this static host"}${build.dirty === true ? " + working changes" : ""}. ${build.engineSha256 ? `Engine SHA-256: ${build.engineSha256}` : ""}`;
}

$("play").addEventListener("click", togglePlay);
$("next").addEventListener("click", () => {
  playing = false;
  elapsed = 0;
  lastFeedback = "";
  setCursor(cursor + 1);
});
$("back").addEventListener("click", () => {
  playing = false;
  elapsed = 0;
  lastFeedback = "";
  setCursor(cursor - 1);
});
$("restart").addEventListener("click", () => {
  playing = false;
  elapsed = 0;
  lastFeedback = "";
  setCursor(0, false);
});
$("timeline").addEventListener("input", (event) => {
  playing = false;
  elapsed = 0;
  lastFeedback = "";
  setCursor(Number(event.target.value), false);
});
$("guess-in").addEventListener("click", () => prediction("contract"));
$("guess-out").addEventListener("click", () => prediction("expand"));
$("guess-same").addEventListener("click", () => prediction("steady"));
$("save").addEventListener("click", saveFlight);
$("save-result").addEventListener("click", saveFlight);
document.querySelectorAll("[data-mission]").forEach((button) =>
  button.addEventListener("click", () => {
    const mission = missions[button.dataset.mission];
    launch(
      { ...mission, mode: "standard" },
      mission.label,
      button.dataset.mission,
    );
  }),
);
document
  .querySelectorAll("[data-tab]")
  .forEach((button) =>
    button.addEventListener("click", () => showTab(button.dataset.tab)),
  );
$("go-mission").addEventListener("click", () => showTab("mission"));
$("rule-select").addEventListener("change", () => {
  $("custom-rule").hidden = $("rule-select").value !== "custom";
});
$("lab-form").addEventListener("submit", (event) => {
  event.preventDefault();
  const rule = RULES.find((r) => r.id === $("rule-select").value);
  try {
    launch(
      {
        seed: $("seed").value.trim(),
        multiplier: rule ? rule.multiplier : $("multiplier").value,
        offset: rule ? rule.offset : $("offset").value,
        mode: $("map-mode").value,
      },
      "EXPERIMENT · YOUR RULE",
    );
    $("flight-deck").scrollIntoView({
      block: "center",
      behavior: reducedMotion ? "instant" : "smooth",
    });
  } catch (error) {
    $("form-error").hidden = false;
    $("form-error").textContent = error.message;
  }
});
$("export").addEventListener("click", () => {
  const evidence = makeEvidence(run, {
    sourceRevision: build.revision,
    label: provenanceLabel(),
  });
  const blob = new Blob([JSON.stringify(evidence, null, 2)], {
    type: "application/json",
  });
  const url = URL.createObjectURL(blob);
  const link = el("a");
  link.href = url;
  link.download = `orbit-${run.config.seed.slice(0, 20)}-${run.config.multiplier}n${BigInt(run.config.offset) > 0n ? "+" : ""}${run.config.offset}.json`;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  $("save-notice").textContent =
    "Exported the full calculated journey. Import it to recheck every move.";
});
$("import").addEventListener("change", async (event) => {
  const file = event.target.files[0];
  if (!file) return;
  try {
    if (file.size > 8 * 1024 * 1024)
      throw new Error("File exceeds the 8 MiB import limit.");
    const evidence = JSON.parse(await file.text());
    const check = verifyEvidence(evidence);
    if (!check.valid) throw new Error(check.error);
    $("import-notice").textContent =
      `Every calculation verified. ${remember(evidence)}`;
  } catch (error) {
    $("import-notice").textContent = `Replay rejected: ${error.message}`;
  }
  event.target.value = "";
});
function openHelp() {
  playing = false;
  renderInfo();
  $("help").showModal();
}
$("help-button").addEventListener("click", openHelp);
$("close-help").addEventListener("click", () => $("help").close());
$("start-playing").addEventListener("click", () => $("help").close());
async function fullscreen() {
  try {
    document.fullscreenElement
      ? await document.exitFullscreen()
      : await $("flight-deck").requestFullscreen();
  } catch {
    $("save-notice").textContent =
      "Fullscreen is not available in this browser.";
  }
}
$("fullscreen").addEventListener("click", fullscreen);
document.addEventListener("keydown", (event) => {
  if (
    /INPUT|SELECT|TEXTAREA|BUTTON/.test(event.target.tagName) ||
    event.target.isContentEditable ||
    $("help").open ||
    view !== "mission"
  )
    return;
  if (event.code === "Space") {
    event.preventDefault();
    togglePlay();
  }
  if (event.code === "ArrowRight") {
    event.preventDefault();
    playing = false;
    elapsed = 0;
    setCursor(cursor + 1);
  }
  if (event.code === "ArrowLeft") {
    event.preventDefault();
    playing = false;
    elapsed = 0;
    setCursor(cursor - 1);
  }
  if (event.code === "KeyF") fullscreen();
});
document.addEventListener("visibilitychange", () => {
  if (document.hidden) {
    playing = false;
    renderInfo();
  }
});
new ResizeObserver(resize).observe(canvas);
window.addEventListener("resize", resize);
document.addEventListener("fullscreenchange", resize);
window.render_game_to_text = () =>
  JSON.stringify({
    mode: playing
      ? "playing"
      : cursor === run.steps
        ? run.outcome.type
        : "paused",
    tab: view,
    coordinateSystem:
      "Canvas top-left origin; x right, y down. Radial distance represents log2(number), not physical distance; angle is a stable decorative layout.",
    rule: run.config,
    mission: currentLabel,
    step: cursor,
    number: run.frames[cursor].value,
    operation: run.frames[cursor].operation,
    elementarySteps: run.frames[cursor].elementarySteps,
    ship: displayedShip || shipPoint(run.frames[cursor].value),
    target: shipPoint(run.frames[cursor].value),
    home: { x: width * 0.5, y: height * 0.5 + 9, number: "1" },
    outcome: cursor === run.steps ? run.outcome : null,
    predictionScore: {
      correct: [...guesses.values()].filter(Boolean).length,
      attempted: guesses.size,
    },
    savedFlights: flights.length,
    sourceRevision: build.revision,
  });
let manualUntil = 0;
window.advanceTime = (ms) => {
  manualUntil = performance.now() + 150;
  for (let remaining = ms; remaining > 0; remaining -= 16.6667)
    update(Math.min(16.6667, remaining));
};
let lastTime = performance.now();
function loop(now) {
  const dt = Math.min(100, now - lastTime);
  lastTime = now;
  if (now >= manualUntil && view === "mission") update(dt);
  requestAnimationFrame(loop);
}
loadFlights();
launch({ ...missions.home, mode: "standard" }, missions.home.label, "home");
renderHistory();
loadBuild();
requestAnimationFrame(loop);
