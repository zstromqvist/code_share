# Transform the 'date_of_birth' column to a date variable
date_var = pd.to_datetime(df['date_of_birth'])

# Use the date variable to filter the DataFrame
filtered_df = df[date_var < '1990-01-01']

# Create a specific date
my_date = pd.Timestamp('1990-01-01')

# Use the date to filter the DataFrame
filtered_df = df[date_var < my_date]


date_string = "2023-04-25"
date = datetime.strptime(date_string, "%Y-%m-%d").date()

print(date)  # Output: 2023-04-25