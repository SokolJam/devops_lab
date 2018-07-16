import argparse
import getpass
import setting
import sys


import requests


class InfoClient(object):
    def __init__(self, user, password):
        self.username = user
        self.password = password
        self.url = setting.GITHUB_API.replace(':user', self.username)

    def info_response(self, url):
        response = requests.get(url, auth=(self.username,
                                           self.password)).json()
        return response


class PrStats(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = []
        self.user = None
        self.add_count = 0
        self.password = ''
        self.username = ''
        self.base_action_dict = {'info': self.info, 'version': self.version,
                                 'username': self.credentials}
        self.options_dict = {'base': self.base_info, 'repos': self.repos_info,
                             'add': self.lines, 'delete': self.lines,
                             'repo': self.repo}

    def get_parameters(self):
        self.parser.add_argument('-v', '--version',
                                 help='show the version of program',
                                 action='store_true')
        self.parser.add_argument('-i', '--info',
                                 help='information about the program',
                                 action='store_true')
        self.parser.add_argument('username',
                                 help='take user name, use with [-b][-rs][-r]'
                                      '[-a][-d]', nargs='?')
        self.parser.add_argument('-b', '--base',
                                 help='show the base information about user',
                                 action='store_true')
        self.parser.add_argument('-rs', '--repos',
                                 help='list available user\'s repositories ',
                                 action='store_true')
        self.parser.add_argument('-r', '--repo', type=str,
                                 help='repositories information, '
                                      'use with -a, -d')
        self.parser.add_argument('-a', '--add',
                                 help='number of added lines, use with -r',
                                 action='store_true')
        self.parser.add_argument('-d', '--delete',
                                 help='number of deleted lines, use with -r',
                                 action='store_true')
        self.args = self.parser.parse_args()

        for key in self.base_action_dict.keys():
            if self.args.__dict__[key]:
                self.base_action_dict[key]()
                break
        else:
            print('You have to input <username> for Github.com. '
                  'Try again "pr-stats.py <username>"')
            sys.exit()
        for option in self.options_dict.keys():
            if self.args.__dict__[option] is True:
                self.options_dict[option]()
            elif option == 'repo' and self.args.repo:
                self.options_dict[option]()

    @staticmethod
    def info():
        print(setting.INFO)

    @staticmethod
    def version():
        print('Current version:', setting.VERSION)

    @staticmethod
    def print_info(data_dict, info_list):
        for keys in data_dict.keys():
            if keys in info_list:
                print(keys, ':', data_dict[keys])
            elif keys == 'parent':
                print('---parent---\nowner :',
                      data_dict[keys]['owner']['login'])
                for parent_key in data_dict[keys]:
                    if parent_key in ['full_name', 'forks', 'open_issues',
                                      'id']:
                        print(parent_key, ':', data_dict[keys][parent_key])

    def credentials(self):
        self.username = self.args.username
        self.password = getpass.getpass(prompt='Enter your password: ')
        self.user = InfoClient(self.username, self.password)

    def base_info(self):
        data = self.user.info_response(self.user.url)
        print('Base %s information:' % self.username)
        self.print_info(data, ['created_at', 'email', 'location', 'name',
                               'public_repos', 'total_private_repos'])

    def repos_info(self):
        data = self.user.info_response('%s/repos' % self.user.url)
        print('Information about all repositories of user', self.username)
        for i in data:
            self.print_info(i, ['name', 'private', 'description', 'fork',
                                'url', 'created_at', 'pushed_at',
                                'clone_url'])
            print('------------------')

    def repo(self):
        if not self.args.add and not self.args.delete:
            url = setting.GITHUB_API_REPO.replace(':user', self.username)
            data = self.user.info_response(url.replace(':repo',
                                                       self.args.repo))
            print('Information about repository - ', self.args.repo)
            self.print_info(data, ['private', 'description', 'fork', 'url',
                                   'created_at', 'pushed_at', 'id',
                                   'clone_url', 'updated_at', 'permissions'])

    def lines(self):
        if not self.args.repo:
            print('You have to input <repo>! '
                  'Try "python pr-stats.py -a -r <repo>"')
            sys.exit()
        url = setting.GITHUB_API_COUNT.replace(':user', self.username)
        data = self.user.info_response(url.replace(':repo', self.args.repo))
        if self.args.delete:
            choose = ['d', 'deleted from']
        else:
            choose = ['a', 'added to']
        for index in data[0]['weeks']:
            self.add_count += index[choose[0]]
        print('Number of lines %s repository %s:'
              % (choose[1], self.args.repo), self.add_count)


if __name__ == '__main__':
    stat = PrStats()
    stat.get_parameters()
