from collections import deque
import os,json

base=os.path.dirname(os.path.abspath(__file__))
path=os.path.join(base,"telangana_adj.json")

with open(path) as f:
    adj=json.load(f)

defs=["Red","Green","Blue","Black","White","Grey"]

def make_dom(cols):
    return {v:list(cols) for v in adj}

def revise(dom,xi,xj):
    ch=False
    for val in dom[xi][:]:
        if not any(val!=o for o in dom[xj]):
            dom[xi].remove(val)
            ch=True
    return ch

def ac3(dom):
    q=deque((xi,xj) for xi in adj for xj in adj[xi])
    while q:
        xi,xj=q.popleft()
        if revise(dom,xi,xj):
            if not dom[xi]:
                return False
            for xk in adj[xi]:
                if xk!=xj:
                    q.append((xk,xi))
    return True

def ok(var,val,asg):
    return all(asg.get(nb)!=val for nb in adj[var])

def pick(asg,dom):
    left=[v for v in adj if v not in asg]
    return min(left,key=lambda v:len(dom[v]))

def fwd(var,val,asg,dom):
    pr={}
    for nb in adj[var]:
        if nb not in asg:
            nd=[v for v in dom[nb] if v!=val]
            if not nd:
                return None,pr
            pr[nb]=dom[nb][:]
            dom[nb]=nd
    return True,pr

def bt(asg,dom):
    if len(asg)==len(adj):
        return asg
    var=pick(asg,dom)
    for val in dom[var]:
        if ok(var,val,asg):
            asg[var]=val
            good,pr=fwd(var,val,asg,dom)
            if good:
                res=bt(asg,dom)
                if res:
                    return res
            asg.pop(var)
            for nb,s in pr.items():
                dom[nb]=s
    return None

def solve(cols):
    dom=make_dom(cols)
    if not ac3(dom):
        print("No solution possible with these Colours")
        return None
    return bt({},dom)

def show(res):
    if not res:
        print("No solution found\n")
        return
    print("\nSolution:\n")
    print(f"  {'District':<35} Colour")
    print(f"  {'------------------------':<35} -----")
    for d in adj:
        print(f"  {d:<35} {res[d]}")
    print()

print("\n*** Map Colouring Problem for the 33 Districts of Telangana ***\n")

cols=list(defs)
res=None

while True:
    print("1. Solve with Current Colours")
    print("2. Set Custom Colours")
    print("3. Display All Districts")
    print("4. Display Colours in Current Colour Set")
    print("5. Exit\n")

    try:
        ch=int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a number between 1 and 5\n")
        continue

    if ch==1:
        print(f"\nColours in use: {', '.join(cols)}")
        res=solve(cols)
        show(res)

    elif ch==2:
        raw=input("Enter Colours separated by commas (atleast 4 colours recommended)").strip().split(",")
        new=[c.strip() for c in raw if c.strip()]
        if len(new)<3:
            print("Need at least 3 Colours\n")
        else:
            cols=new
            res=None
            print(f"Colours updated: {', '.join(cols)}\n")

    elif ch==3:
        print("\nAll Districts:\n")
        for i,d in enumerate(adj,1):
            print(f"  {i:>2}. {d}")
        print()

    elif ch==4:
        print(f"\nCurrent Colours: {', '.join(cols)}\n")

    elif ch==5:
        break

    else:
        print("Please enter your choice through a number between 1 and 5\n")
