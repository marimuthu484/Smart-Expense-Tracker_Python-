# Smart Expense Tracker with Insights

## Overview

**Smart Expense Tracker** is a Python-based personal finance management application designed to help individuals track daily expenses, understand spending patterns, and make informed financial decisions. The application provides visual insights through charts and analytical summaries to identify areas for potential savings.

## Features

### Core Functionality
- Expense Recording
  - Log daily expenses with date, category, amount, and note
  - Quick and easy data entry interface
  - Persistent storage using CSV format

-  Data Analysis
  - Monthly expense totals
  - Identify highest spending category
  - View all recorded expenses

- Visual Insights
  - Pie charts showing category-wise expense distribution
  - Percentage breakdown of spending

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **CSV Module** | Data storage and retrieval |
| **Matplotlib** | Data visualization and charts |

## Project Structure

```
python/
│   main.py              # Main menu and program control
│   data_handler.py      # File operations and data management
│   analysis.py          # Expense analysis calculations
│   chart.py            # Pie chart visualization
│   expense_data.csv    # Data storage file
│
├───output/             # Chart output images
│       image.png
│       image copy.png
│
└───__pycache__/        # Python cache files
        analysis.cpython-313.pyc
        chart.cpython-313.pyc
        data_handler.cpython-313.pyc
```

### Module Descriptions

#### **main.py**
- Contains the main menu interface
- Controls program flow
- Calls functions from other modules

#### **data_handler.py**
- Creates and manages CSV file
- Handles adding new expenses
- Displays all expense data

#### **analysis.py**
- Calculates monthly totals
- Identifies highest spending category

#### **chart.py**
- Generates pie chart visualization
- Shows category-wise expense distribution

## Installation

### Prerequisites
- Python 3.x
- matplotlib library

### Setup Instructions

1. **Install required dependency**
```bash
pip install matplotlib
```

2. **Run the application**
```bash
python main.py
```


### Getting Started

1. **Launch the Application**
   ```bash
   python main.py
   ```

2. **Main Menu Options**
   ```
   1 Add
   2 View
   3 Monthly
   4 Highest
   5 Chart
   6 Exit
   
   Choice: 
   ```

3. **Adding an Expense**
   ```
   Enter date (YYYY-MM-DD): 2026-08-27
   Enter category: Food
   Enter amount: 1000
   Enter note: Lunch at Hostel
   Saved
   ```

4. **Viewing Monthly Total**
   ```
   Enter month (YYYY-MM): 2024-08
   Total expense: 1800.0
   ```

5. **Checking Highest Spending Category**
   ```
   Highest category: Shopping
   ```


## Sample Data

### expense_data.csv
```csv
2026-8-27,Food,1000.0,Lunch at hotel
2026-08-05,Transport,300.0,Bus ticket price
2025-08-12,Shopping,2000.0,Bought clothes
2026-08-18,Bills,800.0,Electricity bill
2026-08-24,Entertainment,700.0,Movie

```

## How It Works

1. **File Creation**: Automatically creates `expense_data.csv` if it doesn't exist
2. **Data Entry**: Users input expense details (date, category, amount, note)
3. **Storage**: All data is appended to CSV file
4. **Analysis**: 
   - Monthly total calculates sum for specified month
   - Highest spending identifies category with maximum expenses
5. **Visualization**: Pie chart displays category-wise percentage distribution



## Expected Outcomes

- Clear understanding of spending patterns
- Ability to track expenses over time
- Visual insights through pie charts
- Identification of high-spending categories
