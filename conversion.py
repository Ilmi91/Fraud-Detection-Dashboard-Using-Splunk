import pandas as pd

# Load the Excel file
excel_file = "prepared_data.xlsx"

# Read the first sheet
df = pd.read_excel(excel_file)

# Save it as a CSV file
df.to_csv("prepared_data.csv", index=False)
