"""Add new stuff

Revision ID: a851caf3a626
Revises: dea5f62444a8
Create Date: 2016-05-20 15:30:49.412694

"""

# revision identifiers, used by Alembic.
revision = 'a851caf3a626'
down_revision = 'dea5f62444a8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('mod', sa.Column('banana_url', sa.String(512)))
    pass


def downgrade():
    op.drop_column('mod', 'banana_url')
    pass
