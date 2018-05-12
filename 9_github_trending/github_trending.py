import requests
import datetime


def get_trending_repositories(top_size):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    search_queque = 'created:>' + week_ago.isoformat()
    payload = {'q':search_queque,'sort':'stars', 'per_page':top_size}
    rep_response = requests.get(
        'https://api.github.com/search/repositories', params=payload)
    return rep_response.json()['items']


def get_open_issues_amount(repo_owner, repo_name):
    rep_responce = \
        requests.get('https://api.github.com/repos/{}/{}/issues'.format(
            repo_owner, repo_name))
    issues = rep_responce.json()
    return len([issue for issue in issues if 'pull_request' not in issue])


def check_rep_for_pull_requests(rep_list):
    checked_reps = rep_list
    for repository in checked_reps:
        repository['open_issues'] = get_open_issues_amount(
            repository['owner']['login'], repository['name'])
    return checked_reps


def print_rep_info(repos):
    for rep in repos:
        what_to_print = [str(rep['open_issues']), rep['name'],
                         rep['html_url']]
        print(" ".join(what_to_print))


def input_rep_amount():
    users_input = input("print how much top repositories you "
                            "need (less then 100): \n")
    amount_of_top_rep = 0
    try:
        amount_of_top_rep = int(users_input)
    except ValueError:
        print('{} is not a number'.format(users_input))
        users_input = None
    if amount_of_top_rep < 0:
        print("number must be positive")
        users_input = None
    elif amount_of_top_rep > 100:
        print("number must be less then 100")
        users_input = None
    return users_input


if __name__ == '__main__':
    amount_of_top_rep = input_rep_amount()
    if not amount_of_top_rep:
        exit()
    trending_repos = get_trending_repositories(amount_of_top_rep)
    checked_trending = check_rep_for_pull_requests(trending_repos)
    print_rep_info(checked_trending)
