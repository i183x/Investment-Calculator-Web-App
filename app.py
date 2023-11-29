from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calculate_investment(lump_sum, cagr, years, yearly_addition):
    net_amount = lump_sum
    for year in range(1, years + 1):
        net_amount = net_amount * (1 + cagr / 100) + yearly_addition
    profit = net_amount - (lump_sum + yearly_addition * years)
    return round(net_amount, 2), round(profit, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    lump_sum_amount = float(request.form['lump_sum'])
    cagr_percent = float(request.form['cagr'])
    investment_years = int(request.form['years'])
    yearly_addition = float(request.form['yearly_addition'])

    result, profit = calculate_investment(lump_sum_amount, cagr_percent, investment_years, yearly_addition)

    return render_template('result.html', result={'result': result, 'profit': profit, 'years': investment_years})

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)), debug=False)