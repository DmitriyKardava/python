class OrgUnitError(Exception):
    def __init__(self, *args):
        if args:
            self.msg = args[0]

    def __str__(self):
        return f'Отдел {self.msg} не найден'


class Storage:
    inv_number = 0
    items = {}
    org_units = {'Склад', 'Бухгалтерия', 'Отдел продаж', 'Руководство'}

    @classmethod
    def add_to_storage(cls, office_equipment):
        cls.inv_number += 1
        cls.items.setdefault(office_equipment, [cls.inv_number, 'Склад'])

    @classmethod
    def move_to_org_unit(cls, office_equipment, org_unit):
        if org_unit not in cls.org_units:
            raise OrgUnitError(org_unit)
        if cls.items.get(office_equipment)[1] == 'Склад':
            cls.items[office_equipment][1] = org_unit

    @classmethod
    def show_org_unit(cls, org_unit):
        print(f'{org_unit}:')
        for item in cls.items:
            ou = cls.items.get(item)[1]
            if ou == org_unit:
                print(item.group, item.vendor, item.model)
        print()


class OfficeEquipment:
    __req_values = ('vendor', 'model', 'purchase_date')

    def __init__(self, vendor, model, purchase_date):
        self.vendor = vendor
        self.model = model
        self.purchase_date = purchase_date
        self.group = self.__class__.__name__

    def __setattr__(self, key, value):
        if key in self.__req_values and not value:
            raise AttributeError(f'Не указано значение {key}')
        object.__setattr__(self, key, value)

    @staticmethod
    def check_date(date_str):
        if date_str.count('.') == 2:
            day, month, year = map(int, date_str.split('.'))
            return day <= 31 and month <= 12 and year <= 3999


class Printer(OfficeEquipment):
    def __init__(self, print_type, paper_size, vendor, model, purchase_date):
        self.print_type = print_type
        self.paper_size = paper_size
        super().__init__(vendor, model, purchase_date)


class Scanner(OfficeEquipment):
    def __init__(self, scan_type, paper_size, vendor, model, purchase_date):
        self.scan_type = scan_type
        self.paper_size = paper_size
        super().__init__(vendor, model, purchase_date)


class Copier(OfficeEquipment):
    def __init__(self, paper_size, vendor, model, purchase_date):
        self.paper_size = paper_size
        super().__init__(vendor, model, purchase_date)


scanner1 = Scanner('Планшетный', 'A4', 'Epson', 'Perfection V19', '05.10.2021')
scanner2 = Scanner('Протяжный', 'A4', 'Plustek', 'SmartOffice PS186', '05.10.2021')
scanner3 = Scanner('Протяжный', 'A4', 'Kodak', 'Alaris E1025', '05.10.2021')
printer1 = Printer('Струйный', 'A4', 'Canon', 'PIXMA TS304', '05.10.2021')
printer2 = Printer('Струйный', 'A4', 'HP', 'OfficeJet Pro 6230', '05.10.2021')
printer3 = Printer('Лазерный', 'A4', 'Lexmark', 'B2236dw', '05.10.2021')
printer4 = Printer('Лазерный', 'A4', 'HP', 'Laser 107r', '05.10.2021')
printer5 = Printer('Лазерный', 'A4', 'Brother', 'HL-1110R', '05.10.2021')
Storage.add_to_storage(scanner1)
Storage.add_to_storage(scanner2)
Storage.add_to_storage(scanner3)
Storage.add_to_storage(printer1)
Storage.add_to_storage(printer2)
Storage.add_to_storage(printer3)
Storage.add_to_storage(printer4)
Storage.add_to_storage(printer5)
Storage.move_to_org_unit(scanner2, 'Бухгалтерия')
Storage.move_to_org_unit(printer2, 'Бухгалтерия')
Storage.show_org_unit('Бухгалтерия')
Storage.show_org_unit('Склад')
