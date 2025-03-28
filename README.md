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
   - Set the main file path to: `deployment_app.py` (special file for Streamlit Cloud)
   - For requirements, use any of these options:
     - Enter these manually: `streamlit>=1.22.0,pandas>=1.5.3,matplotlib>=3.7.1,seaborn>=0.12.2`
     - Or use the existing `streamlit_requirements.txt` file
4. **Deploy**: Click the deploy button

### Troubleshooting Deployment

If you encounter a `connection refused` error during deployment:
- Verify you're using `deployment_app.py` as the main file
- Check that your `.streamlit/config.toml` file doesn't specify a custom port

### Port Configuration

- **Locally**: This application runs on port 5000 on Replit
- **Streamlit Cloud**: The application must use the default port (8501)
- The `deployment_app.py` file is configured to work correctly on Streamlit Cloud

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