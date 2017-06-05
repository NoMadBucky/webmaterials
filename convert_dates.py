import csv
from datetime import datetime

violator_list = '/Users/barry_b_esq/Google Drive/PollutionWatch/webmaterials/EPAWaterViolators.csv'

def convertDate(row):
    ## It would be nice to add a function to search for and identify datefields in the csvfile that are
    ## improperly formatted, put them in a list, and have the program loop through the list. I have done it
    ## the old-fashioned way here, manually identifying the columns that have invalid dates.
    invalid_date_list = (10, 11, 35, 45, 55, 58)
    for item in invalid_date_list:
        if row[item] is '':
            row[item] = "1900-01-01"
        else:
            old_date = row[item]
            old_date_format = datetime.strptime(old_date, '%m/%d/%Y')
            new_date_format = datetime.strftime(old_date_format, '%Y-%m-%d')
            row[item] = new_date_format
    return row

with open(violator_list) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    count = 0
    for permittee in reader:
        effluent_csv_data = ('/Users/barry_b_esq/Google Drive/PollutionWatch/EPAData/' + permittee[0] + '.csv')
        with open(effluent_csv_data) as effluent_csv_file:
            effluent_reader = csv.reader(effluent_csv_file)
            effluent_header = next(effluent_reader)
            rows = list(effluent_reader)
        rows = [convertDate(row) for row in rows]

        with open('/Users/barry_b_esq/Google Drive/PollutionWatch/EPAData/' + permittee[0] + '-formatted.csv', 'w', newline='') as newfile:
            writer = csv.writer(newfile)
            writer.writerow(effluent_header)
            for row in rows:
                writer.writerow(row)
            print (permittee[0] + '.csv reformatted.')

print('Done.')