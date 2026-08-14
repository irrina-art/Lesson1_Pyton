
from Мусор.Companytable import CompanyTable
from datetime import date


db = CompanyTable("postgresql://postgres@localhost:5432/111")

def test_add_species():
    new_data = {
        'species_id': 111,
        'species_name': 'Аарбуз',
        'species_amount': 10,
        'date_start': date(2026, 8, 1),
        'species_status': 'active'

    }

    new_name = db.add_species(**new_data)
    print(f'Добавлен объект с name: {new_name}')

    #deleted_rows = db.delete_species(species_name="Аарбуз")
    #print (f"удалено записей: {deleted_rows}")
    #assert deleted_rows == 1

    