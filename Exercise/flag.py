#code for flag triangle
def ftri():
                a=int(input("Enter the no of lines in flag triangle: "))
                print(a)
                if(a==0):
                    print("error")
                else:
                    for i in range(1,a+1):
                        print('*'*i)
                        print("\n")
