import vk
from getpass import getpass


APP_ID = 6109461


def get_user_login():
    return input("print login: ")


def get_user_password():
    return getpass("print password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends, users'
    )
    api = vk.API(session)
    friends_adis = api.friends.getOnline()
    return api.users.get(user_ids=friends_adis)


def output_friends_to_console(friends_online):
    print("Here's list of your online friends: ")
    for friend_info in friends_online:
        print("{} {}".format(friend_info['first_name'], friend_info[
            'last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
