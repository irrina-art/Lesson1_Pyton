from Мусор.Companytable import CompanyTable


db = CompanyTable("postgresql://postgres@localhost:5432/111")

def test_get_species():
    db_result = db.get_species()
    print(db_result)