from collections import deque
import copy

R='ABCDEFGHI'
C='123456789'

vs=[r+c for r in R for c in C]

def units():
    u=[]
    for r in R:
        u.append([r+c for c in C])
    for c in C:
        u.append([r+c for r in R])
    for rb in ['ABC','DEF','GHI']:
        for cb in ['123','456','789']:
            u.append([r+c for r in rb for c in cb])
    return u

us=units()

vu={v:[u for u in us if v in u] for v in vs}

ps={v:set(p for u in vu[v] for p in u if p!=v) for v in vs}

def arcs():
    a=set()
    for u in us:
        for i in range(len(u)):
            for j in range(len(u)):
                if i!=j:
                    a.add((u[i],u[j]))
    return list(a)

as_=arcs()

PZ=(
"003020600"
"900305001"
"001806400"
"008102900"
"700000008"
"006708200"
"002609500"
"800203009"
"005010300"
)

def parse(s):
    d={}
    for i,v in enumerate(vs):
        x=int(s[i])
        d[v]=[x] if x!=0 else list(range(1,10))
    return d

def rev(d,xi,xj):
    ch=False
    for v in d[xi][:]:
        if not any(v!=o for o in d[xj]):
            d[xi].remove(v)
            ch=True
    return ch

def ac3(d):
    q=deque(as_)
    while q:
        xi,xj=q.popleft()
        if rev(d,xi,xj):
            if not d[xi]:
                return False
            for xk in ps[xi]:
                if xk!=xj:
                    q.append((xk,xi))
    return True

def done(d):
    return all(len(x)==1 for x in d.values())

def pick(d,a):
    u=[v for v in vs if v not in a]
    return min(u,key=lambda v:len(d[v]))

def ok(v,val,a):
    return all(a.get(p)!=val for p in ps[v])

def fwd(v,val,d):
    pr={}
    for p in ps[v]:
        nd=[x for x in d[p] if x!=val]
        if not nd:
            return None,pr
        if len(nd)!=len(d[p]):
            pr[p]=d[p][:]
            d[p]=nd
    return True,pr

def bt(a,d):
    if len(a)==len(vs):
        return a
    v=pick(d,a)
    for val in d[v][:]:
        if ok(v,val,a):
            a[v]=val
            good,pr=fwd(v,val,d)
            if good:
                r=bt(a,d)
                if r:
                    return r
            a.pop(v)
            for p,s in pr.items():
                d[p]=s
    return None

def solve(d):
    d=copy.deepcopy(d)
    if not ac3(d):
        return None
    if done(d):
        return {v:d[v][0] for v in vs}
    a={v:d[v][0] for v in vs if len(d[v])==1}
    return bt(a,d)

def show(src,lab=""):
    if lab:
        print(f"\n{lab}\n")
    for i,r in enumerate(R):
        row=[]
        for j,c in enumerate(C):
            v=r+c
            if isinstance(src,dict):
                d=src.get(v)
                if d is None:
                    x="."
                elif isinstance(d,list):
                    x=str(d[0]) if len(d)==1 else "_"
                else:
                    x=str(d)
            else:
                x="."
            row.append(x)
        line=""
        for k,x in enumerate(row):
            if k in [3,6]:
                line+="| "
            line+=x+" "
        print(f"  {line}")
        if i in [2,5]:
            print("  ------+-------+------")
    print()

def inp():
    print("\nEnter puzzle with 9 digits in each row (enter 0 for a blank):\n")
    s=""
    for i,r in enumerate(R,1):
        while True:
            row=input(f"Row {i}: ").strip()
            if len(row)==9 and all(ch.isdigit() for ch in row):
                s+=row
                break
            print("Enter exactly 9 digits")
    return s

print("\n*** Sudoku (Constraint Satisfaction Problem) ***\n")

pz=None
d=None

while True:
    print("1. Load textbook puzzle")
    print("2. Enter custom puzzle")
    print("3. Solve currently loaded puzzle")
    print("4. Show current puzzle")
    print("5. Exit\n")

    try:
        ch=int(input("Enter choice: "))
    except ValueError:
        print("Enter a number between 1 and 5\n")
        continue

    if ch==1:
        pz=PZ
        d=parse(pz)
        show(d,"Puzzle:")

    elif ch==2:
        pz=inp()
        d=parse(pz)
        show(d,"Puzzle:")

    elif ch==3:
        if d is None:
            print("Please load a puzzle first (use option 1 to load the textbook puzzle from figure 6.4a) \n")
            continue
        sol=solve(d)
        if sol:
            show(sol,"Solution:")
        else:
            print("No solution found for this puzzle, please enter a different puzzle\n")

    elif ch==4:
        if d is None:
            print("No puzzle loaded yet (use option 1 to load the textbook puzzle from figure 6.4a)\n")
        else:
            show(d,"Current puzzle:")

    elif ch==5:
        break

    else:
        print("Please enter a number between 1 and 5\n")
