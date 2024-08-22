from main import first_last_name

def test_name():
    my_name = first_last_name('sadaf', 'rahman')
    assert my_name == "Sadaf Rahman"
