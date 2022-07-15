import excelrd
from pyfaidx import Fasta
import sys
sys.stdout = open('Upregulated_edited', 'w')
workbook = excelrd.open_workbook("Sig_up.xlsx")
sh = workbook.sheet_by_index(0)
row_num = sh.nrows
col_num = sh.ncols
list_of_excel = []
# Workbook is opened and the first sheet is accessed. The number of rows and columns is calculated.
for i in range(1, row_num):
    Seq_excel = sh.cell_value(i, 0)
    list_of_excel.append(Seq_excel)
    i += 1
sequences = Fasta("IDS_UP.fasta")
long_seq = []
long_seq = list(sequences.keys()) # the keys have the entire descriptor (header of the FASTA sequences)

list_of_ID = []

for key in sequences.keys():
    U_ID = key.split('|')  # splitting the ID because pyfaidx retrieves IDs long format
    seq = U_ID[1]
    list_of_ID.append(seq)
final_pos = []
for id in list_of_ID:  # ID in unique list, since there are many IDs that are repeating
    i = 0
    pos = []
    for j in list_of_excel:  # ID in complete list from the excel file given.
        i += 1
        if id == j:
            value = sh.cell_value(i, 1)
            value = int(value)
            pos.append(value)
    for i in range(len(pos)):
                pos[i] = int(pos[i])
    final_pos.append(pos)
count = 0
for j in final_pos:
    for k in j:
        if k <= 7:
            a = sequences.get_seq(long_seq[count], 1, k+7)
            a = str(a)
            ex = 15-len(a)
            b = ex * "X"
            b += a
            print(list_of_ID[count], b, k, b[7])
        else:
            a = sequences.get_seq(long_seq[count], k-7, k+7)
            seq_len = len(sequences[count])
            if k+7 > seq_len:
                ex = (k+7)-seq_len
                b = ex * "X"
                a = str(a)
                a += b
                print(list_of_ID[count], a, k, a[7])
            else:
                print(list_of_ID[count], a, k, a[7])
    count += 1
sys.stdout.close()
