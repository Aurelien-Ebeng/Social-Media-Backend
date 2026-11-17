"""add foreign key to post table

Revision ID: c20017fa85dc
Revises: 6ab92321be1b
Create Date: 2026-11-17 06:46:44.094703

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c20017fa85dc"
down_revision: Union[str, Sequence[str], None] = "6ab92321be1b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "owner_id")
    pass
