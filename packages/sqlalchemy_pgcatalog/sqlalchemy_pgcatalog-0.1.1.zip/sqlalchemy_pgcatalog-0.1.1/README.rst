SQLAlchemy PostgreSQL Catalog Definition
========================================

SQLAlchemy schema definition (partially reflected) for the PostgreSQL catalog (pg_catalog schema)

Example
=======

Simple example::

    >>> import sqlalchemy

    >>> import sqlalchemy_pgcatalog

    >>> engine = sqlalchemy.create_engine("postgresql://localhost:5432/examples")

    >>> list(engine.execute(select([sqlalchemy_pgcatalog.Lock])))
    [('relation', 320034, 11090, None, None, None, None, None, None, None, '2/77352', 23112, 'AccessShareLock', True, True),
     ('virtualxid', None, None, None, None, '2/77352', None, None, None, None, '2/77352', 23112, 'ExclusiveLock', True, True)]
