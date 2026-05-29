"""add context Column to post table

Revision ID: 5bfe899c46b7
Revises: 5bf0530cc360
Create Date: 2026-05-28 22:11:26.224709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bfe899c46b7'
down_revision: Union[str, Sequence[str], None] = '5bf0530cc360'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("post",sa.Column('content',sa.String(),nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("post",'content')
    pass
