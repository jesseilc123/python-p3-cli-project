"""Initial commit

Revision ID: c81e4eaf8cc9
Revises: 
Create Date: 2023-06-14 15:19:07.910965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c81e4eaf8cc9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('exp', sa.Integer(), nullable=True),
    sa.Column('skin', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('players')
    # ### end Alembic commands ###
