"""created posts table

Revision ID: 5bf0530cc360
Revises: 
Create Date: 2026-05-28 20:55:04.039542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bf0530cc360'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('post',sa.Column('id',sa.Integer(),nullable=False,primary_key=True), sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('post')
    """Downgrade schema."""
    pass
