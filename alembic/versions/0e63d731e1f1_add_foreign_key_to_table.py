"""add foreign key to table

Revision ID: 0e63d731e1f1
Revises: 93197801e817
Create Date: 2026-05-29 13:48:47.234143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e63d731e1f1'
down_revision: Union[str, Sequence[str], None] = '93197801e817'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('post',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table="post",referent_table="user",local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk',table_name='post')
    op.drop_column('post','owner_id')
    """Downgrade schema."""
    
    pass
