import pandas as pd

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
    df = pd.DataFrame(data=[food, rent, entertainment, books], index=["Food", "Rent", "Entertainment", "Books"], columns=["Amount"])
    expensepiechart = df.plot.pie(y='Amount', autopct='%1.1f%%', legend=False, title="Expenses Breakdown").get_figure()

