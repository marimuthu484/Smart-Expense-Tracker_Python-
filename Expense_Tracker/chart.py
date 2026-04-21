import csv
import matplotlib.pyplot as plt

file_name = "expense_data.csv"

def pie_chart():
    data = {}
    try:
        with open(file_name, "r") as f:
            r = csv.reader(f)

            for row in r:
                if len(row) < 3:
                    continue

                category = row[1]
                amount = float(row[2])

                data[category] = data.get(category, 0) + amount

    except FileNotFoundError:
        print("File not found")
        return
    except:
        print("Error reading data")
        return

    if not data:
        print("No data")
        return

    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    labels = [x[0] for x in sorted_data]
    values = [x[1] for x in sorted_data]
    total = sum(values)
    def format_label(pct):
        value = pct * total / 100
        return f"{pct:.1f}%\n₹{value:.0f}"

    fig, (ax1, ax2) = plt.subplots(
        1, 2,
        figsize=(12, 6),
        gridspec_kw={'width_ratios': [2, 1]}
    )

    explode = [0.05 if i == 0 else 0 for i in range(len(values))]  # highlight top

    wedges, texts, autotexts = ax1.pie(
        values,
        labels=labels,
        autopct=format_label,
        startangle=90,
        explode=explode,
        wedgeprops=dict(edgecolor="black")
    )

    ax1.set_title("Expense Distribution", fontsize=14)
    ax1.axis("equal")

    table_data = []
    for i, (cat, val) in enumerate(sorted_data, start=1):
        percent = (val / total) * 100
        table_data.append([
            i,
            cat,
            f"₹{val:.0f}",
            f"{percent:.1f}%"
        ])

    col_labels = ["#", "Category", "Amount", "%"]

    ax2.axis("off")
    table = ax2.table(
        cellText=table_data,
        colLabels=col_labels,
        loc="center",
        cellLoc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    ax2.set_title("Summary (High → Low)", fontsize=12)

    for (row, col), cell in table.get_celld().items():
        if row == 1: 
            cell.set_facecolor("#e6f2ff")

    plt.tight_layout()
    plt.show()
