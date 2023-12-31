"""empty message

Revision ID: 2a1b5a53eb79
Revises: a9abe0511a69
Create Date: 2023-06-19 17:03:34.317463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a1b5a53eb79'
down_revision = 'a9abe0511a69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_since', sa.DateTime(), nullable=True))
        batch_op.alter_column('location',
               existing_type=sa.TEXT(),
               type_=sa.String(length=64),
               existing_nullable=True)
        batch_op.alter_column('about_me',
               existing_type=sa.DATETIME(),
               type_=sa.Text(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('about_me',
               existing_type=sa.Text(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('location',
               existing_type=sa.String(length=64),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.drop_column('member_since')

    # ### end Alembic commands ###
