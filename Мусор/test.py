from sqlalchemy import create_engine

db_connection_string = "postgresql://postgres@localhost:5432/111"


def test_db_connection():
    engine = create_engine(db_connection_string)
    with engine.connect() as conn:
        result = conn.scalars(literal_string("SELECT 1")).one()
        assert result == 1
       