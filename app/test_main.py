import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 27, [3, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ]
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    human_age: tuple[int, int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_output_changes() -> None:
    assert get_human_age(14, 14) != get_human_age(15, 15)


@pytest.mark.parametrize(
    "cat_age, dog_age", [
        ("abc", 12),
        (12, "csd"),
        ("d", "k"),
        (20, 20.5),
        (20.5, 20)

    ]
)
def test_invalid_type(cat_age, dog_age) -> None:
    with pytest.raises((TypeError, ValueError)):
        get_human_age(cat_age, dog_age)
