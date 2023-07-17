import settings
from tests.example import example_list


def test_delete_empty_operations():
    assert settings.delete_empty_operations([{}]) == []


def test_first_five_sorted_operations():
    assert settings.first_five_sorted_operations(example_list) == sorted(example_list,
                                                                         key=lambda operation_data: (
                                                                             operation_data['state'],
                                                                             operation_data['date']),
                                                                         reverse=True
                                                                         )[:5]
