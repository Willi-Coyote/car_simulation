from field import Field


def test_given_inside_coord_is_outside_is_false():
    field = Field(10, 10)

    is_outside = field.is_outside(1, 1)

    assert is_outside is False


def test_given_x_outside_coord_is_outside_is_true():
    field = Field(10, 10)

    is_outside = field.is_outside(11, 1)

    assert is_outside is True


def test_given_y_outside_coord_is_outside_is_true():
    field = Field(10, 10)

    is_outside = field.is_outside(1, 11)

    assert is_outside is True


def test_given_0_0_coord_is_outside_is_false():
    field = Field(10, 10)

    is_outside = field.is_outside(0, 0)

    assert is_outside is False
