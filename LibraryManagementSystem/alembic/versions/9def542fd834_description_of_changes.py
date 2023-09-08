"""Description of changes

Revision ID: 9def542fd834
Revises: 324cac73980e
Create Date: 2023-09-08 16:20:49.790943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9def542fd834'
down_revision: Union[str, None] = '324cac73980e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
