
class Bank:

    def __init__(self,user1_avail_bal,user2_avail_bal,amount):
        self.user1_avail_bal=250
        self.user2_avail_bal=100
        #self.amount=1000
    def balance(self):
        self.user1_avail_bal=self.user1_avail_bal+self.amount_deposit-self.amount_withdraw
        self.user2_avail_bal = self.user2_avail_bal + self.amount_deposit - self.amount_withdraw
    def deposit(self,amount_to_deposit):
        try:
            if amount_to_deposit<=1000:
                print("enter amount to be deposit:",amount_to_deposit)
        except:
            print("enter the amount upto 1000")
    def withDraw(self,amount_to_withdraw):
        print("user1 avaible balance")





bank=Bank()
bank.balance()
amount_deposit=int(input())
bank.deposit(amount_deposit)
amount_withdraw=int(input())
bank.withDraw()


class Bank:
    





















