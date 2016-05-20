"""Add banana stuff

Revision ID: dea5f62444a8
Revises: f4c441491815
Create Date: 2016-05-20 15:21:13.554214

"""

# revision identifiers, used by Alembic.
revision = 'dea5f62444a8'
down_revision = 'f4c441491815'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('mod', sa.Column('banana_id', sa.Integer))
    op.add_column('mod', sa.Column('banana_verified', sa.Boolean()))
    op.add_column('mod', sa.Column('banana_verification', sa.String(512)))
    pass


def downgrade():
    op.drop_column('mod', 'banana_id')
    op.drop_column('mod', 'banana_verified')
    op.drop_column('mod', 'banana_verification')
    pass
