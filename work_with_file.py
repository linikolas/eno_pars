import csv


def write_csv(data):
    with open('test.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['age']))


def write_csv2(data):
    with open('test.csv', 'a') as f:
        rownames = ['name', 'age']
        writer = csv.DictWriter(f, fieldnames=rownames)
        writer.writerow(data)


def main():
    d = {'name': 'vasya', 'age': 18}
    d1 = {'name': 'petya', 'age': 13}
    d2 = {'name': 'olya', 'age': 39}

    lists = [d, d1, d2]

    # for lis in lists:
    #     write_csv2(lis)

    with open('moda.csv') as file:
        rowname = ['brand', 'old_price', 'new_price']
        reader = csv.DictReader(file, fieldnames=rowname)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
