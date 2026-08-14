from Typename import Type


db = Type("postgresql://postgres@localhost:5432/111")


def test_add_type():

    new_data = {
       'type_id': 15,
       'type_name': 'грибы'
    }
    db.add_type(**new_data)
    types_list = db.get_species_type()
    print(types_list)
    assert any(item == new_data['type_name']for item in types_list)

    delete_rows = db.delete_species_type(15)
    print(delete_rows)
    after_deletion = db.get_species_type()
    print(after_deletion)
    assert (item == new_data['type_id'] == 15 for item in after_deletion)
