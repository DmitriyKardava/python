class Worker:
    name = ''
    surname = ''
    position = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def get_full_name(self):
        return str.strip(self.surname + ' ' + self.name)

    def get_total_income(self):
        return self.position.get('wage') + self.position.get('bonus')


employer = Position()
print(f"Сотрудник: {employer.get_full_name()}")
print(f"Доход: {employer.get_total_income()}")
employer.name = 'Иван'
employer.surname = 'Иванов'
employer.position['wage'] = 100
employer.position['bonus'] = 50
print(f"Сотрудник: {employer.get_full_name()}")
print(f"Доход: {employer.get_total_income()}")
