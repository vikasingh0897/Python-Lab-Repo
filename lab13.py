class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float = 0.0):
        self._account_number = account_number
        self._name = name
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ₹{amount:.2f}")

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: ₹{amount:.2f}")
            return True
        else:
            print("Insufficient balance.")
            return False

    def get_balance(self) -> float:
        return self._balance

    def display(self) -> None:
        print(f"Account: {self._account_number}")
        print(f"Name   : {self._name}")
        print(f"Balance: ₹{self._balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, name: str, balance: float = 0.0, interest_rate: float = 0.04):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> bool:
        print("Savings Account Withdrawal:")
        return super().withdraw(amount)

    def add_interest(self) -> None:
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest added (4%): ₹{interest:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number: str, name: str, balance: float = 0.0, overdraft: float = 5000.0):
        super().__init__(account_number, name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount: float) -> bool:
        print("Current Account Withdrawal:")
        if amount <= self._balance + self.overdraft:
            self._balance -= amount
            print(f"Withdrawn: ₹{amount:.2f}")
            if self._balance < 0:
                print(f"Overdraft facility used: ₹{abs(self._balance):.2f}")
            return True
        else:
            print("Overdraft limit exceeded.")
            return False


def main():
    sa = SavingsAccount("SA101", "Rahul", 10000.0)
    ca = CurrentAccount("CA201", "Amit", 5000.0, overdraft=5000.0)

    accounts = [sa, ca]
    for acc in accounts:
        acc.display()
        acc.deposit(1000)
        acc.withdraw(3000)
        print(f"Current Balance: ₹{acc.get_balance():.2f}\n")

    print("--- Testing Overdraft Protection ---")
    ca.withdraw(6000)
    print(f"Current Account Balance: ₹{ca.get_balance():.2f}")


if __name__ == "__main__":
    main()
