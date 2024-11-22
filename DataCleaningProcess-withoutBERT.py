import pandas as pd
import numpy as np

# Load the data
incidents_df = pd.read_csv('path/to/incidents_table.csv')
categories_df = pd.read_csv('path/to/categories_table.csv')
user_queries_df = pd.read_csv('path/to/user_queries_table.csv')
users_df = pd.read_csv('path/to/users_table.csv')

# --- Data Cleaning Functions ---

# Function to clean text fields by removing whitespace, special characters, and converting to lowercase
def clean_text(text):
    if isinstance(text, str):
        text = text.strip().lower()
        text = ''.join(e for e in text if e.isalnum() or e.isspace())  # remove special characters
    return text

# Convert date columns to datetime format and handle missing values
def convert_to_datetime(df, column):
    df[column] = pd.to_datetime(df[column], errors='coerce')
    return df

# --- 1. Clean Incidents Table ---
# Convert date columns
incidents_df = convert_to_datetime(incidents_df, 'created_at')
incidents_df = convert_to_datetime(incidents_df, 'updated_at')

# Handle missing updated_at dates (e.g., fill with created_at or mark as NaT)
incidents_df['updated_at'].fillna(incidents_df['created_at'], inplace=True)

# Standardize severity column (e.g., lowercase or capitalize)
incidents_df['severity'] = incidents_df['severity'].str.capitalize()

# Clean text fields
text_columns = ['Incident_Description', 'Root_Cause', 'Resolution', 'Solution']
for col in text_columns:
    incidents_df[col] = incidents_df[col].apply(clean_text)

# --- 2. Clean Categories Table ---
# Ensure unique combinations of category and subcategory
categories_df.drop_duplicates(subset=['category_Id', 'subcategory_Id'], inplace=True)

# Clean text fields
categories_df['category_name'] = categories_df['category_name'].apply(clean_text)
categories_df['subcategory_name'] = categories_df['subcategory_name'].apply(clean_text)

# --- 3. Clean User Queries Table ---
# Clean query field
user_queries_df['query'] = user_queries_df['query'].apply(clean_text)

# --- 4. Clean Users Table ---
# Convert date columns to datetime
users_df = convert_to_datetime(users_df, 'created_at')
users_df = convert_to_datetime(users_df, 'last_login')

# Standardize role and department columns
users_df['role'] = users_df['role'].str.capitalize()
users_df['department'] = users_df['department'].apply(clean_text)

# --- Consistency Checks ---
# Ensure user IDs in incidents and queries tables exist in users table
missing_user_ids_incidents = incidents_df[~incidents_df['user_id'].isin(users_df['Id'])]
missing_user_ids_queries = user_queries_df[~user_queries_df['user_id'].isin(users_df['Id'])]

if not missing_user_ids_incidents.empty:
    print("Warning: Some user IDs in incidents table are missing from users table.")

if not missing_user_ids_queries.empty:
    print("Warning: Some user IDs in user queries table are missing from users table.")

# Output cleaned data
incidents_df.to_csv('cleaned_incidents_table.csv', index=False)
categories_df.to_csv('cleaned_categories_table.csv', index=False)
user_queries_df.to_csv('cleaned_user_queries_table.csv', index=False)
users_df.to_csv('cleaned_users_table.csv', index=False)

print("Data cleaning completed and saved to CSV files.")