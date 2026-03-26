import pandas as pd

def load_and_process_data(file_path):
    
    # Load dataset
    df = pd.read_csv(file_path)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Standardize text values (convert to lowercase)
    df['cloud_provider'] = df['cloud_provider'].str.lower()
    df['resource_type'] = df['resource_type'].str.lower()
    df['public_access'] = df['public_access'].str.lower()
    df['encryption_enabled'] = df['encryption_enabled'].str.lower()
    df['iam_privilege'] = df['iam_privilege'].str.lower()

    # Handle missing values
    df.fillna({
        'cpu_utilization': 0,
        'monthly_cost': 0
    }, inplace=True)

    # Convert numeric columns
    df['cpu_utilization'] = pd.to_numeric(df['cpu_utilization'], errors='coerce')
    df['monthly_cost'] = pd.to_numeric(df['monthly_cost'], errors='coerce')

    return df