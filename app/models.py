#models.py
from db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    risk_tolerance = db.Column(db.Float, nullable=False, default=0.0)
    trades = db.relationship('Trade', backref='user', lazy=True)

    # Flask-Login integration
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class OptionsContract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trade_id = db.Column(db.Integer, db.ForeignKey('trade.id'), nullable=False)
    symbol = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(10), nullable=False)  # "call" or "put"
    strike = db.Column(db.Float, nullable=False)
    expiry = db.Column(db.Date, nullable=False)
    iv = db.Column(db.Float)
    delta = db.Column(db.Float)
    gamma = db.Column(db.Float)
    theta = db.Column(db.Float)
    vega = db.Column(db.Float)
    open_interest = db.Column(db.Integer)
    volume = db.Column(db.Integer)

    def __repr__(self):
        return f'<OptionsContract {self.id}>'

class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    asset = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    trade_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='open')
    profit_loss = db.Column(db.Float)
    contracts = db.relationship('OptionsContract', backref='trade', lazy=True)

    def calculate_profit_loss(self, current_market_price):
        # Implement logic to calculate profit/loss based on current market price
        pass

    def __repr__(self):
        return f'<Trade {self.id}>'

class MarketData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(50), nullable=False, index=True)
    historical_data = db.Column(db.JSON, nullable=False)
    options_data = db.Column(db.JSON)

    def __repr__(self):
        return f'<MarketData {self.ticker}>'
