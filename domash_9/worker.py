class Worker:

    def __init__(self, name, surname, wage= 80, bonus= 40):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def full_name(self):
        full_names = self.name + ' ' + self.surname
        print(f"полное имя: {full_names}")

    def full_salary(self):
        full_salarys = self._income['wage'] + self._income['bonus']
        print(f"доход с учетом премии: {full_salarys}")


E_bab = Position('Евгений', 'Бабенко', 200, 50)

E_bab.full_name()
E_bab.full_salary()


D_lih = Position('Даниил', 'Лихвостьев', 170, 33)

D_lih.full_name()
D_lih.full_salary()

N_tar = Position('Нарзан', 'Тарасков', 300, 70)

N_tar.full_name()
N_tar.full_salary()