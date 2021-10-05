class Data:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def date_str_to_int(cls, date_str):
        date_list = (date_str.split('-'))
        for i in range(len(date_list)):
            date_list[i] = int(date_list[i])
        return date_list

    @staticmethod
    def date_valid(date_list):
        if len(date_list) != 3:
            return False
        if date_list[0] < 1 or date_list[0] > 31:
            return False
        if date_list[1] < 1 or date_list[0] > 12:
            return False
        if date_list[2] < 1900 or date_list[0] > 9000:
            return False
        return True


for _d in ['01-01-2001', '02-02-2002', '03-03-2003', '44-55-2000']:
    print(Data(_d).date_str)
    print(Data.date_str_to_int(_d))
    print(Data.date_valid(Data.date_str_to_int(_d)))
    print()
