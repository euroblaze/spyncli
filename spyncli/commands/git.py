from .base import Base


class Git(Base):
    """Git Class"""

    @property
    def run(self):

        import requests
        import os
        from environs import Env

        env = Env()
        env.read_env()
        API = env.str("API")
        auth_username = env.str("auth_username")
        auth_password = env.str("auth_password")

        if self.options['read']:
            if not self.options['--name'] and not self.options['--id'] and not self.options['--conf']:
                response = requests.get(API + "git/",
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            elif self.options['--name']:
                response = requests.get(API + "git/%s" % self.options['--name'],
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            elif self.options['--id']:
                response = requests.get(API + "git/id/%s" % self.options['--id'],
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())
            elif self.options['--conf']:
                response = requests.get(API + "git/config_set_id/%s" % self.options['--conf'],
                                        auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())

        if self.options['update']:
            data = {}
            if self.options['--url']:
                data['url'] = self.options['--url']
            if self.options['--usr']:
                data['username'] = self.options['--usr']
            if self.options['--pwd']:
                data['password'] = self.options['--pwd']
            if self.options['--b']:
                data['branch'] = self.options['--b']
            if self.options['--name']:
                data['module'] = self.options['--name']
            response = requests.put(API + "git/%s" % self.options['<id>'],
                                    auth=(auth_username, auth_password),
                                    data=data)
            print(response.status_code, response.content.decode())

        if self.options['delete']:
            response = requests.delete(API + "git/%s" % self.options['<id>'],
                                       auth=(auth_username, auth_password))
            print(response.status_code, response.content.decode())

        if self.options['create']:
            data = {}
            data['url'] = self.options['<git_url>']
            data['username'] = self.options['<username>']
            data['password'] = self.options['<password>']
            data['branch'] = self.options['<branch>']
            data['module'] = self.options['<module_name>']
            response = requests.post(API + "git/insert/%s" % self.options['<configset_id>'],
                                     auth=(auth_username, auth_password),
                                     data=data)
            print(response.status_code, response.content.decode())

        if self.options['check']:
           data = {'url': self.options['<git_url>'],
                   'username': self.options['<username>'],
                   'password': self.options['<password>'],
                   'branch': self.options['<branch>'],
                   'module': self.options['<module_name>']}
           response = requests.post(API + "git/git_module/check_git_creds",
                                    auth=(auth_username, auth_password),
                                    data=data)
           print(response.status_code, response.content.decode())
