#palindome
def pal():
        a=(input("enter the string"))
        b=len(a)
        print(b)
        if(b==-1):
                prin("error")
        else:
                i=0
                flag=0
                k=(b-1)/2
                print(a[i],a[b-1-i],k)
                while(i<k+1):
                        if(a[i]!=a[b-i-1]):
                                flag=0
                                break
                        else:
                                flag=1
                                i=i+1
                if(flag==0):
                        print("the string is not palindromic")
                else:
                        print("the string is palindromic")
                        
