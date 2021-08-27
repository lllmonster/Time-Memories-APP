import dailyPie
import pandas as pd

df = pd.read_excel('Time 2021.xlsx', header=None)

#print(df)
col = 4
daily_data = df.iloc[2:43, col]
daily_week = df.iloc[0,col]
daily_date = df.iloc[1,col]

dailyPie.draw(daily_data, daily_date, daily_week)