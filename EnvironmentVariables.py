from wox import Wox
from os import environ
import subprocess


class EnvironmentVariables(Wox):

    def search_environment_variables(self, user_input):
        env_vars = []
        for k, v in environ.items():
            if (k.lower().startswith(user_input.lower())):
                env_vars.append({
                    'Title': f"{k}",
                    'SubTitle': f"{v}",
                    'IcoPath': 'Images/pic.png',
                    'JsonRPCAction': {
                        'method': 'action',
                        'parameters': [f"{k}={v}"],
                        'dontHideAfterAction': False
                    }
                })

        return env_vars

    def query(self, user_input):
        if not user_input:
            env_vars = []
            for k, v in environ.items():
                env_vars.append({
                    'Title': f"{k}",
                    'SubTitle': f"{v}",
                    'IcoPath': 'Images/pic.png',
                    'JsonRPCAction': {
                        'method': 'action',
                        'parameters': [f"{k}={v}"],
                        'dontHideAfterAction': False
                    }
                })

            return env_vars

        if user_input.startswith('-s'):
            pass

        return self.search_environment_variables(user_input)

    def action(self, env_var):
        subprocess.check_call(f"echo {env_var}|clip", shell=True)

if __name__ == '__main__':
    EnvironmentVariables()
