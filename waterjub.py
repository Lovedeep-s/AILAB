jug1,jug2=3,4
aim = 2

def jug(amt1,amt2):
    run=1
    while(run):
        if (amt1==aim and amt2==0) or (amt1==0 and amt2==aim):
            print ("reached poistion",amt1,amt2)
            run=0
            break
        if amt1==0:
            amt1=jug1
        print("state reached",amt1,amt2)
        if amt1 <= 3 and amt1>0:
            if  amt2==0:
                amt2+=amt1
                amt1=0
            elif amt2>0:
                s=jug2-amt2
                if amt1>s:
                    amt1-=s
                    amt2+=s
                elif amt1<s:
                    amt1=0
                    amt2+=s
        print("state reached",amt1,amt2)
        if amt2==4:
            amt2=0
        print("state reached",amt1,amt2)
        
jug(0,0)    
    