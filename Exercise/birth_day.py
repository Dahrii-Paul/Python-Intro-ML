# Birth Day
import time
import locale
def age():
    dob=input("Enter your date of birth in dd-mm-yyyy format")
    if(dob[2] != "-" and dob[5] !="-" ):
        print("Error in input date format")
    else:
        d=time.strptime(dob,"%d-%m-%Y")
        t=time.gmtime()
        ag=t.tm_year -d.tm_year
        mn=t.tm_mon-d.tm_mon
        da=t.tm_mday-d.tm_mday
        if(da<0):
            da=abs(da)
            m=t.tm_mon
            if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
                da=31-da
            elif(m==4 or m==6 or m==9 or m==11):
                da=30-da
            else:
                if(t.tm_year%4 ==0 or d.tm_year%4== 0):
                    da=29-da
                else:
                    da=28-d.tm_mday
            mn=mn-1
        if(mn<0):
            mn=abs(mn)
            mn=12-mn
            ag=ag-1
        print "Your age is", ag,"years",mn,"Month",da,"day"
