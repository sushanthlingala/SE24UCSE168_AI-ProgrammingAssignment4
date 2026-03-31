L=[]
dom={}

def setup(w1,w2,res):
    global L,dom
    L=list(set(w1+w2+res))
    dom={x:list(range(10)) for x in L}

def word_val(w,a):
    return int("".join(str(a[ch]) for ch in w))

def ok_part(a,w1,w2,res):
    if any(a.get(x)==0 for x in [w1[0],w2[0],res[0]] if x in a):
        return False
    vals=[a[x] for x in a]
    if len(vals)!=len(set(vals)):
        return False
    return True

def ok_full(a,w1,w2,res):
    if not ok_part(a,w1,w2,res):
        return False
    return word_val(w1,a)+word_val(w2,a)==word_val(res,a)

def solve(w1,w2,res):
    order=L

    def bt(a):
        if len(a)==len(L):
            return a if ok_full(a,w1,w2,res) else None
        v=order[len(a)]
        for val in dom[v]:
            a[v]=val
            if ok_part(a,w1,w2,res):
                r=bt(a)
                if r:
                    return r
            a.pop(v)
        return None

    return bt({})

def show(sol,w1,w2,res):
    n1=word_val(w1,sol)
    n2=word_val(w2,sol)
    n3=word_val(res,sol)

    print(f"\n  {w1} = {n1}")
    print(f"+ {w2} = {n2}")
    print(f"  {'-'*len(str(n3))}")
    print(f"  {res} = {n3}")

    print(f"\n  {n1} + {n2} = {n1+n2}")

    print("\n  Values:")
    for x in sorted(sol):
        print(f"    {x} = {sol[x]}")
    print()

w1,w2,res="TWO","TWO","FOUR"
setup(w1,w2,res)

print("\n*** Crypt-analysis Puzzle (Constraint Satisfaction Problem) ***\n")

while True:
    print("1. Find Solution")
    print("2. Add New Words")
    print("3. Show Current Words")
    print("4. Exit\n")

    try:
        ch=int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number between 1 and 4\n")
        continue

    if ch==1:
        sol=solve(w1,w2,res)
        if sol:
            show(sol,w1,w2,res)
        else:
            print("No solution exists for these choice of words, please enter a new set of words using option 2 or use textbook example (Two + Two = Four)\n")

    elif ch==2:
        w1=input("1st Word: ").strip().upper()
        w2=input("2nd Word: ").strip().upper()
        res=input("3rd (Result) Word: ").strip().upper()
        setup(w1,w2,res)
        print("Words updated\n")

    elif ch==3:
        print(f"\n  {w1}")
        print(f"+ {w2}")
        print(f"  {'-'*len(res)}")
        print(f"  {res}\n")

    elif ch==4:
        break

    else:
        print("Please enter a number between 1 and 4\n")
