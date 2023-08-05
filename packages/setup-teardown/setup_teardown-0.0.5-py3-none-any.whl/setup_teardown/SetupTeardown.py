"""Setup Teardown helper classes."""
from functools import cached_property, wraps


class SetupTeardown:
    """Setup Teardown class."""

    def __init__(self, table: str, **kwargs):
        """Accept table name."""
        self.table = table
        self.__dict__.update(kwargs)

    def __call__(self, _func):
        """Catch any call misses, wrap with self."""

        @wraps(_func)
        def wrapper(*args, **kw):
            with self:
                return _func(*args, **kw)

        return wrapper

    def __enter__(self):
        """Entrace/setup function for context manager."""
        self.setup()
        return self

    def __exit__(self, typ, val, traceback):
        """Exit/teardown function for context manager."""
        self.teardown()

    def setup(self):
        """Stub for db setup, needs to be subclassed and implemented."""
        raise NotImplementedError("SetupTeardown.setup NotImplemented")

    def teardown(self):
        """Stub for db setup, needs to be subclassed and implemented."""
        raise NotImplementedError("SetupTeardown.teardown NotImplemented")


class PostgresScrub(SetupTeardown):
    """Simple example Postgres setup teardown class."""

    @cached_property
    def session(self):
        """Only fetch the session one time.  Requires implementation."""
        raise NotImplementedError("DB session NotImplemented")

    def _empty(self):
        """Empty a table."""
        self.session.query(self.table).delete()
        self.session.commit()

    def setup(self):
        """Perform database setup."""
        self._empty()

    def teardown(self):
        """Perform database teardown."""
        self._empty()
