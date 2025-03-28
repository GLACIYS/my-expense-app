import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import (
    initialize_csv, 
    add_expense, 
    get_expenses, 
    visualize_category_expenses,
    visualize_subcategory_expenses,
    calculate_total_spent,
    generate_expense_report,
    CATEGORIES
)

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Initialize the CSV file if it doesn't exist
initialize_csv()

# App title
st.title("💰 Personal Expense Tracker")

# Create sidebar with navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a page:",
    ["Add Expense", "View Expenses", "Visualize Expenses", "Reports"]
)

# Add Expense Page
if page == "Add Expense":
    st.header("Add New Expense")
    
    with st.form("expense_form"):
        description = st.text_input("Description", placeholder="Enter expense description")
        
        col1, col2 = st.columns(2)
        
        with col1:
            category = st.selectbox("Category", list(CATEGORIES.keys()))
        
        with col2:
            subcategory = st.selectbox("Subcategory", CATEGORIES[category])
        
        amount = st.number_input("Amount", min_value=0.01, format="%0.2f")
        
        submitted = st.form_submit_button("Add Expense")
        
        if submitted:
            if description and amount > 0:
                if add_expense(description, category, subcategory, amount):
                    st.success("✅ Expense added successfully!")
                else:
                    st.error("Failed to add expense. Please try again.")
            else:
                st.warning("Please enter a description and a valid amount.")

# View Expenses Page
elif page == "View Expenses":
    st.header("View Your Expenses")
    
    expenses_df = get_expenses()
    
    if expenses_df.empty:
        st.warning("❌ No expenses found! Add some expenses to see them here.")
    else:
        # Total spent
        total = calculate_total_spent()
        st.subheader(f"💰 Total Spent: ${total:.2f}")
        
        # Filter options
        with st.expander("Filter Options"):
            # Category filter
            all_categories = sorted(expenses_df['Category'].unique())
            selected_categories = st.multiselect(
                "Filter by Categories",
                options=all_categories,
                default=all_categories
            )
            
            # Apply filters
            if selected_categories:
                filtered_df = expenses_df[expenses_df['Category'].isin(selected_categories)]
            else:
                filtered_df = expenses_df
        
        # Show data
        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Amount": st.column_config.NumberColumn(
                    "Amount",
                    format="$%.2f"
                )
            }
        )
        
        # Download option
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name="expenses_export.csv",
            mime="text/csv"
        )

# Visualize Expenses Page
elif page == "Visualize Expenses":
    st.header("Visualize Your Expenses")
    
    tab1, tab2 = st.tabs(["By Category", "By Subcategory"])
    
    with tab1:
        fig_category = visualize_category_expenses()
        if fig_category:
            st.pyplot(fig_category)
        else:
            st.warning("No data available for visualization.")
    
    with tab2:
        fig_subcategory = visualize_subcategory_expenses()
        if fig_subcategory:
            st.pyplot(fig_subcategory)
        else:
            st.warning("No data available for visualization.")

# Reports Page
else:  # Reports
    st.header("Expense Reports")
    
    # Calculate total spent
    total = calculate_total_spent()
    st.subheader(f"💰 Total Spent: ${total:.2f}")
    
    # Monthly report
    st.subheader("Monthly Expense Report")
    monthly_report = generate_expense_report()
    
    if monthly_report is not None and not monthly_report.empty:
        # Create a chart
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x="Month", y="Amount", data=monthly_report, ax=ax)
        plt.title("Monthly Expense Breakdown")
        plt.xticks(rotation=45)
        st.pyplot(fig)
        
        # Show the table
        st.dataframe(
            monthly_report,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Amount": st.column_config.NumberColumn(
                    "Amount",
                    format="$%.2f"
                )
            }
        )
    else:
        st.warning("No data available for the report.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Personal Expense Tracker v1.0")
