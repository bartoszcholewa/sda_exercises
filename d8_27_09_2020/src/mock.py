class User:
    def __init__(self, name, age, accounts):
        self.name = name
        self.age = age
        self.accouts = accounts

    def return_available_funds(self):
        available_funds = 0
        for account in self.accouts:
            available_funds += account.get_balance()
        return available_funds