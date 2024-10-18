def rev():
        a=(input("enter the string"))
        b=len(a)
        print(b)
        if(b==0):
                print("error")
        else:
                c=''
                while(b>=0):
                        c=c+a[b-1]
                        b=b-1
                print("reverse string is %s"%(c))
