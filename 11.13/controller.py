from typing import List
import view


class Application:
    """Сохраняет e-mail адреса пользователей и выводит сообщение об успешной или некорректной записи"""
    def save_email(self):
        import model
        for user in users:
            SE1 = model.Email(user)
            SE1.save()
            print(view.CLIView.correct_email())

    def loop(self) -> List[str]:
        users = []
        while user := view.CLIView.get_email():
            users.append(user)
        return users


App = Application()
users = App.loop()
App.save_email()
