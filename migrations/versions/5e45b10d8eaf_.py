"""empty message

Revision ID: 5e45b10d8eaf
Revises: 6ff8d4b68932
Create Date: 2022-07-12 11:31:30.135284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e45b10d8eaf'
down_revision = '6ff8d4b68932'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('group_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'comment', 'group', ['group_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'group_id')
    # ### end Alembic commands ###
