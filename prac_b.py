import pandas as pd

data1 = {'Name': ['John', 'Alice', 'Bob'],
         'Mobile': ['+919123456789', '+17916a89012345', '918901234567']}

df = pd.DataFrame(data1)

def clean_mobile_number(mobile):
    # Remove non-digit characters
    mobile = ''.join(filter(str.isdigit, str(mobile)))

    # Check conditions and apply slicing
    if mobile.startswith('+91'):
        mobile = mobile[3:]
    elif mobile.startswith('+17'):
        mobile = mobile[3:]
    elif mobile.startswith('91') and len(mobile) == 12:
        mobile = mobile[2:]

    # Check length and starting digit
    if len(mobile) == 10 and mobile[0] in ['6', '7', '8', '9']:
        return mobile
    else:
        return None  # Return None for invalid numbers


# Apply the cleaning function to the 'Mobile' column
df['Mobile'] = df['Mobile'].apply(clean_mobile_number)

# Drop rows with invalid mobile numbers (None values)
df = df.dropna()

# Display the cleaned DataFrame
print(df)


