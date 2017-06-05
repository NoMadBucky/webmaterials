import csv

violator_list = '/Users/barry_b_esq/Google Drive/PollutionWatch/webmaterials/EPAWaterViolators.csv'

def convertDate(row):
    invalid_row_list = (10, 11)
    for item in invalid_row_list:
        if row[item] is '':
            row[item] = "0.0000"
    return row

with open(violator_list) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = list(reader)
    count = 0
    rows = [convertDate(row) for row in rows]

    with open('/Users/barry_b_esq/Google Drive/PollutionWatch/webmaterials/EPAWaterViolators'+ '-formatted.csv', 'w', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)

print('Done.')