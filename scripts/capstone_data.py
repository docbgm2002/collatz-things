import math, statistics
THETA=math.log2(3)
def U(n): return n//2 if n%2==0 else (3*n+1)//2
def v2(x): return (x & -x).bit_length()-1

def tail_density(n):
    T=(1<<n)-1; x=(3**n-1)//2; odd=0; tot=0
    while x>=T and tot<10_000_000:
        if x&1: odd+=1
        x=U(x); tot+=1
        if x<T: break
    return odd/tot, tot
def max_deficit(n):
    x=(3**n-1)//2; E=0; T=(1<<n)-1; K=0; best=-1e9
    while x>=T and K<3_000_000:
        val=3*x+1; e=v2(val); x=val>>e; E+=e; K+=1
        d=K*THETA-E
        if d>best: best=d
        if x<T: break
    return best

print("=== ODD-DENSITY BANDS ===")
data=[]
for n in range(7,3000,2):
    f,t=tail_density(n); data.append((n,f))
for lo,hi in [(7,200),(200,800),(800,1600),(1600,3000)]:
    fr=[f for (nn,f) in data if lo<=nn<hi]
    print(f"[{lo},{hi}): mean={statistics.fmean(fr):.4f} max={max(fr):.4f} stdev={statistics.pstdev(fr):.4f}")
print("global max density:", max(f for _,f in data), "at n=", max(data,key=lambda r:r[1])[0])

print("\n=== DEFICIT RECORDS ===")
champ=-1e9
for n in range(7,2500,2):
    d=max_deficit(n)
    if d>champ: champ=d; print(f"n={n}: maxD={d:.4f}")
