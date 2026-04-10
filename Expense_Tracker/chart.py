import csv
import matplotlib.pyplot as plt

file_name = "expense_data.csv"

def pie_chart():
    data = {}

    try:
        with open(file_name, "r") as f:
            r = csv.reader(f)
            for i in r:
                c = i[1]
                a = float(i[2])

                if c in data:
                    data[c] += a
                else:
                    data[c] = a
    except:
        print("No data")
        return

    if len(data) == 0:
        print("Nothing to show")
        return

    labels = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels=labels)
    plt.title("Expense chart")
    plt.show()