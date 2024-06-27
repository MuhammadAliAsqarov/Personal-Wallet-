from datetime import datetime


class Record:
    def __init__(self, date: str, category: str, amount: float, description: str):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"Date: {self.date.strftime('%Y-%m-%d')}\nCategory: {self.category}\nAmount: {self.amount}\nDescription: {self.description}\n"
