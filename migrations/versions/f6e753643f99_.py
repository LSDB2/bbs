"""empty message

Revision ID: f6e753643f99
Revises: af1d34160884
Create Date: 2017-04-14 18:45:58.186732

"""

# revision identifiers, used by Alembic.
revision = 'f6e753643f99'
down_revision = 'af1d34160884'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('ct', sa.Integer(), nullable=True))
    op.add_column('topics', sa.Column('ct', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topics', 'ct')
    op.drop_column('comments', 'ct')
    ### end Alembic commands ###
