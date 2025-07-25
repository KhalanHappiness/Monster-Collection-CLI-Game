"""Initial tables

Revision ID: 330521989b80
Revises: 
Create Date: 2025-06-17 10:15:20.149681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '330521989b80'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('monster_species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('base_hp', sa.Integer(), nullable=True),
    sa.Column('base_attack', sa.Integer(), nullable=True),
    sa.Column('base_defense', sa.Integer(), nullable=True),
    sa.Column('rarity', sa.String(), nullable=True),
    sa.Column('abilities', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.Column('money', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('battles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player1_id', sa.Integer(), nullable=True),
    sa.Column('player2_id', sa.Integer(), nullable=True),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['player1_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['player2_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_achievements',
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.Column('achievement_id', sa.Integer(), nullable=False),
    sa.Column('unlocked_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['achievement_id'], ['achievements.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.PrimaryKeyConstraint('player_id', 'achievement_id')
    )
    op.create_table('player_monsters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('current_hp', sa.Integer(), nullable=True),
    sa.Column('experience', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['species_id'], ['monster_species.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_player', sa.Integer(), nullable=True),
    sa.Column('to_player', sa.Integer(), nullable=True),
    sa.Column('offered_monsters', sa.String(), nullable=True),
    sa.Column('requested_monsters', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['from_player'], ['players.id'], ),
    sa.ForeignKeyConstraint(['to_player'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trades')
    op.drop_table('player_monsters')
    op.drop_table('player_achievements')
    op.drop_table('battles')
    op.drop_table('players')
    op.drop_table('monster_species')
    op.drop_table('achievements')
    # ### end Alembic commands ###
