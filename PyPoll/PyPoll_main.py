from pathlib import Path
import csv

data_folder_in = (Path("/01_Data_Analytics/Git_Clones/UTAUS201807DATA2/\
homework-instructions/03-Python-Instructions/Instructions/PyPoll/Resources/"))
file_to_open = data_folder_in / "election_data.csv"

data_list = []
with open(file_to_open, 'r', newline='') as f_o:
    reader = csv.reader(f_o)
    csv_header = next(f_o)
    for row in reader:
        data_list.append(row)

cand_list = []
cand_tot = []
cand_per = []
line_list = []

for data in data_list:
    if data[2] not in cand_list:
        cand_list.append(data[2])
        cand_tot.append(1)
    else:
        cand_tot[cand_list.index(data[2])] += 1

total_votes = sum(cand_tot)
winner = cand_list[cand_tot.index(max(cand_tot))]

line_list.append("Election Results\n")
line_list.append("-----------------------------\n")
line_list.append("Total Votes: " + str(total_votes) + "\n")
line_list.append("-----------------------------" + "\n")
for i in range(4, len(cand_list)+4):
    line_list.append(cand_list[i-4] + ": " + str(format(cand_tot[i-4]/total_votes,\
    '.3%')) + " (" + str(cand_tot[i-4]) + ")\n")
line_list.append("-----------------------------\n")
line_list.append("Winner: " + winner + "\n")
line_list.append("-----------------------------\n")

print(*line_list, sep = '')

data_folder_out = Path("/01_Data_Analytics/Git_Clones/03_Python/PyPoll/")
file_to_write = data_folder_out / "Pollpy.txt"
f_c = open(file_to_write, 'w')
f_c.writelines(line_list)
f_c.close()
