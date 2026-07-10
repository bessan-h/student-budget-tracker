import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

monthbudget = 0
monthexpenses = 0
food=0
rent=0
entertainment=0
books=0
monthexpenses=food + rent + entertainment + books
if monthexpenses > 0:
    df = pd.DataFrame(data=[food, rent, entertainment, books], index=["Food", "Rent", "Entertainment", "Books"], columns=["Amount"])
    expensepiechart = df.plot.pie(y='Amount', autopct='%1.1f%%', legend=False, title="Expenses Breakdown").get_figure()

def cycle():
    global monthbudget, monthexpenses, food, rent, entertainment, books, expensepiechart
    monthexpenses = food + rent + entertainment + books
    if monthexpenses > 0:
        df = pd.DataFrame(data=[food, rent, entertainment, books], index=["Food", "Rent", "Entertainment", "Books"], columns=["Amount"])
        expensepiechart = df.plot.pie(y='Amount', autopct='%1.1f%%', legend=False, title="Expenses Breakdown").get_figure()
def savetransactiontocsv(amount, category):
    global monthbudget, monthexpenses, food, rent, entertainment, books
    data = {
        "Category": [category],
        "Amount": [amount],
        "Timestamp": [dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    }
    df = pd.DataFrame(data)
    df.to_csv("budget_data.csv",mode='a', index=False, header=False)
def clearbudgetdata():
    global monthbudget, monthexpenses, food, rent, entertainment, books
    monthbudget = 0
    monthexpenses = 0
    food = 0
    rent = 0
    entertainment = 0
    books = 0
    # Clear the CSV file content
    with open("budget_data.csv", "w") as f:
        f.write("Category,Amount,Timestamp\n")
def loadbudgetdata():
    global monthbudget, monthexpenses, food, rent, entertainment, books
    try:
        df = pd.read_csv("budget_data.csv")
        monthbudget = df[df['Category'] == 'Income']['Amount'].sum()
        food = df[df['Category'] == 'Food']['Amount'].sum()
        rent = df[df['Category'] == 'Rent']['Amount'].sum()
        entertainment = df[df['Category'] == 'Entertainment']['Amount'].sum()
        books = df[df['Category'] == 'Books']['Amount'].sum()
        monthexpenses = food + rent + entertainment + books
    except FileNotFoundError:
        # If the file doesn't exist, initialize it with headers
        with open("budget_data.csv", "w") as f:
            f.write("Category,Amount,Timestamp\n")

