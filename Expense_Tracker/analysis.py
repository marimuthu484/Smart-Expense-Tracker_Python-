import csv

file_name = "expense_data.csv"

def monthly_total():
    m = input("Enter month (YYYY-MM): ")
    total = 0

    try:
        with open(file_name, "r") as f:
            r = csv.reader(f)
            for i in r:
                if i[0].startswith(m):
                    total += float(i[2])
    except:
        pass

    print("Total:", total)


def highest_spending():
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
        pass

    if data:
        print("Highest:", max(data, key=data.get))
    else:
        print("No data")