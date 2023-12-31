"""2nd - assocation proxy

Revision ID: 2582e8b0e692
Revises: c33d09226af6
Create Date: 2023-06-15 15:00:52.320067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2582e8b0e692'
down_revision = 'c33d09226af6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_worlds')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player_worlds',
    sa.Column('player_id', sa.INTEGER(), nullable=False),
    sa.Column('world_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['world_id'], ['worlds.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'world_id')
    )
    # ### end Alembic commands ###
