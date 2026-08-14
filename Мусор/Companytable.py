from sqlalchemy import create_engine, text


class CompanyTable:
    __scripts = {
        "select": text("SELECT * FROM species"),
        "delete by name": text("DELETE FROM species WHERE species_name=:species_name")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_species(self):
        conn = self.db.connect()
        result = conn.execute(text("SELECT * FROM species"))
        rows = result.mappings().all()
        conn.close()
        return rows

    def add_species(self, species_id, species_name, species_amount, date_start, species_status):
        conn = self.db.connect()
        query = text("INSERT INTO species (species_id, species_name, species_amount, date_start, species_status)"
                          "VALUES (:species_id, :species_name, :species_amount, :date_start, :species_status)")
        result = conn.execute(query,
                              {'species_id': species_id,
                                      'species_name': species_name,
                                      'species_amount': species_amount,
                                      'date_start': date_start,
                                      'species_status': species_status
                              })
        conn.close()
        return result.lastrowid

    def delete_species(self, species_name):
        conn = self.db.connect()
        result = conn.execute(
            self.__scripts["delete by name"],
            {"species_name": species_name}
        )
        conn.commit()
        conn.close()
        return result.rowcount