import hashlib

bank_db = [
    ["1234-1234-1234-1234", "9999-9999-9999-9999"], # accounts
    ["03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
     "9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0"
     ], # passwords: 1234, 0000
    [
        [150,100], # indexed using acc index
        [1000,10000] # 0th: Checking, 1th: Saving
    ]
]


class CardInfo:
    def __init__(self, status, num):
        self.status = status
        self.num = num

    def password_match(self, password_input):
        result = hashlib.sha256(str(password_input).encode()).hexdigest()
        index = bank_db[0].index(str(self.num))
        if bank_db[1][index] == result:
            return True
        else:
            return False

    def see_balance(self, account_info):
        index = bank_db[0].index(str(self.num))
        return bank_db[2][index][account_info]

    def check_withdrawable(self, account_info, amount):
        index = bank_db[0].index(str(self.num))
        return bank_db[2][index][account_info] >= amount

    def withdraw(self, account_info, amount):
        index = bank_db[0].index(str(self.num))
        bank_db[2][index][account_info] -= amount

    def deposit(self, account_info, amount):
        index = bank_db[0].index(str(self.num))
        bank_db[2][index][account_info] += amount
