# Transform the 'date_of_birth' column to a date variable
date_var = pd.to_datetime(df['date_of_birth'])

# Use the date variable to filter the DataFrame
filtered_df = df[date_var < '1990-01-01']