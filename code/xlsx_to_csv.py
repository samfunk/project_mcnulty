import xlrd
import csv
import tickerlist

tickers = tickerlist.make_list()

tickers.pop()
tickers.pop()

total_count = 0
base = '/Users/samfunk/ds/metis/project_mcnulty/code/stockrow_metrics/stockrow_metrics_'

for t in range(5):
    directory = base + str(total_count)
    file_count = 0
    while file_count < 101:
        wb = xlrd.open_workbook('%s/financials (%s).xlsx' % (directory, str(file_count)))
        sh = wb.sheet_by_name(tickers[total_count])
        your_csv_file = open('/Users/samfunk/ds/metis/project_mcnulty/code/metrics_csv/%s.csv' % tickers[total_count], 'w')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()
        file_count += 1
        total_count += 1
