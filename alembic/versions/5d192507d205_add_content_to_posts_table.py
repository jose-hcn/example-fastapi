"""add content to posts table

Revision ID: 5d192507d205
Revises: 5fef5927f81c
Create Date: 2024-11-11 21:44:46.892338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d192507d205'
down_revision: Union[str, None] = '5fef5927f81c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
