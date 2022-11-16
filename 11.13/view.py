

class CLIView:
    @staticmethod
    def get_email():
        return input('Введите Ваш e-mail: ')

    @staticmethod
    def incorrect_email():
        raise ValueError("Введён некорректный e-mail адресс.")

    @staticmethod
    def correct_email():
        return ("Ваш e-mail адресс успешно сохранён.")

# print(CLIView.get_email())




