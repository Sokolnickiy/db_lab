"""Database creation

Revision ID: a2ff89e65882
Revises: 
Create Date: 2023-12-22 10:23:58.753335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2ff89e65882'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "class_info",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("profile_name", sa.String(50), nullable=False),
        sa.Column("lang_name", sa.String(50), nullable=False)
    )
    op.create_table(
        "location_info",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("reg_name", sa.String(255), nullable=False),
        sa.Column("area_name", sa.String(255), nullable=False),
        sa.Column("ter_name", sa.String(255), nullable=False),
    )
    op.create_table(
        "e_o",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("type_name", sa.String(255), nullable=True),
        sa.Column("parent", sa.String(255), nullable=True),
        sa.Column("location_info_id", sa.Integer(), sa.ForeignKey("location_info.id"), nullable=False)
    )
    op.create_table(
        "person",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("outid", sa.String(255), nullable=False, unique=True),
        sa.Column("birth", sa.Integer(), nullable=False),
        sa.Column("sex_type", sa.String(50), nullable=False),
        sa.Column("location_info_id", sa.Integer(), sa.ForeignKey("location_info.id"), nullable=False),
        sa.Column("e_o_id", sa.Integer(), sa.ForeignKey("e_o.id"), nullable=True),
        sa.Column("class_info_id", sa.Integer(), sa.ForeignKey("class_info.id"), nullable=True)
    )
    op.create_table(
        "test",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("ball", sa.Float(), nullable=True),
        sa.Column("ball100", sa.Float(), nullable=True),
        sa.Column("ball12", sa.Float(), nullable=True),
        sa.Column("status", sa.String(255), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("dpa_level", sa.String(255), nullable=True),
        sa.Column("adapt_scale", sa.Integer(), nullable=True),
        sa.Column("location_info_id", sa.Integer(), sa.ForeignKey("location_info.id"), nullable=False),
    )
    op.create_table(
        "person_test",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column("test_id", sa.Integer(), sa.ForeignKey("test.id"), nullable=False),
        sa.Column("person_id", sa.Integer(), sa.ForeignKey("person.id"), nullable=False)
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS class_info CASCADE")
    op.execute("DROP TABLE IF EXISTS location_info CASCADE")
    op.execute("DROP TABLE IF EXISTS e_o CASCADE")
    op.execute("DROP TABLE IF EXISTS person CASCADE")
    op.execute("DROP TABLE IF EXISTS test CASCADE")
    op.execute("DROP TABLE IF EXISTS person_test CASCADE")
