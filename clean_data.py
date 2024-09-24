import pandas as pd
merged_df = pd.read_csv('merged_data.csv')

def clean_merged_df(merged_df):
   #compute delta of open and close
   #sort dates in descending manner 
   merged_df['Delta % Close - Open'] = ((merged_df['Close'].astype(float) - merged_df['Open'].astype(float))/merged_df['Open'].astype(float))*100
   merged_df['Delta % High - Low'] = ((merged_df['High'].astype(float) - merged_df['Low'].astype(float))/ merged_df['Low'].astype(float))*100
   #use fillna to replace null values with 0 if the company wasn't granted any contract on that day
   merged_df['Award Amount'] = merged_df['Award Amount'].fillna(0)
   #use fillna to fill in the company name for non-overlapping rows between pltr_stock_price.csv and contracts_data.csv
   merged_df['Company Name'] = merged_df['Company Name'].fillna('PALANTIR TECHNOLOGIES INC.')
   sorted_merged_df = merged_df.sort_values(by='Date', ascending=False)
   sorted_merged_df.to_csv('final_output.csv', index=False)


clean_merged_df(merged_df)