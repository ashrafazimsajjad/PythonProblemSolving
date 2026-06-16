import pandas as pd

# Create sample data
data = {
    "Name": ["Sajjad", "Rahim", "Karim"],
    "Age": [30, 35, 28],
    "City": ["Dhaka", "Khulna", "Chittagong"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel file
df.to_excel("output.xlsx", index=False)

print("Data successfully written to Excel file!")