import pytest
from data_engineering.unitesting  import capitalize_first_letter

# but doing the things like this is not the best way to do it, because we are not testing the
# function in all the possible ways, so we can use the parametrize decorator
#  to test the function in all the possible ways

@pytest.mark.parametrize(
    "input, expected",  # Nombres de los parámetros
    [
        ("fabricio", "Fabricio"),
        ("FABRICIO", "Fabricio"),
        ("Fabricio", "Fabricio"),
        ("fabricio", "Fabricio")
    ]
)

def test_capitalize_first_letter(input, expected):
    assert capitalize_first_letter(input) == expected
