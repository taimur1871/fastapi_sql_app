from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, event, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query

engine = create_engine(
    'postgresql+psycopg2://postgres:postgres@localhost:5432/bit_data',
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Default naming convention for all indexes and constraints
# See why this is important and how it would save your time:
# https://alembic.sqlalchemy.org/en/latest/naming.html
# convention = {
#     'all_column_names': lambda constraint, table: '_'.join([
#         column.name for column in constraint.columns.values()
#     ]),
#     'ix': 'ix__%(table_name)s__%(all_column_names)s',
#     'uq': 'uq__%(table_name)s__%(all_column_names)s',
#     'ck': 'ck__%(table_name)s__%(constraint_name)s',
#     'fk': (
#         'fk__%(table_name)s__%(all_column_names)s__'
#         '%(referred_table_name)s'
#     ),
#     'pk': 'pk__%(table_name)s'
# }

# Registry for all tables
# metadata = MetaData(naming_convention=convention)
Base = declarative_base()


def initialize_continuum():
    # Required to configuring versioning support for all Models where it is declared
    sa.orm.configure_mappers()


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class SoftDeleteMixin:
    deleted_at = sa.Column(sa.DateTime(timezone=True), nullable=True)

    def delete(self, deleted_at: datetime = None):
        self.deleted_at = deleted_at or datetime.now()

    def restore(self):
        self.deleted_at = None


@event.listens_for(Query, 'before_compile', retval=True)
def before_compile(query):
    include_deleted = query._execution_options.get('include_deleted', False)
    if include_deleted:
        return query

    for column in query.column_descriptions:
        entity = column['entity']
        if entity is None:
            continue

        inspector = inspect(column['entity'])
        mapper = getattr(inspector, 'mapper', None)
        if mapper and issubclass(mapper.class_, SoftDeleteMixin):
            query = query.enable_assertions(False).filter(
                entity.deleted_at.is_(None),
            )

    return query


@event.listens_for(SoftDeleteMixin, 'load', propagate=True)
def load(obj, context):
    pass
    # TODO: this is no longer valid should we re-enable?
    # Allowing models to load soft-deleted dependencies so that Anomalies can still eager load their Checks
    # This may lead to bad side-effects so leaving the prior logic commented here until this soaks.
    # include_deleted = context.query._execution_options.get('include_deleted', False)
    # if obj.deleted_at and not include_deleted:
    #     raise TypeError(f'Deleted object {obj} was loaded, did you use joined eager loading?')


