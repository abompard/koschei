"""Store distance in dependency

Revision ID: 4c8bb5a1cf4a
Revises: 2a5e201f5bce
Create Date: 2014-08-26 15:56:18.334442

"""

# revision identifiers, used by Alembic.
revision = '4c8bb5a1cf4a'
down_revision = '2a5e201f5bce'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dependency', sa.Column('distance', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dependency', 'distance')
    ### end Alembic commands ###