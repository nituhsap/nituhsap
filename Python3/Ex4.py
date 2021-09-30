import csv

def read_csv():
    B = []
    with open("table.csv", 'r') as text:
        text = csv.reader(text)
        for line in text:
            A = line[0].split(';')
            B.append(A)
    return B
def add_0 (lst_2D):
    for i in range(len(lst_2D)):
        lst_2D[i] = lst_2D[i][:len(lst_2D[i])//2] + [0] + lst_2D[i][len(lst_2D[i])//2:]

    lst_2D = lst_2D[:len(lst_2D)//2] + [[0]*(len(lst_2D)+1)] + lst_2D[len(lst_2D)//2:]
    return lst_2D
def add_csv(lst_2D):
    with open('tablet.csv', 'w') as file:
        writer = csv.writer(file, delimiter = ";")
        for line in lst_2D:
            writer.writerow(line)

new_csv_list = add_0(read_csv())
add_csv(new_csv_list)

