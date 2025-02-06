import csv

def calculate_column_average(file_path, column_name):
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)  # Read the CSV file as a dictionary
            total = 0
            count = 0
            for row in reader:
                try:
                    value = float(row[column_name])  # Convert the column value to a float
                    total += value
                    count += 1
                except ValueError:
                    print(f"Skipping invalid value in row: {row}")
            if count == 0:
                return "No valid data found in the specified column."
            return total / count  # Calculate and return the average
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except KeyError:
        return f"Column '{column_name}' not found in the CSV file."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# File path to the CSV file
file_path = "data.csv"  # Replace with the path to your CSV file

# Column to calculate the average for
column_name = "Score"  # Replace with the column name you want to calculate the average for

# Calculate and display the average
average = calculate_column_average(file_path, column_name)
print(f"The average of the '{column_name}' column is: {average}")