from RecordOutput.handlersFile import Convert
from datetime import datetime


class Config:
    @staticmethod
    def length():
        if len(Convert.data) == 0:
            print('У вас нет расходов')


class Tracker:

    @staticmethod
    def add_spense(category: str, amount: int, desc: str):
        if isinstance(amount, int) and isinstance(desc, str) and isinstance(category, str):
            for index in range(len(Convert.data) + 1):
                if str(index) not in Convert.data:
                    Convert.data[str(index)] = {'amount': amount,
                                                'desc': desc,
                                                'time': datetime.now().strftime("%B"),
                                                'category': category}

                    print(f'Рассходы добавлены, ID: {index}')
        else:
            raise TypeError

    @staticmethod
    def update_spense(id: int, new_category: str, new_amount: int, new_desc: str):
        if id not in Convert.data or not isinstance(id, int):
            raise ValueError
        Convert.data[id] = {'amount': new_amount,
                            'desc': new_desc,
                            'category': new_category}

    @staticmethod
    def del_spense(id: str):
        if id not in Convert.data or not isinstance(id, str):
            raise ValueError
        del Convert.data[id]

    @staticmethod
    def show_spense():
        if len(Convert.data) > 0:
            for i in Convert.data:
                print(
                    f'{i}\t\t\t{Convert.data[i]["amount"]}\t\t\t{Convert.data[i]["desc"]}\t\t\t{Convert.data[i]["category"]}')
        else:
            Config.length()

    @staticmethod
    def show_summary_expense():
        count = 0

        if len(Convert.data) > 0:
            for sum in Convert.data:
                count += Convert.data[str(sum)]['amount']
        else:
            Config.length()

        print(count)

    @staticmethod
    def show_summary_month_expense(month: str):
        count = 0

        if len(Convert.data) > 0:
            for i in Convert.data:
                if Convert.data[str(i)]['time'] == month:
                    count += Convert.data[str(i)]['amount']
        else:
            Config.length()

        return count
