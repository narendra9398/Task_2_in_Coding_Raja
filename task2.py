import json

# Initialize data structures
income = 0
expenses = []
categories = {}

# Load data from a file (if available)
try:
    with open('budget_data.json', 'r') as file:
        data = json.load(file)
        income = data.get('income', 0)
        expenses = data.get('expenses', [])
        categories = data.get('categories', {})
except FileNotFoundError:
    pass

def add_income():
    global income
    amount = float(input("Enter income amount: "))
    income += amount
    print(f"Income added: ${amount}")

def add_expense():
    global income
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    
    if category not in categories:
        categories[category] = 0
    
    if amount > income:
        print("Warning: Expense exceeds available income!")
    
    income -= amount
    categories[category] += amount
    expenses.append({"category": category, "amount": amount})
    print(f"Expense added: ${amount} in category '{category}'")

def calculate_budget():
    total_expenses = sum(expense["amount"] for expense in expenses)
    remaining_budget = income - total_expenses
    print(f"Remaining budget: ${remaining_budget}")

def analyze_expenses():
    print("Expense Analysis:")
    for category, amount in categories.items():
        print(f"{category}: ${amount}")

while True:
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Budget")
    print("4. Analyze Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        calculate_budget()
    elif choice == "4":
        analyze_expenses()
    elif choice == "5":
        # Save data to a file before exiting
        with open('budget_data.json', 'w') as file:
            json.dump({'income': income, 'expenses': expenses, 'categories': categories}, file)
        break
    else:
        print("Invalid choice. Please choose a valid option.")
