#checking prime no or not
def prime():
        a=int(input("Enter the no upto which "))
        if(a==1):
                print(1)
        elif(a==2):
                print(1)
                print(2)
        else:
                i=2
                f=1
                n=3
                j=3
                print 1,"\n",2
                while(j<=a):
                        i=2
                        f=1
                        while(i<=n/2):
                                if(n%i == 0):
                                        f=0
                                        break
                                else:
                                        i=i+1
                        if(f==0):
                                n=n+1
                        else:
                                k=n
                                n=n+1
                                j=j+1
                                print(k)
                                
