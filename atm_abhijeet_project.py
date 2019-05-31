class account:
    def register(self,regno,accno,bal,pin):
        f=open(str(pin)+".txt","w")
        f.write("regno,accno,bal\n")
        f.write(str(regno)+","+str(accno)+","+str(bal))
        print("new file created with the name" +str(pin)+".txt")
    def deposit(self,pin,damount):
        f=open(str(pin)+".txt","r")
        y=[]
        j=0
        for i in f:
            x=i.split(',')
            print("ohh",x)
            if not y:
                y=x
                #print("poh",y)
            if j==0:
                j=1
            else:
                k=int(x[2])
                newamount=k+damount
                print(newamount)
                x[2]=str(newamount)
        f1=open(str(pin)+".txt","w")
        f1.write(y[0]+','+y[1]+','+y[2])
        f1.write(x[0]+','+x[1]+','+x[2])
        f.close()
        f1.close()
    def withdraw(self,pin,wamount):
        f=open(str(pin)+".txt","r")
        y=[]
        j=0
        for i in f:
            x=i.split(',')
            print(x)
            if not y:
                y=x
            if j==0:
                j=1
            else:
                k=int(x[2])
                if k<=1000:
                    print("balance is law")
                else:
                    newamount=k-wamount
                    print(newamount)
                    x[2]=str(newamount)
        f1=open(str(pin)+".txt","w")
        f1.write(y[0]+','+y[1]+','+y[2])
        f1.write(x[0]+','+x[1]+','+x[2])
        f.close()
        f1.close()
obj=account()

#obj.register(1234,66666,1000,2000)
x=int(input("enter the deposit amount"))            
obj.deposit(2000,x)
y=int(input("enter the withdraw amount"))           
obj.withdraw(2000,y)
       
        
