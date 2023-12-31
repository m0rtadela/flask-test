"""Initial migration.

Revision ID: 86e13c6ba6e4
Revises: 
Create Date: 2023-02-12 05:05:38.473599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86e13c6ba6e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('constancias', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('rfc',
               existing_type=sa.VARCHAR(length=13),
               nullable=True)
        batch_op.alter_column('curp',
               existing_type=sa.VARCHAR(length=18),
               nullable=True)
        batch_op.alter_column('tipo',
               existing_type=sa.CHAR(length=2),
               type_=sa.String(length=2),
               nullable=True)
        batch_op.alter_column('owner',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.TEXT(),
               type_=sa.String(length=60),
               nullable=True)
        batch_op.alter_column('file_url',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
#         batch_op.drop_table_comment(
#         'constancias',
#         existing_comment='Constancias solicitadas',
#         schema=None
#     )

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    with op.batch_alter_table('constancias', schema=None) as batch_op:
        batch_op.create_table_comment(
        'constancias',
        'Constancias solicitadas',
        existing_comment=None,
        schema=None
    )
        batch_op.alter_column('file_url',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.String(length=60),
               type_=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('owner',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('tipo',
               existing_type=sa.String(length=2),
               type_=sa.CHAR(length=2),
               nullable=False)
        batch_op.alter_column('curp',
               existing_type=sa.VARCHAR(length=18),
               nullable=False)
        batch_op.alter_column('rfc',
               existing_type=sa.VARCHAR(length=13),
               nullable=False)
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
