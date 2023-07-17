import datetime

from settings import five_operations



def convert_date(date: str) -> str:
    date_format = '%Y-%m-%dT%H:%M:%S.%f'
    new_date = datetime.datetime.strptime(date, date_format)
    return datetime.datetime.strftime(new_date, '%d.%m.%Y')


def convert_from(score):
    pass


def convert_to(score):
    pass



final_date_list = []
final_description = []
final_from = []
final_to = []
final_amount = []
final_amount_name = []

for operation in five_operations:
    new_data = convert_date(operation['date'])
    final_date_list.append(new_data)
    final_description.append(operation['description'])
    final_to.append(operation['to'])
    if 'Открытие вклада' in operation['description']:
        final_from.append("")
    else:
        final_from.append(operation[list(operation.keys())[-2]])
    final_to.append(operation['to'])
    final_amount.append(operation['operationAmount']['amount'])
    final_amount_name.append(operation['operationAmount']['currency']['name'])

for op in range(0, 5):
    print(f"{final_date_list[op]} {final_description[op]}\n"
          f"{final_from[op]} -> {final_to[op]}\n"
          f"{final_amount[op]} {final_amount_name[op]}\n")
