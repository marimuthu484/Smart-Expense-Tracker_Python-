import csv

file_name = "expense_data.csv"

def create_file():
    try:
        open(file_name, "x").close()
    except:
        pass


def add_expense():
    d = input("Enter date (YYYY-MM-DD): ")
    c = input("Enter category: ")
    a = float(input("Enter amount: "))
    desc = input("Enter note: ")

    with open(file_name, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([d, c, a, desc])

    print("Saved")


def view_all():
    try:
        with open(file_name, "r") as f:
            r = csv.reader(f)
            print("\nData:")
            for i in r:
                print(i)
    except:
        print("No data found")