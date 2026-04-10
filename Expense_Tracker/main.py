from data_handler import add_expense, view_all, create_file
from analysis import monthly_total, highest_spending
from chart import pie_chart

def menu():
    create_file()

    while True:
        print("\n1. Add New Expense")
        print("2. View All Expenses")
        print("3. Show Monthly Summary")
        print("4. Check Highest Spending Category")
        print("5. Display Expense Chart")
        print("6. Exit Program")

        ch = input("Choice: ")

        if ch == '1':
            add_expense()
        elif ch == '2':
            view_all()
        elif ch == '3':
            monthly_total()
        elif ch == '4':
            highest_spending()
        elif ch == '5':
            pie_chart()
        elif ch == '6':
            break
        else:
            print("Wrong choice")

menu()