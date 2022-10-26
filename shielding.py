class Email:
    def __init__(self, email: str = 'Anonymous', shield_character: str = 'x'):
        self.email = email
        self.shield_character = shield_character

    def __str__(self):
        return self.email

    def get_shield_email(self) -> str:
        return self.shielding()

    def shielding(self) -> str:
        dog_index = self.email.find('@')
        if dog_index == -1:
            print("Invalid email format")
            return ''

        return self.shield_character * dog_index + self.email[dog_index:]


class Number:
    def __init__(self, number: str = 'Number', shield_character: str = 'x', char_number_to_shielding: int = 3):
        self.number = number
        self.shield_character = shield_character
        self.char_number_to_shielding = char_number_to_shielding

    def __str__(self):
        return self.number

    def get_shield_number(self) -> str:
        return self.shielding()

    def shielding(self) -> str:
        format_number = ' '.join(self.number.split())
        current_char_number = self.char_number_to_shielding
        shield_number = ''
        for char in format_number[::-1]:
            if char.isdigit() and current_char_number > 0:
                shield_number += self.shield_character
                current_char_number -= 1
            else:
                shield_number += char

        return shield_number[::-1]


class Skype:
    def __init__(self, string_with_login: str = 'Anonymous'):
        self.string_with_login = string_with_login

    def __str__(self):
        return self.string_with_login

    def get_shield_login(self) -> str:
        return self.shielding()

    def shielding(self) -> str:
        if self.string_with_login.find('href') == -1:
            if self.string_with_login.find('skype:') != -1:
                return 'skype:xxx'
            else:
                print('Invalid login format')
                return ''
        else:
            login_start_index = self.string_with_login.find('skype')
            login_end_index = self.string_with_login.find('?')
            login = self.string_with_login[login_start_index: login_end_index]
            shield_ref = self.string_with_login.replace(login, 'skype:xxx')
            return shield_ref


if __name__ == '__main__':


    # test emails
    email_1 = Email()
    email_2 = Email("mail@mail.ru")
    email_3 = Email("yandex@yandex.ru", 'o')
    email_4 = Email("yandex.ru", 'x')
    email_5 = Email("gmail%gmail.ru", 'o')
    emails = [email_1, email_2, email_3, email_4, email_5]

    for email in emails:
        print(email.get_shield_email())

    # test numbers
    print()
    number_1 = Number('+7 666 777 888')
    number_2 = Number('  +7   666 777  888')
    number_3 = Number('+7 666 777 888', 'x', 7)
    number_4 = Number('+7 666 777   888', 'x', 20)
    number_5 = Number('+7 666 777  888', 'x', -1)
    number_6 = Number('+7 666 777  888', 'x', 0)

    numbers = [number_1, number_2, number_3, number_4, number_5, number_6 ]
    for number in numbers:
        print(number.get_shield_number())

    # test skype
    print()
    login_1 = Skype('skype:alex.max')
    login_2 = Skype(r'<a href=\"skype:xxx?call\">skype</a>')
    login_3 = Skype('alex.max')
    login_4 = Skype('sype:alex.max')

    logins = [login_1, login_2, login_3, login_4]

    for login in logins:
        print(login.get_shield_login())
