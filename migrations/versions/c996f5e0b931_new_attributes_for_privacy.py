"""new attributes for privacy

Revision ID: c996f5e0b931
Revises: 9dccb02d8201
Create Date: 2017-07-04 10:46:02.417305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c996f5e0b931'
down_revision = '9dccb02d8201'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attribute_privacy', sa.Column('attribute_name', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('attribute_privacy', 'attribute_name')
    # ### end Alembic commands ###
