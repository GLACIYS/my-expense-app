# Personal Expense Tracker

A modern Streamlit-powered personal expense tracker that offers comprehensive financial monitoring and visualization.

## Features

- **Expense Tracking**: Easy input of expenses with categories and subcategories
- **Data Visualization**: Charts and graphs for expense analysis by category and subcategory
- **Monthly Reports**: View spending patterns over time with monthly breakdowns
- **Data Management**: Export and import your expense data for safe backup
- **Responsive Interface**: User-friendly design that works on desktop and mobile

## Technology Stack

- **Python 3.11**
- **Streamlit**: For the interactive web interface
- **Pandas**: For data manipulation and analysis
- **Matplotlib & Seaborn**: For data visualization
- **CSV Storage**: Simple file-based database

## Deployment to Streamlit Cloud

This application is configured for easy deployment to Streamlit Cloud. Follow these steps:

1. **Go to Streamlit Cloud**: Visit [streamlit.io/cloud](https://streamlit.io/cloud)
2. **Sign in with GitHub**: Connect your GitHub account
3. **Create a New App**:
   - Select the 'my-expense-app' repository
   - Set the main file path to: `app.py`
   - Rename `streamlit_requirements.txt` to `requirements.txt` or enter the requirements manually
4. **Deploy**: Click the deploy button

### Data Persistence in Cloud

When deploying to Streamlit Cloud, be aware that data might not persist between sessions. Use the **Backup & Restore** feature to:
- Download a backup of your expense data regularly
- Upload your data when needed to restore your expense history

## Local Development

To run this application locally:

```bash
streamlit run app.py
```

## License

Open source under MIT license.