"""add content to posts table

Revision ID: 2b11451069b4
Revises: 534669f3573c
Create Date: 2026-11-17 06:24:53.600062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b11451069b4'
down_revision: Union[str, Sequence[str], None] = '534669f3573c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
