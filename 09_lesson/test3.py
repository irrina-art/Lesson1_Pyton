from Typename import Type


db = Type("postgresql://postgres@localhost:5432/111")


def test_delete_species_type():
    types_before = db.get_species_type()
    print(types_before)
    assert (item['type_id'] == 99 for item in types_before)

    deleted_rows = db.delete_species_type(99)
    print(deleted_rows)

    after_deletion = db.get_species_type()
    print(after_deletion)

    assert (item['type_id'] == 99 for item in after_deletion)
