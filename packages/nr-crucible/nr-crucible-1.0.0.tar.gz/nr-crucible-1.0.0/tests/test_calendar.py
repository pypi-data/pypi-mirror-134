import pytest

from crucible.calendar.calendar import fields_check
from crucible.calendar.exceptions import MissingRequiredFields


@pytest.fixture
def fields():
    return [
        "AudienceLevel",
        "ClassName",
        "Description",
        "Department",
        "Section",
        "Hours",
        "FrequencyRegularPrice",
        "Prerequisite",
    ]


def test_fields_match():
    fields = {"AudienceLevel", "ClassName", "Description", "Department", "Section", "Hours",
              "FrequencyRegularPrice", "Prerequisite"}
    assert fields_check(fields) is True


def test_fields_check_with_empty_list(fields):
    fields = {}
    with pytest.raises(MissingRequiredFields) as e:
        assert fields_check(fields)
    assert str(
        e.value) == 'Invalid fields.  Missing [AudienceLevel, ClassName, Department, Description, FrequencyRegularPrice, Hours, Prerequisite, Section]'


def test_fields_check_missing_one_field(fields):
    fields = {"AudienceLevel", "ClassName", "Description", "Department", "Section", "Hours",
              "FrequencyRegularPrice", ""}
    with pytest.raises(MissingRequiredFields) as e:
        assert fields_check(fields)
    assert str(
        e.value) == 'Invalid fields.  Missing [Prerequisite]'


def test_fields_check_missing_all_but_one(fields):
    fields = {"AudienceLevel"}
    with pytest.raises(MissingRequiredFields) as e:
        assert fields_check(fields)
    assert str(
        e.value) == 'Invalid fields.  Missing [ClassName, Department, Description, FrequencyRegularPrice, Hours, Prerequisite, Section]'
