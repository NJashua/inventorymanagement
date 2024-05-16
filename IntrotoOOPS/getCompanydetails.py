from flask import Flask, render_template
import json

app = Flask(__name__)

with open('company_data.json', 'r') as file:
    company_data = json.load(file)

@app.route('/getcompanydetails/<ticker_symbol>', methods=['GET'])
def get_company_details(ticker_symbol):

    for company in company_data:
        if company['ticker_symbol'] == ticker_symbol:
            return render_template('index.html', company=company)
    return render_template('index.html', error="Ticker symbol not found")

if __name__ == '__main__':
    app.run(debug=True)
