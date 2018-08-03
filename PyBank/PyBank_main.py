from pathlib import Path
import csv

data_folder_in = (Path("/01_Data_Analytics/Git_Clones/UTAUS201807DATA2/\
homework-instructions/03-Python-Instructions/Instructions/PyBank/Resources/"))
file_to_open = data_folder_in / "budget_data.csv"

data_list = []
with open(file_to_open, 'r', newline='') as f_o:
    reader = csv.reader(f_o)
    for row in reader:
        data_list.append(row)

tot_months = len(data_list)-1
tot_income = int(data_list[1][1])
tot_change = 0

g_inc = int(data_list[1][1])
g_dec = int(data_list[1][1])

for i in range(2,len(data_list)):
        tot_income += int(data_list[i][1])
        tot_change += int(data_list[i][1]) - int(data_list[i-1][1])

        if int(data_list[i][1]) - int(data_list[i-1][1]) > g_inc:
            g_inc = int(data_list[i][1]) - int(data_list[i-1][1])
            g_inc_m = data_list[i][0]

        elif int(data_list[i][1]) - int(data_list[i-1][1]) < g_dec:
            g_dec = int(data_list[i][1]) - int(data_list[i-1][1])
            g_dec_m = data_list[i][0]

avg_change = tot_change / (tot_months - 1)

print(tot_change)

line1 = ("Financial Analysis\n")
line2 = ("---------------------------------------\n")
line3 = ("Total Months: " + str(tot_months) + "\n")
line4 = ("Total: " + str('${:,.2f}'.format(tot_income)) + "\n")
line5 = ("Average Change: " + str('${:,.2f}'.format(avg_change)) + "\n")
line6 = ("Greatest Increase in Profits: " + str(g_inc_m) + " " + \
str('${:,.2f}'.format(g_inc)) + "\n")
line7 = ("Greatest Decrease in Profits: " + str(g_dec_m) + " " + \
str('${:,.2f}'.format(g_dec)) + "\n")

print(line1, line2, line3, line4, line5, line6, line7, sep='')

data_folder_out = Path("/01_Data_Analytics/Git_Clones/python-challenge/PyBank/")
file_to_write = data_folder_out / "BankPy.txt"
f_c = open(file_to_write, 'w')
f_c.writelines([line1, line2, line3, line4, line5, line6, line7])
f_c.close()
