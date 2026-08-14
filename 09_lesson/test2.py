from Typename import Type


db = Type("postgresql://postgres@localhost:5432/111")


def test_update_type():
    db.add_type(type_id=8, type_name='трава')
    types_list_before = db.get_species_type()
    print(types_list_before)
    assert (item['type_id'] == 8 and ['type_name'] == 'трава' for item in types_list_before)

    update_rows = db.update_type_name(8, 'дерево')
    print(update_rows)
    after_update = db.get_species_type()
    print(after_update)
    assert (item == 'дерево' for item in after_update)

    delete_rows = db.delete_species_type(8)
    print(delete_rows)
    final_list = db.get_species_type()
    print(final_list)
    assert (item['type_id'] == 8 for item in final_list)
