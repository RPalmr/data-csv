import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            """skip header"""
            line_count += 1
        else:
            last_name, phone_number = row[1], row[2]
            print(f'{last_name}: {phone_number}')
            line_count += 1
