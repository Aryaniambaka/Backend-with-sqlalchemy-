"""add last few to post

Revision ID: 66cd122c8824
Revises: 0e63d731e1f1
Create Date: 2026-05-29 14:28:49.401827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66cd122c8824'
down_revision: Union[str, Sequence[str], None] = '0e63d731e1f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('post',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('post',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('post','published')
    op.drop_column('post','created_at')
    """Downgrade schema."""
    pass
