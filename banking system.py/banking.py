class bank:
    def __init__(self):
        self.client_details_list=[]
        self.logedin=False
        self.cash=100
        self.TransferCash=False
     # user register
    def register(self,name,ph,password):
        cash=self.cash
        conditions=True    
        if len(str(ph))>10 or len(str(ph))<10:
            print("invalid phone number! please enter 10 digit number")
            conditions=False 
        if len(str(password))<7 or len(str(ph))>10:
            print("Enter password greater than 7 and less than 10 character")    
            conditions=False
        if  conditions==True: 
            print("Account created successfully")
            self.client_details_list=[name,ph,password,cash]
            with open(f"{name}.txt","w")as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")
    #   user login              
    def login(self,name,ph,password): 
        with open(f"{name}.txt","r")as f:
            details=f.read()
            self.client_details_list=details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.logedin= True
            if self.logedin==True:  
                print(f"{name}logged in") 
                self.cash=int(self.client_details_list[3])
                self.name=name  
            else:
                print("wrong details")  
     # user add amount in account
    def add_cash(self,amount):
        if amount>0:
            self.cash+=amount
            with open(f"{name}.txt","r")as f:
                details=f.read()
                self.client_details_list=details.split("\n")
            with open (f"{name}.txt","w")as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash))) 
                print("Amount added successfully")
        else:
            print("Enter correct value of amount ")
    # user Transfer amount to another user         
    def  Transfer_cash(self, amount,name,ph): 
         with open(f"{name}.txt","r")as f:
                details=f.read()
                self.client_details_list=details.split("\n")
                if str(name) in self.client_details_list:
                    self.TransferCash=True
                if self.TransferCash==True: 
                    total_cash=int(self.client_details_list[3])+amount
                    left_cash =self.cash-amount
                    with open (f"{name}.txt","w")as f:
                        f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))
                    with open(f"{self.name}.txt","r")as f:
                        details_2=f.read()
                        self.client_details_list=details_2.split("\n") 
                    with open (f"{self.name}.txt","w")as f:
                        f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash))) 
                    print("Amount transfered successfully to",name,"-",ph)
                    print("Balance left=",left_cash)
    #  change user password                  
    def password_change(self,password):
        if len(str(password))<7 or len(str(ph))>10:
            print("Enter password greater than 7 and less than 10 character") 
        else:
            with open(f"{self.name}.txt","r")as f:
                details=f.read()
                self.client_details_list=details.split("\n")
            with open (f"{self.name}.txt","w")as f:
                f.write(details.replace(str(self.client_details_list[3]),str(password))) 
                print("Change your password successfully") 
    # change user moblie number             
    def ph_change (sel,ph):
        if len(str(ph))>10 or len(str(ph))<10:
            print("invalid phone number! please enter 10 digit number")
        else:
            with open(f"{self.name}.txt","r")as f:
                details=f.read()
                self.client_details_list=details.split("\n")
            with open (f"{self.name}.txt","w")as f:
                f.write(details.replace(str(self.client_details_list[3]),str(ph))) 
                print("Change your phone number successfully") 
# bank menu                
if __name__=="__main__":
    bank_object=bank()
    print("welcome to world bank")
    print("==================")
    print("1.Login")
    print("2.Create a new account")
    print('- - - - - - - - - - - ')
    user=int(input("choose your option:"))

    if user==1:
        print("Loggin in")
        name=input("Enter your full name:")  
        ph=int(input("Enter your  10 digits moblie number:"))
        password=input("Enter your password:")    
        bank_object.login(name,ph,password) 
        while True:
            if bank_object.logedin:
                print("1.Add amount")
                print("2.Check Balance")
                print("3.transfer amount")
                print("4.Edit profile")
                print("5.Logout")
                print('- - - - - - - - - - - ')                
                login_user=int(input("choose your option:"))
                if login_user==1:
                    print("Balance=",bank_object.cash)
                    amount=int(input("Enter amount:"))
                    bank_object.add_cash(amount)
                    print("\n 1.back main menu:")
                    print("2.Logout")
                    print('- - - - - - - - - - - ') 
                    choose=int(input("choose your option:"))
                    if choose==1:
                        continue
                    elif choose==2:
                        break
                elif login_user==2:
                    print("Loggin in")
                    name=input("Enter your full name:")  
                    ph=int(input("Enter your  10 digits moblie number:"))
                    password=input("Enter your password:")    
                    print("Balance=",bank_object.cash) 
                    print("\n 1.back main menu")
                    print("2.Logout")
                    print('- - - - - - - - - - - ') 
                    choose=int(input("choose your option:"))
                    if choose==1:
                        continue
                    elif choose==2:
                        break 
                elif login_user==3:
                    print("Balance=",bank_object.cash)
                    amount=int(input("Enter your transfer amount:"))
                    if amount>0 and amount<bank_object.cash:
                        name=input("Enter person name who want you transfer:")
                        ph=int(input("Enter 10 digit phone number"))
                        bank_object.Transfer_cash(amount,name,ph)
                        print("\n 1.back main menu")
                        print("2.Logout")
                        print('- - - - - - - - - - - ') 
                        choose=int(input("choose your option:"))
                        if choose==1:
                            continue
                        elif choose==2:
                            break 
                    elif amount<0:
                        print("Please enter correct amount")
                    elif amount>bank_object.cash:
                        print("NO money has left your account for this payment")
                elif login_user==4:
                    print("1>change password ")    
                    print("2>change phone number") 
                    edit_profile=int(input("choose your option:"))
                    if edit_profile==1:
                        new_password=input("Enter your new password:")
                        bank_object.password_change(new_password) 
                        print("\n 1.back main menu")
                        print("2.Logout")
                        print('- - - - - - - - - - - ') 
                        choose=int(input("choose your option:"))
                        if choose==1:
                            continue
                        elif choose==2:
                            break 
                    elif edit_profile ==2:
                        new_ph=int(input("Enter your new phone number:"))
                        bank_object.ph_change(new_ph) 
                        print("\n 1.back main menu")
                        print("2.Logout")
                        print('- - - - - - - - - - - ') 
                        choose=int(input("choose your option:"))
                        if choose==1:
                            continue
                        elif choose==2:
                            break 
                    elif login_user==5:
                        break 
                    print("Thank you for spendig your valuable time") 
    # open  new account                          
    if user==2:
        print("creating a new account")  
        name=input("Enter your full name:")  
        ph=int(input("Enter your  10 digits moblie number:"))
        password=input("Enter your password:")    
        bank_object.register(name,ph,password)           


                    
                        







         
