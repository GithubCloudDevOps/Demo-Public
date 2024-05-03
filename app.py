n=int(input("enter any number:")) #4926 #153
if(n<=0):
    print("{} is invalid input".format(n))
else:
    s=0
    tn=n #here we are pre serving original n value in another variable tn
    while(n>0):
        r=n%10
        s=s+r**3
        n=n//10
    else:
        if(s==tn):
            print("{} is amstrong".format(tn))
        else:
            print("{} is not amstrong".format(tn))
