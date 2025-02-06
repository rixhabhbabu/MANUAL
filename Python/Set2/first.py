class Customer:
    def __init__(self,customer_id,name,age,phone = 0,address = ""):
        self.customer_id = customer_id
        self.name = name 
        self.age  = age
        self.phone = phone
        self.address = address
        
    def update_info(self,new_address,new_phone):
        if new_address:
            self.address = new_address
        if new_phone:
            self.phone = new_phone
            
    def __str__(self):
        return f"CUSTOMER NAME:{self.name}\nAGE:{self.age}\nPHONE:{self.phone}\nADDRESS:{self.address}"
    
class Account:
    def __init__(self,account_number,customer,account_type = "Cheaking",initial_balance = 0.0):
        self.account_number = account_number
        self.customer = customer
        self.account_type = account_type
        self.balance = initial_balance
        self.transaction = ["Account created Succcessfully"] 
        
    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(f"{amount} is Credit in your Account")   
            return True
        return False
   
    def withdraw(self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction.append(f"{amount} is Debit from your Account")   
            return True
        return False 
    
    def get_balance(self):
        return self.balance
    
    def transaction_history(self):
        return self.transaction.copy()
    
    def __str__(self):
        return f"ACCOUNT NUMBER:{self.account_number}\nACCOUNT TYPE:{self.account_type}\nBALANCE:{self.balance}"       
    
 
class Bank:
    def __init__(self,name):
        self.name = name
        self.customer = {}
        self.account = {}
        self.next_customer_id = 1
        self.next_account_number = 1000
        
    def add_customer(self,name,age,phone = "",address = ""):
        customer_id = self.next_customer_id
        new_customer = Customer(customer_id,name,age,phone,address) 
        self.customer[customer_id] = new_customer
        self.next_customer_id +=1
        return new_customer
    
    def create_account(self,customer_id,account_type = "Cheaking",initial_balance = 0.0):
             if customer_id not in self.customer:
                 return None
             customer = self.customer[customer_id]
             account_number = self.next_account_number
             new_account = Account(account_number,customer,account_type,initial_balance=0.0)
             self.account[account_number] = new_account
             self.next_account_number += 1
             return new_account
         
    def deposite(self,account_number,amount):
        account = self.account.get(account_number)
        if account:
            return account.deposite(amount) 
        return False
    
    def withdraw(self,account_number,amount):
        account = self.account.get(account_number)
        if account:
            return account.withdraw(amount) 
        return False
    
    def get_balance(self,accout_number):
        account = self.account.get(accout_number)
        if account:
            return self.get_balance()
        return False   
    
    def transfer(self,from_account,to_account,amount):
        if self.withdraw(from_account,amount):
            if self.deposite(to_account,amount):
                return True
            self.deposite(from_account,amount)
        return False
    
    def __str__(self):
        return f"BANK NAME: {self.name}\nNO OF CUSTOMERS:{len(self.customer)}\nNO OF ACCOUNTS:{len(self.account)}"    
        
        
bank1 = Bank("CANARA BANK")
bank2 = Bank("SBI BANK")       

c1 = bank1.add_customer("Rishabh babu",17,7818973038,"New shiv nagar Tundla Firozabad")
c2 = bank1.add_customer("Ritesh Verma",19,7505111484,"Anata Shubhlaxmi Khatamba VAdodara Gujrat")
cc1 = bank2.add_customer("Vishal babu",23,7302097162,"New shiv nagar Tundla Firozabad")
# c2 = bank2.add_customer("Rahul Meena",20,7055758523,"Anata Shubhlaxmi Khatamba VAdodara Gujrat")

a1 = bank1.create_account(c1.customer_id,"Saving",7500)
a2 = bank1.create_account(c2.customer_id,"Current",100000)
aa1 = bank2.create_account(c1.customer_id,"Cuurent",1000)

bank1.deposite(a1.account_number,1000)
bank1.deposite(a1.account_number,5000)
bank1.withdraw(a2.account_number,2000)
bank2.deposite(aa1.account_number,1000)

bank1.transfer(a1.account_number,a2.account_number,2000)

print(a1.transaction_history())
print(c1)

 