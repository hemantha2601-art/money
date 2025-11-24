import datetime

class MonthlyExpenseTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, trans_type, date=None):
        if trans_type not in ['income', 'expense']:
            raise ValueError("Transaction type must be 'income' or 'expense'")
        if date is None:
            date = datetime.date.today()
        self.transactions.append({
            'amount': amount,
            'category': category,
            'type': trans_type,
            'date': date
        })

    def monthly_summary(self, year, month):
        total_income = 0
        total_expense = 0
        category_expense = {}

        for t in self.transactions:
            if t['date'].year == year and t['date'].month == month:
                if t['type'] == 'income':
                    total_income += t['amount']
                else:
                    total_expense += t['amount']
                    category_expense[t['category']] = category_expense.get(t['category'], 0) + t['amount']

        print(f"Summary for {year}-{month:02d}:")
        print(f"Total Income: ${total_income}")
        print("Expenses by Category:")
        for cat, amt in category_expense.items():
            print(f"  {cat}: ${amt}")
        print(f"Total Expenses: ${total_expense}")
        print(f"Net Savings: ${total_income - total_expense}")

# Example Usage
tracker = MonthlyExpenseTracker()
tracker.add_transaction(5000, 'Salary', 'income', datetime.date(2025, 11, 1))
tracker.add_transaction(1200, 'Rent', 'expense', datetime.date(2025, 11, 2))
tracker.add_transaction(350, 'Groceries', 'expense', datetime.date(2025, 11, 10))
tracker.add_transaction(150, 'Transport', 'expense', datetime.date(2025, 11, 15))

tracker.monthly_summary(2025, 11)
