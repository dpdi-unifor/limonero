""" extra parameters for storage  

Revision ID: 3949289c976c
Revises: 0c56a2478a23
Create Date: 2020-06-09 16:19:24.260000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3949289c976c'
down_revision = '0c56a2478a23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('storage', sa.Column('client_url', sa.String(length=1000), nullable=True))
    op.add_column('storage', sa.Column('extra_params', mysql.LONGTEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('storage', 'extra_params')
    op.drop_column('storage', 'client_url')
    # ### end Alembic commands ###
