#import libraries
from pathlib import Path
import csv
from datetime import datetime as dt

#abspath to resource data
data_folder_in = Path("/01_Data_Analytics/Git_Clones/UTAUS201807DATA2/\
homework-instructions/03-Python-Instructions/Instructions/PyBank/Resources/")
file_to_open = data_folder_in / "budget_data.csv"

#read in data to a list
data_list = []
with open(file_to_open, 'r', newline='') as f_o:
    reader = csv.reader(f_o)
    csv_header = next(f_o) #remove header row
    for row in reader:
        data_list.append(row)

#initialize variables
tot_months = len(data_list)
tot_income = int(data_list[0][1])
tot_change = 0

#initialize lists
g_inc = int(data_list[0][1])
g_dec = int(data_list[0][1])

#loop through each item in the list
for i in range(1,len(data_list)):
        tot_income += int(data_list[i][1]) #accrete total income
        tot_change += int(data_list[i][1]) - int(data_list[i-1][1]) #accrete change in income

        #evaluate for max change in income
        if int(data_list[i][1]) - int(data_list[i-1][1]) > g_inc:
            g_inc = int(data_list[i][1]) - int(data_list[i-1][1]) #delta between current row and previous
            g_inc_m = dt.strptime(data_list[i][0], '%b-%y').strftime('%b-%Y') #corresponding month converted to 'Mon-YYYY' format

        #evaluate for min change in income
        elif int(data_list[i][1]) - int(data_list[i-1][1]) < g_dec:
            g_dec = int(data_list[i][1]) - int(data_list[i-1][1]) #delata between current row and previous
            g_dec_m = dt.strptime(data_list[i][0], '%b-%y').strftime('%b-%Y') #corresponding month converted to 'Mon-YYYY' format

avg_change = tot_change / (tot_months-1) #average change

#store output in a sequence of variables
line1 = ("Financial Analysis\n")
line2 = ("---------------------------------------\n")
line3 = ("Total Months: " + str(tot_months) + "\n")
line4 = ("Total: " + str('${:,.2f}'.format(tot_income)) + "\n") #format for currency
line5 = ("Average Change: " + str('${:,.2f}'.format(avg_change)) + "\n") #format for currency
line6 = ("Greatest Increase in Profits: " + str(g_inc_m) + " " + \
str('${:,.2f}'.format(g_inc)) + "\n") #format for currency
line7 = ("Greatest Decrease in Profits: " + str(g_dec_m) + " " + \
str('${:,.2f}'.format(g_dec)) + "\n") #format for currency

#print results to screen
print(line1, line2, line3, line4, line5, line6, line7, sep='')

#write results to file
data_folder_out = Path("/01_Data_Analytics/Git_Clones/03_Python/PyBank/")
file_to_write = data_folder_out / "BankPy.txt"
f_c = open(file_to_write, 'w')
f_c.writelines([line1, line2, line3, line4, line5, line6, line7])
f_c.close()
