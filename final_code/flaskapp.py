import flask
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pickle
from recent_earnings_tickers import ok_tickers
import re

#---------- Model ----------------#

#with open('/Users/samfunk/ds/metis/project_mcnulty/code/REPLACE_WITH_MODEL_PICKLE', 'rb') as f:
    #PREDICTOR = pickle.load(f)


'''Have final model in the pickle file
Should be prefit to main data
Simply ask for a company/list of companies
Input the ticker into model (which will scrape web for current features)
Pray some of them are right'''



#---------- URLS AND WEB PAGES -------------#
app = flask.Flask(__name__)

@app.route('/')
def home_page():
    with open("/Users/samfunk/ds/metis/project_mcnulty/stock_page.html",'r') as viz_file:
        return viz_file.read()


@app.route("/stock", methods=["POST"])
def stock(ok_tickers=ok_tickers()):

    data = flask.request.json
    ticker = str(data["ticker"]).upper()
    if ticker in ok_tickers:
        earnings_soup = BeautifulSoup(requests.get("https://finance.yahoo.com/quote/%s/analysts?p=%s" % (ticker, ticker)).text, 'html.parser')
        surprise_string = earnings_soup.find_all('table')[2].tbody.find_all('tr')[3].find_all('td')[4].text
        surprise = float(re.search(r'(.*)%', surprise_string)[1])


        #score = PREDICTOR.predict_proba(x)

        if abs(surprise) < 5.0:
            score = 0
        else:
            score = 1
    else:
        surprise_string = 'null'
        score = 'null'
    #score = PREDICTOR.predict_proba(x)
    results = {"surprise": surprise_string, "score": score}

    print(ticker, results)
    return flask.jsonify(results)

if __name__ == '__main__':
    app.run()
