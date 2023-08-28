"""empty message

Revision ID: 623f3c854148
Revises: 6a69b834a4c2
Create Date: 2023-08-28 21:13:05.491016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '623f3c854148'
down_revision = '6a69b834a4c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model_type', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('score', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('response', schema=None) as batch_op:
        batch_op.drop_column('score')
        batch_op.drop_column('model_type')

    # ### end Alembic commands ###
