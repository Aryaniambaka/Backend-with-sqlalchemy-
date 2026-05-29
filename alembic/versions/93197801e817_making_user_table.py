"""making user table

Revision ID: 93197801e817
Revises: 5bfe899c46b7
Create Date: 2026-05-28 23:04:04.121475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93197801e817'
down_revision: Union[str, Sequence[str], None] = '5bfe899c46b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('user',sa.Column('id',sa.Integer(),nullable=False),sa.Column('email',sa.String(),nullable=False),sa.Column('password',sa.String(),nullable=False),sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("now()")),sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("user")
    pass
