from sqlalchemy import create_engine, inspect

db_connection_string = "postgresql://postgres@localhost:5432/111"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    print("all tables:")
    for name in names:
     print(name)
     assert 'places' in names