import csv

def ReadOnlySimpleLineCSV():
    # CSVファイルを読み込む
    with open('qestions.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # CSVファイルの内容をリストに格納
        data_list = [row[0] for row in reader]
    return data_list