"""create tables

Revision ID: 49ba048d3c2d
Revises: 
Create Date: 2025-06-08 02:51:35.791624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision: str = '49ba048d3c2d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('client_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('client_email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('booked_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_booking_client_email'), 'booking', ['client_email'], unique=False)
    op.create_index(op.f('ix_booking_client_name'), 'booking', ['client_name'], unique=False)
    op.create_table('fitnessclass',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('class_time', sa.DateTime(), nullable=False),
    sa.Column('instructor', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_slot', sa.Integer(), nullable=False),
    sa.Column('booked_slot', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fitnessclass_name'), 'fitnessclass', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fitnessclass_name'), table_name='fitnessclass')
    op.drop_table('fitnessclass')
    op.drop_index(op.f('ix_booking_client_name'), table_name='booking')
    op.drop_index(op.f('ix_booking_client_email'), table_name='booking')
    op.drop_table('booking')
    # ### end Alembic commands ###
