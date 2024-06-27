import os
from datetime import datetime
from typing import List
from src.record import Record


class Wallet:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.records: List[Record] = self.load_records()

    def load_records(self) -> List[Record]:
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            content = file.read().strip().split('\n\n')
            records = []
            for entry in content:
                lines = entry.split('\n')
                date = lines[0].split(': ')[1]
                category = lines[1].split(': ')[1]
                amount = float(lines[2].split(': ')[1])
                description = lines[3].split(': ')[1]
                records.append(Record(date, category, amount, description))
            return records

    def save_records(self):
        with open(self.file_path, 'w') as file:
            for record in self.records:
                file.write(str(record) + '\n')

    def add_record(self, record: Record):
        self.records.append(record)
        self.save_records()

    def edit_record(self, index: int, new_record: Record):
        if 0 <= index < len(self.records):
            self.records[index] = new_record
            self.save_records()

    def search_records(self, **kwargs):
        results = self.records
        if 'category' in kwargs:
            results = [r for r in results if r.category == kwargs['category']]
        if 'date' in kwargs:
            search_date = datetime.strptime(kwargs['date'], '%Y-%m-%d')
            results = [r for r in results if r.date == search_date]
        if 'amount' in kwargs:
            results = [r for r in results if r.amount == kwargs['amount']]
        return results

    def get_balance(self):
        income = sum(r.amount for r in self.records if r.category == 'Income')
        expenses = sum(r.amount for r in self.records if r.category == 'Expense')
        return income, expenses, income - expenses
