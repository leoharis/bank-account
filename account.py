class BankAccount:
    def __init__(self, sort_code, account_number, bank_name, first_name, last_name):
        self.sort_code = sort_code
        self.account_number = account_number
        self.bank_name = bank_name
        self.first_name = first_name
        self.last_name = last_name


bank_account1 = BankAccount("52-02-02", "250255251", "HSBC", "Barry", "Cassidy")

print(bank_account1.first_name + " " + bank_account1.last_name)
print(bank_account1.bank_name)
print(bank_account1.sort_code)
print(bank_account1.account_number)
