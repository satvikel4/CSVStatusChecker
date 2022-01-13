from csv import reader

with open('idoft.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    unfixed = 0
    for row in csv_reader:
        if (row[5] != "Accepted" and row[5] != "Opened"):
            unfixed += 1
    print(unfixed)
