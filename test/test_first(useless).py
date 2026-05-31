# #-v -s tag 
# import pytest
# # def add(a,b):
# #     return a+b
# # @pytest.mark.parametrize("num1, num2, expected",[
# #     (3,2,5),
# #     (7,8,15),
# #     (10,2,12)
# # ])
# # def test_add(num1,num2,expected):
# #     print("testing add function")
# #     assert add(num1,num2) == expected
# class InsufficientFunds(Exception):
#     pass
# class BankAccount():
#     def __init__(self, starting_balance=0):
#         self.balance = starting_balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount>self.balance:
#             raise InsufficientFunds("insufficient balance")
#         # if i raise any other exception it wont work like zerodivision error etc it wont pass
#         self.balance -= amount

#     def collect_interest(self):
#         self.balance *= 1.1
# def test_bank():
#     bank_account =BankAccount(50)
#     assert bank_account.balance == 50
# def test_bank2():
#     bank_account =BankAccount(50).balance
#     assert bank_account == 50
# def test_bank3():
#     bank_account =BankAccount(50)
#     bank_account.deposit(40)
#     assert bank_account.balance == 90
# def test_bank4():
#     bank_account =BankAccount(50)
#     bank_account.collect_interest()
#     assert bank_account.balance == pytest.approx(55)
# @pytest.fixture
# def zero_balance():
#     return BankAccount()
# @pytest.fixture
# def bank_account_start():
#     return BankAccount(50)

# def test_bank6(bank_account_start):
#     assert bank_account_start.balance ==50
# @pytest.mark.parametrize("deposited, withdrew, expected",[
#    (3,2,1),
    
#      (10,2,8)
# ])
# def test_bank7(zero_balance,deposited,withdrew,expected):
#     zero_balance.deposit(deposited)
#     zero_balance.withdraw(withdrew)
#     assert zero_balance.balance == expected
# def test_insufficientfund(zero_balance):
#     with pytest.raises(InsufficientFunds):
#         zero_balance.withdraw(50) #only accepts if a exception is raised
