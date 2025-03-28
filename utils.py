import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import streamlit as st

# Constants
MAIN_FILE = "expenses.csv"

CATEGORIES = {
    "Food": ["Restaurants", "Snacks", "Cafes"],
    "Transport": ["Fuel", "Public Transport", "Cabs"],
    "Shopping": ["Accessories", "Clothes", "Electronics"],
    "Bills": ["Household", "Internet", "Product"],
    "Entertainment": ["Subscriptions", "Games", "Movies"],
    "Others": ["Gifts", "Donations", "Miscellaneous"],
}

# Initialize CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(MAIN_FILE):
        df = pd.DataFrame(columns=["Date", "Description", "Category", "Subcategory", "Amount"])
        df.to_csv(MAIN_FILE, index=False)

# Add a new expense to the CSV
def add_expense(description, category, subcategory, amount):
    date = datetime.now().strftime("%d/%m/%Y")
    
    try:
        # Read existing data
        df = pd.read_csv(MAIN_FILE)
        
        # Create new row
        new_row = pd.DataFrame({
            "Date": [date],
            "Description": [description],
            "Category": [category],
            "Subcategory": [subcategory],
            "Amount": [amount]
        })
        
        # Append new row
        df = pd.concat([df, new_row], ignore_index=True)
        
        # Save back to CSV
        df.to_csv(MAIN_FILE, index=False)
        return True
    except Exception as e:
        st.error(f"Error adding expense: {e}")
        return False

# Read expenses from CSV
def get_expenses():
    try:
        if os.path.exists(MAIN_FILE):
            df = pd.read_csv(MAIN_FILE)
            return df
        else:
            return pd.DataFrame(columns=["Date", "Description", "Category", "Subcategory", "Amount"])
    except Exception as e:
        st.error(f"Error reading expenses: {e}")
        return pd.DataFrame(columns=["Date", "Description", "Category", "Subcategory", "Amount"])

# Generate category visualization
def visualize_category_expenses():
    df = get_expenses()
    
    if df.empty:
        st.warning("No data to visualize!")
        return None
    
    # Clean column names
    df = df.rename(columns=lambda x: x.strip())
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="Category", y="Amount", data=df, estimator=sum, errorbar=None, ax=ax)
    plt.title("Expense Breakdown by Category")
    plt.xticks(rotation=45)
    
    return fig

# Generate subcategory visualization
def visualize_subcategory_expenses():
    df = get_expenses()
    
    if df.empty:
        st.warning("No data to visualize!")
        return None
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x="Subcategory", y="Amount", data=df, estimator=sum, errorbar=None, ax=ax)
    plt.title("Expense Breakdown by Subcategory")
    plt.xticks(rotation=45)
    
    return fig

# Calculate total spent
def calculate_total_spent():
    df = get_expenses()
    
    if df.empty:
        return 0
    
    return df["Amount"].sum()

# Generate expense report
def generate_expense_report():
    df = get_expenses()
    
    if df.empty:
        return None
    
    # Make sure Date is treated as string for string operations
    df['Date'] = df['Date'].astype(str)
    
    # For DD/MM/YYYY format, we'll extract MM/YYYY
    df['Month'] = df['Date'].apply(lambda x: '/'.join(x.split('/')[1:]) if '/' in x else x[:7])
    
    monthly_spent = df.groupby('Month')['Amount'].sum().reset_index()
    return monthly_spent
