"""empty message

Revision ID: 3b65ebeb65cf
Revises: 
Create Date: 2023-11-26 15:11:17.225422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b65ebeb65cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('market_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=50), nullable=False),
    sa.Column('historical_data', sa.JSON(), nullable=False),
    sa.Column('options_data', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.Column('risk_tolerance', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('trade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('asset', sa.String(length=100), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.Column('trade_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('profit_loss', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('options_contract',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trade_id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=False),
    sa.Column('strike', sa.Float(), nullable=False),
    sa.Column('expiry', sa.Date(), nullable=False),
    sa.Column('iv', sa.Float(), nullable=True),
    sa.Column('delta', sa.Float(), nullable=True),
    sa.Column('gamma', sa.Float(), nullable=True),
    sa.Column('theta', sa.Float(), nullable=True),
    sa.Column('vega', sa.Float(), nullable=True),
    sa.Column('open_interest', sa.Integer(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trade_id'], ['trade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('options_contract')
    op.drop_table('trade')
    op.drop_table('user')
    op.drop_table('market_data')
    # ### end Alembic commands ###