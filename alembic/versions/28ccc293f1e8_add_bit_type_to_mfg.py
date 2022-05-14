"""add bit type to mfg

Revision ID: 28ccc293f1e8
Revises: 
Create Date: 2022-05-12 21:47:21.821101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28ccc293f1e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('manufacturer', sa.Column('bit_class', sa.String(50), nullable=False))


def downgrade():
    op.drop_column('manufacturer', 'bit_class')
