#main.py
from flask import Blueprint, render_template, redirect, url_for, jsonify
from flask_login import login_required, current_user
from chart_functions import get_available_indicators, fetch_chart_data
from models import MarketData

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # Redirect to the 'index' route
    return redirect(url_for('auth.login'))

# Main Page
@main_bp.route('/home')
@login_required
def index():
    return render_template('index.html', user=current_user)

#Charts Page
@main_bp.route('/charts')
@login_required
def charts():
    indicators = get_available_indicators()  # Implement this function
    return render_template('charts.html', indicators=indicators)

@main_bp.route('/search_tickers')
@login_required
def search_tickers():
    search_query = request.args.get('query', '')
    matching_tickers = MarketData.query.filter(MarketData.ticker.like(f'%{search_query}%')).all()
    tickers = [ticker.ticker for ticker in matching_tickers]
    return jsonify(tickers)

@main_bp.route('/get_all_tickers')
@login_required
def get_all_tickers():
    try:
        tickers = [ticker.ticker for ticker in MarketData.query.all()]
        return jsonify(tickers)
    except Exception as e:
        print("Error fetching tickers:", e)
        return jsonify([]), 500  # Returning an empty list for error scenario