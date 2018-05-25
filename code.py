from random import randint
class tickets():
    def __init__(self):
       self.holders ={}
    def Purchase_ticket (self,Name,Category):
        self.ticket_num =randint(10000,99999)
        self.Name= Name
        if Category=="1":
            print("You have to pay $100 for VIP")
            self.price=100
            self.rank="VIP"
            self.holders[self.ticket_num] = [self.price, self.Name, self.rank]
        elif Category=="2":
            print("You have to pay $50 for Gold")
            self.price= 50
            self.rank ="Gold"
            self.holders[self.ticket_num] = [self.price, self.Name, self.rank]
        elif Category== "3":
            print("You have to pay $30 for Regular")
            self.price =30
            self.rank ="Regular"
            self.holders[self.ticket_num] = [self.price, self.Name, self.rank]
        print(Name,"your ticket no. is ",self.ticket_num,"and is of type:",self.rank,"")
    def authenticate(self,name,ticket_number):
        if ticket_number in self.holders.keys():
            if self.holders[ticket_number][1]==name:
                print("you are allowed to enter")
                return True
            else:
                print("You are not allowed!!!")
                return False
        else:
            print("You are not allowed!!!")
            return False
    def upgrade(self,ticket_number,new_price,new_rank):
        if new_price<=self.holders[ticket_number][0]:
            print("You cant downgrade your ticket")
        else:
            print("You have to pay ",new_price-self.holders[ticket_number][0],"more")
            self.holders[ticket_number][0] = new_price
            self.holders[ticket_number][2] = new_rank

    def check_status(self,ticket_number):
        print("You have purchased",self.holders[ticket_number][2])


client1 = tickets()
while True:

    ans=input("To buy press 1 or press 2 to enter or 3 to upgrade/check status or any other key to exit: ")
    if ans =="1":
        nam=input("Enter your name: ").title()
        Cat=input("Press 1 to buy Vip , 2 for Gold or 3 for regular: ")
        client1.Purchase_ticket(nam,Cat)
    elif ans =="2":
        chk_nam =input("Enter your name: ").title()
        chk_tckt =int(input("Enter your ticket no."))
        client1.authenticate(chk_nam,chk_tckt)
    elif ans== "3":
        chk_nam = input("Enter your name: ").title()
        chk_tckt = int(input("Enter your ticket no.: "))
        if client1.authenticate(chk_nam, chk_tckt):
            client1.check_status(chk_tckt)
            upgrade_rank=input("Press 1 for Gold, 2 for VIP or 3 for exit: ")
            if upgrade_rank=="1":
                client1.upgrade(chk_tckt,50,"Gold")
                continue
            elif upgrade_rank== "2":
                client1.upgrade(chk_tckt,100,"VIP")
                continue
            elif upgrade_rank=="3":
                exit()
            else:
                print("Invalid Input!!")
                pass

        else:
            print("You are not authorized")
            continue
    else:
       exit()
