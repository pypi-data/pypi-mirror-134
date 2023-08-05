# Setup Teardown Content Decorator

This is a simple package that aims to make adding setup and teardown to pytest flavored tests quick and painless.

# Installation
```
python3 -m pip install setup-teardown
```

## Provided Postgres Database Class Decorator Usage
Extend and implement the session.
```
class TableScrub(PostgresScrub):
    """Extend to add session."""

    @cached_property
    def session(self):
        """Only fetch the session one time."""
        return new_session()
```

## Example class with decorator usage
```
class TestHandlerDatabaseRequired:
    @TableScrub(table="table_name")
    def test_handler_success(self, mock_datetime):
        """
        Example of using the SetupTeardown ContextDecorator
        with arbitrary setup and teardown.
        """
        assert 1 == 1
        # Effect the database test that may leave db in dirty state
```

## Example function with decorator usage
```
    @TableScrub(table="table_name")
    def test_insert():
        with TableScrub(setup=setup, teardown=teardown):
            assert 1 == 1
            # Effect the database test that may leave db in dirty state
```

## Example function with context manager usage

```
    def setup(self):
        db.session.new_session().query(self.table).delete()

    def teardown(self):
        db.session.new_session().query(self.table).delete()


    def test_insert():
        with SetupTeardown(setup=setup, teardown=teardown):
            assert 1 == 1
            # Effect the database test that may leave db in dirty state
```
