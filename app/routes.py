from flask import render_template, send_file, make_response, request, redirect, url_for
from app import app
from flask_bootstrap import Bootstrap
import MathPart as mp
import base64


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    # pgain = mp.stockPriceCalculator("TSLA", 1000, "2020-02-03", "2020-02-07")
    stock = ''
    submitted = False
    error = False
    if request.method == 'POST':
        stock = request.form.get('stock')
        init = request.form.get('init')
        start = request.form.get('start')
        end = request.form.get('end')
        submitted = request.form.get('submitted')
        if not mp.isStockReal(stock):
            return render_template('index.html', stock=stock, plot_url=plot_url, submitted=submitted, answers=answers)
        if submitted == 'Try Again?':
            submitted = False
            return redirect(url_for('index'))
        answers = mp.stockPriceCalculator(stock, round(float(init), 2), start, end)
        bytes_obj = mp.stockPlotter(stock, start, end)
        submitted = True
        # session['stock'] = stock
        plot_url = base64.b64encode(bytes_obj.getvalue()).decode()
        return render_template(
            'index.html', stock=stock, plot_url=plot_url, submitted=submitted, answers=answers)
    return render_template(
        'index.html', stock=stock, submitted=submitted)
