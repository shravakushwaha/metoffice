"""init

Revision ID: 9cbc3d3d0f5a
Revises: 
Create Date: 2022-04-10 13:39:16.369186

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '9cbc3d3d0f5a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('metofiice',
    sa.Column('modified_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('years', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('jan', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('feb', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('mar', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('apr', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('may', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('jun', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('jul', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('aug', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('sep', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('oct', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('nov', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('dec', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('win', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('spr', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('sum', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('aut', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('ann', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('region', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('parameter', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_metofiice_ann'), 'metofiice', ['ann'], unique=False)
    op.create_index(op.f('ix_metofiice_apr'), 'metofiice', ['apr'], unique=False)
    op.create_index(op.f('ix_metofiice_aug'), 'metofiice', ['aug'], unique=False)
    op.create_index(op.f('ix_metofiice_aut'), 'metofiice', ['aut'], unique=False)
    op.create_index(op.f('ix_metofiice_created_on'), 'metofiice', ['created_on'], unique=False)
    op.create_index(op.f('ix_metofiice_dec'), 'metofiice', ['dec'], unique=False)
    op.create_index(op.f('ix_metofiice_feb'), 'metofiice', ['feb'], unique=False)
    op.create_index(op.f('ix_metofiice_id'), 'metofiice', ['id'], unique=False)
    op.create_index(op.f('ix_metofiice_is_active'), 'metofiice', ['is_active'], unique=False)
    op.create_index(op.f('ix_metofiice_jan'), 'metofiice', ['jan'], unique=False)
    op.create_index(op.f('ix_metofiice_jul'), 'metofiice', ['jul'], unique=False)
    op.create_index(op.f('ix_metofiice_jun'), 'metofiice', ['jun'], unique=False)
    op.create_index(op.f('ix_metofiice_mar'), 'metofiice', ['mar'], unique=False)
    op.create_index(op.f('ix_metofiice_may'), 'metofiice', ['may'], unique=False)
    op.create_index(op.f('ix_metofiice_nov'), 'metofiice', ['nov'], unique=False)
    op.create_index(op.f('ix_metofiice_oct'), 'metofiice', ['oct'], unique=False)
    op.create_index(op.f('ix_metofiice_parameter'), 'metofiice', ['parameter'], unique=False)
    op.create_index(op.f('ix_metofiice_region'), 'metofiice', ['region'], unique=False)
    op.create_index(op.f('ix_metofiice_sep'), 'metofiice', ['sep'], unique=False)
    op.create_index(op.f('ix_metofiice_spr'), 'metofiice', ['spr'], unique=False)
    op.create_index(op.f('ix_metofiice_sum'), 'metofiice', ['sum'], unique=False)
    op.create_index(op.f('ix_metofiice_win'), 'metofiice', ['win'], unique=False)
    op.create_index(op.f('ix_metofiice_years'), 'metofiice', ['years'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_metofiice_years'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_win'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_sum'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_spr'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_sep'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_region'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_parameter'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_oct'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_nov'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_may'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_mar'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_jun'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_jul'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_jan'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_is_active'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_id'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_feb'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_dec'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_created_on'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_aut'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_aug'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_apr'), table_name='metofiice')
    op.drop_index(op.f('ix_metofiice_ann'), table_name='metofiice')
    op.drop_table('metofiice')
    # ### end Alembic commands ###
