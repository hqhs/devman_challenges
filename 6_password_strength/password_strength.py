import re


def check(password, pattern):
    if re.fullmatch(pattern, password):
        return 0
    else:
        return 1


def check_for_re_patterns(password):
    patterns = [
            '[0-9]*\Z',
            '[a-zA-Z]*\Z',
            '[^@]+@[^@]+\.[^@]+',
            '[^0-9a-zA-Z]*\Z'
    ]
    points = 0
    for pattern in patterns:
        points += check(password, pattern)
    return points


def lenght_check(password):
    if len(password) < 8:
        return 1
    elif len(password) < 10:
        return 1.5
    elif len(password) < 16:
        return 2
    else:
        return 2.5


def most_common_check(password):
    ten_most_popular_passwords = ["password", "12345678", "qwertyui",
                                  "123456789", "baseboll", "football",
                                  "qwertyuiop", "1234567890",
                                  "superman", "1qaz2wsx"]
    if password in ten_most_popular_passwords:
        return 0
    else:
        return 1


def get_password_strength(password):
    passw_str = 1 + lenght_check(password) * most_common_check(password) \
                                            * check_for_re_patterns(password)
    if passw_str > 10:
        passw_str = 10
    return passw_str


if __name__ == '__main__':
    password = input("Print your password: ")
    print("Strength of your password is: \n", get_password_strength(password))
