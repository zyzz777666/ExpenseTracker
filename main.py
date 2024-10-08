from Handlers.handlers import Tracker
from RecordOutput.handlersFile import Convert


def main():
    Convert.output_files('asdasd')

    while True:
        print("""
            1 - Добавить рассходы
            2 - Изменить расскаходы
            3 - Удалить рассходы
            4 - Показать все рассходы
            5 - Показать сумму расходов
            6 - Показать сумму расходов за опеределенный месяц этого года
            q - Завершить и сохранить
            s - Сохранить
            """)
        start = input('ss: ')

        if start == '1':
            Tracker.add_spense(input('Введите категорию: '),
                               int(input('Введите сумму: ')),
                               input('Введите описание: '))
        elif start == '2':
            Tracker.update_spense(int(input('Введите [ID]: ')),
                                  input('Введите новую категорию расходов: '),
                                  int(input('Введите новую сумму расходов: ')),
                                  input('Введите новое описание: '))
        elif start == '3':
            Tracker.del_spense(input('Введите [ID] категории которую хотите удалить: '))
        elif start == '4':
            print(f'ID\t\t\tСумма\t\t\tОписание\t\t\tКатегория')
            Tracker.show_spense()
        elif start == '5':
            print(Tracker.show_summary_expense())
        elif start == '6':
            print(Tracker.show_summary_month_expense(input('Введите месяц в строковом виде: ')))
        elif start == 's':
            Convert.record_files('asdasd')
        elif start == 'q':
            Convert.record_files('asdasd')
            break


if __name__ == '__main__':
    main()
