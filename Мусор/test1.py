from sqlalchemy import create_engine, MetaData

db_connection_string = "postgresql://postgres@localhost:5432/111"


def test_db_connection():
    engine = create_engine(db_connection_string)
    metadata = MetaData
    with engine.connect() as conn:
        metadata.reflect(bind=engine, con=conn)
    names = metadata.tables.keys()
    assert "species" in names