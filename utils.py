import datetime

from settings import five_operations


def convert_date(date: str) -> str:
    date_format = '%Y-%m-%dT%H:%M:%S.%f'
    new_date = datetime.datetime.strptime(date, date_format)
    return datetime.datetime.strftime(new_date, '%d.%m.%Y')


def convert_from(score: str):
    new_score = score.split(" ")
    split_score = new_score[-1]
    final_score = split_score[0:4] + " " + split_score[4:6] + "**" + " " + "****" + split_score[12:16]
    split_name = new_score[:-1]
    big_name = ""
    for name in split_name:
        big_name += " " + name
    final_name_score = big_name + " " + final_score
    return final_name_score


def convert_to(score: str):
    new_score = score.split(" ")
    split_score = new_score[-1]
    final_score = "Счет" + " " + "**" + split_score[-4:]
    return final_score


final_date_list = []
final_description = []
final_from = []
final_to = []
final_amount = []
final_amount_name = []


def converted_five_operation():
    for operation in five_operations:
        new_data = convert_date(operation['date'])
        final_date_list.append(new_data)
        final_description.append(operation['description'])
        final_to.append(convert_to((operation['to'])))
        if 'Открытие вклада' in operation['description']:
            final_from.append("")
        else:
            final_from_1 = operation[list(operation.keys())[-2]]
            final_from_converted = convert_from(final_from_1)
            final_from.append(final_from_converted)
        final_amount.append(operation['operationAmount']['amount'])
        final_amount_name.append(operation['operationAmount']['currency']['name'])
    return None


def printed_five_operation():
    converted_five_operation()
    for op in range(0, 5):
        print(f"{final_date_list[op]} {final_description[op]}\n"
              f"{final_from[op]} -> {final_to[op]}\n"
              f"{final_amount[op]} {final_amount_name[op]}\n")



