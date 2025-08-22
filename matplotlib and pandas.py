import pandas as pd

RBA_data= pd.read_excel(r'C:\Users\Danilo\Downloads\f01hist.xlsx')
print(RBA_data.head(10))

#pandas import from excel file

import pandas as pd

RBA_data = pd.read_excel(r'C:\Users\Danilo\Downloads\f01hist.xlsx')

#print(RBA_data.columns)  # Check column names

filtered = RBA_data[RBA_data['F1.1 INTEREST RATES AND YIELDS – MONEY MARKET'].astype(str).str.contains('2002|2003', case=False, na=False)]

print(filtered)

#pandas import from  column in and it contains some values

import pandas as pd

RBA_data = pd.read_excel(r'C:\Users\Danilo\Downloads\f01hist.xlsx')

# Convert the date column to datetime
RBA_data['F1.1 INTEREST RATES AND YIELDS – MONEY MARKET'] = pd.to_datetime(
    RBA_data['F1.1 INTEREST RATES AND YIELDS – MONEY MARKET'], errors='coerce'
)

# Filter from October 2002 to June 2003 (inclusive)
start = pd.Timestamp('2002-10-01')
end = pd.Timestamp('2003-06-30')
filtered = RBA_data[
    (RBA_data['F1.1 INTEREST RATES AND YIELDS – MONEY MARKET'] >= start) &
    (RBA_data['F1.1 INTEREST RATES AND YIELDS – MONEY MARKET'] <= end)
]

#select only the first two columns for output and copy them
output = filtered.iloc[:, :2].copy()
output.columns = ['Month', 'Value']  # Change to your desired names

print(output)

import matplotlib.pyplot as plt

#size of the plot
plt.figure(figsize=(10,5))
#axis values
plt.plot(output['Month'], output['Value'], marker='o')
#axis names
plt.xlabel('Month')
plt.ylabel('Value')
#title of the plot
plt.title('Values from October 2002 to June 2003')
#rotate x axis values for better visibility
plt.xticks(rotation=45)
#adjust layout to prevent clipping of tick-labels
plt.tight_layout()
plt.show()

#import data from excel, filter by date and plot the results