import utils


def test_convert_date():
    assert utils.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert utils.convert_date("2018-06-30T02:08:58.425572") == "30.06.2018"


def test_convert_from():
    assert utils.convert_from("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert utils.convert_from("Счет 75106830613657916952") == "Счет 7510 68** **** 6952"


def test_convert_to():
    assert utils.convert_to("Счет 64686473678894779589") == "Счет **9589"
    assert utils.convert_to("Счет 74489636417521191160") == "Счет **1160"


def test_converted_five_operation():
    assert utils.converted_five_operation() is None


def test_printed_five_operation():
    assert utils.printed_five_operation() is None
