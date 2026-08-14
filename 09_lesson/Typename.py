from sqlalchemy import create_engine, text


class Type:
    def __init__(self, connection_string):
     self.db = create_engine(connection_string)


def get_species_type(self):
    with self.db.connect() as conn:
     result = conn.execute(text("SELECT type_name FROM species_type"))
    return [row['type_name'] for row in result.mappings()]


def add_type(self, type_id, type_name):
    query = text("INSERT INTO species_type (type_id, type_name) VALUES (:type_id, :type_name)")
    with self.db.connect() as conn:
        result = conn.execute(query, {'type_id': type_id, 'type_name': type_name})
    conn.commit()
    return result.lastrowid


def delete_species_type(self, type_id):
    query = text("DELETE FROM species_type WHERE type_id=:type_id")
    with self.db.connect() as conn:
        result = conn.execute(query, {'type_id': type_id})
    conn.commit()
    return result.rowcount


def update_type_name(self, type_id, new_name):
    query = text("UPDATE species_type SET type_name=:new_name WHERE type_id=:type_id")
    with self.db.connect() as conn:
        result = conn.execute(query, {'type_id': type_id, 'new_name': new_name})
    conn.commit()
    return result.rowcount
