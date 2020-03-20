from .base import Base


class Replicas(Base):
    """Replicas Class"""

    @property
    def run(self):

        import requests
        from environs import Env

        env = Env()
        env.read_env()
        API = env.str("API")
        auth_username = env.str("auth_username")
        auth_password = env.str("auth_password")

        if self.options['read']:
            if self.options['--clone']:
                response = requests.get(API + "clouds/replicas/retrieve/%s" % self.options['--clone'], auth=(auth_username,auth_password))
                print(response.status_code, response.content.decode())
            else:
                response = requests.get(API + "clouds/replicas", auth=(auth_username, auth_password))
                print(response.status_code, response.content.decode())

        if self.options['scale']:
                data = {'scale_number': str(self.options['<final_number>'])}
                response = requests.post(API + "clouds/replicas/%s" % self.options['<clone_id>'], auth=(auth_username, auth_password),
                                         data=data)
                print(response.status_code, response.content.decode())


