"""empty message

Revision ID: af1d34160884
Revises: 7cfb1430d6de
Create Date: 2017-04-14 18:29:05.749131

"""

# revision identifiers, used by Alembic.
revision = 'af1d34160884'
down_revision = '7cfb1430d6de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nodes', sa.Column('ct', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('nodes', 'ct')
    ### end Alembic commands ###