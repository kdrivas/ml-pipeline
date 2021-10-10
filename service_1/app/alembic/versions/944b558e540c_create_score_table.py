"""create score table

Revision ID: 944b558e540c
Revises: 
Create Date: 2021-10-06 18:14:08.246085

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '944b558e540c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  op.create_table('predictions', 
      sa.Column('id', sa.Integer, index=True, primary_key=True),
      sa.Column('credit_score_1', sa.Float, nullable=False),
      sa.Column('credit_score_2', sa.Float, nullable=False),
      sa.Column('credit_score_3', sa.Float, nullable=False),
      sa.Column('credit_score_4', sa.Float, nullable=False),
      sa.Column('pred', sa.Integer, nullable=False))

def downgrade():
  op.drop_table('predictions')
