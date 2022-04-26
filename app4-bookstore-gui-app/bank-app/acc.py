# __main__ - is the name of the module executed which is acc.py, if you import acc.py __main__ will be account.acc.Account where account=package acc=module and Account=class

# class - blueprint

# base class - generic class
class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


# inheritance is creating new class out of the base class
# subclass - pass argument which is the base class

class Checking(Account):
    # Doc strings - written right after creating a class to provide info/details about a class
    """This class generates checking account object """

    # class variable - declared outside of methods shared across all methods or instances
    type = "checking"  # data members -refer to class or instance variables

    # __init___ is a special method called constructor
    def __init__(self, filepath, fee):
        # have access to all methods in Account class
        Account.__init__(self, filepath)
        # create new instance variable specific for Checking subclass
        self.fee = fee

    # transfer is a new method specific for Checking subclass
    def transfer(self, amount):
        # can access instance variable from base class
        self.balance = self.balance - amount - self.fee


# checking = object instance or instantiation
john_checking = Checking("john_balance.txt", 10)
# access methods of base class in subclass without re-writing them
john_checking.transfer(200)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)

# checking = object instance
wick_checking = Checking("wick_balance.txt", 10)
# access methods of base class in subclass without re-writing them
wick_checking.transfer(200)
print(wick_checking.balance)  # .balance is called attributes
wick_checking.commit()
print(wick_checking.type)

print(john_checking.__doc__)
