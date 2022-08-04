"""empty message

Revision ID: 317fbf000bd4
Revises: 0beceac61218
Create Date: 2022-08-03 05:39:51.127543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317fbf000bd4'
down_revision = '0beceac61218'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('past_shows', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Artist', sa.Column('upcoming_shows', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('past_shows', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('past_shows_count', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('upcoming_shows_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'upcoming_shows_count')
    op.drop_column('Venue', 'upcoming_shows')
    op.drop_column('Venue', 'past_shows_count')
    op.drop_column('Venue', 'past_shows')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'upcoming_shows_count')
    op.drop_column('Artist', 'upcoming_shows')
    op.drop_column('Artist', 'past_shows_count')
    op.drop_column('Artist', 'past_shows')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_talent')
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###
