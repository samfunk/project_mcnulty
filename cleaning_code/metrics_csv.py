import csv

def transform(ticker):
    in_file = '/home/ubuntu/mcnultydata/metrics_csv/%s.csv' % ticker.replace('-','')
    data = []
    with open(in_file, 'r') as f:
        csv_data = csv.reader(f)
        
        for row in csv_data:
            data.append(row[:5])

    with open('/home/ubuntu/mcnultydata/final_metrics.csv', 'a') as f:
        for ind in range(1,5):
            f.write('%s_%d,' % (ticker, ind))
            for row in data[1:-7]:
                f.write('%s,' % row[ind])
      
            f.write('\n')

with open('/home/ubuntu/mcnultydata/tickers.txt', 'r') as f:
    tickers = f.read().split('\n')

for ticker in tickers[:-1]:
    transform(ticker)
