import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    """csv dict implemented here"""
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        last_name = row['last_name']
        phone_number = row['phone_number']
        print(f'{last_name}: {phone_number}')


"""or can use """
# for row in csv_reader:
    # print(f'{row["last_name"]}: {row["phone_number"]}')
