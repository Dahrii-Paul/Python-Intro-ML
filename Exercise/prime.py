#checking prime no or not
def perfect():
        a=int(input("Enter the no upto which "))
        i=2
        n=2
        j=1
        su=1
        while(j<=a):
                i=2
                print("n,j",n,j)
                while(i<=n/2):
                        if(n%i == 0):
                                su=su+i
                                i=i+1
                        else:
                                i=i+1
                if(su == n):
                        print(n)
                        n=n+1
                        j=j+1
                else:
                        n=n+1
                       
