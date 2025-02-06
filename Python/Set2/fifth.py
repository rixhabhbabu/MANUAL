import pandas as pd

def read_and_print_excel(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Print the data in a tabular format
        print("Data from the Excel file:")
        print(df.to_string(index=False))  # Use `to_string` for tabular formatting

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# File path to the Excel file
file_path = "random.xlsx"  # Replace with the path to your Excel file

# Read and print the Excel data
read_and_print_excel(file_path)