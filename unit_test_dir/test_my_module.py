

from my_module import get_cube_of_a_number

def test_get_cube(input_value):
    #when
    subject = get_cube_of_a_number(input_value)

    #then
    assert subject == 62