import dailyPie
import pandas as pd
import sys
import getopt

df = pd.read_excel('Time 2021.xlsx', header=None)

def draw_daily_pie(input_date):
    print(f"Daily-Pie-{input_date}")
    col = 0
    date_list = df.iloc[1]

    for i, date in enumerate(date_list):
        if date == input_date:
            col = i
            break

    print(f"Date is {input_date} in col {col}")
    daily_data = df.iloc[2:43, col]
    daily_week = df.iloc[0, col]
    daily_date = df.iloc[1, col]

    dailyPie.draw(daily_data, daily_date, daily_week)

def draw_monthly_pie(month):
    print("TODO-Monthly-Pie")

def dray_getup_chart(getup):
    print("TODO-Getup-TimeLine")

def read_my_excel(day, month, getup):
    if (day != ''):
        draw_daily_pie(day)
    if (month != ''):
        draw_monthly_pie(month)
    if (getup != ''):
        dray_getup_chart(getup)

def main(argv):
    day = ''
    month = ''
    getup = ''
    try:
        opts, args = getopt.getopt(argv, "hd:m:g:")
    except getopt.GetoptError:
        print('Wrong Input. Run -h to check help')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('-d Date of Daily Pie')
            print('-m Month of Month Pie')
            print('-g Get up and Sleep time line')
            sys.exit()
        elif opt in ("-d"):
            day = arg
        elif opt in ("-m"):
            month = arg
        elif opt in ("-g"):
            getup = arg
    
    read_my_excel(day, month, getup)

if __name__ == "__main__":
    main(sys.argv[1:])

# print(df)
