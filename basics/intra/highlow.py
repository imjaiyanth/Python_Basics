import pandas as pd

def find_open_low_high_same(csv_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Filter rows where 'Open' is equal to 'Low' or 'Open' is equal to 'High'
    result_df = df[(df['Open'] == df['Low']) | (df['Open'] == df['High'])]

    # Display the result
    print("Rows where 'Open' is equal to 'Low' or 'Open' is equal to 'High':")
    print(result_df)

# Replace 'your_csv_file.csv' with the actual path to your CSV file
csv_file_path = 'C://Users//suhi0//OneDrive//Desktop//Repo//python//Python_Basics//basics//intra//MW-NIFTY-50-08-Feb-2024.csv.csv'
find_open_low_high_same(csv_file_path)
