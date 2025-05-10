import os

from dotenv import dotenv_values
from rich.pretty import pprint


def find_root_path(start_path=None, root_marker='.projectroot'):
    """
    Find the root path of the project by searching for a root marker file.

    :param start_path: The path to start searching from. Defaults to the current working directory.
    :param root_marker: The name of the file that marks the root directory.
    :return: The absolute path of the root directory, or None if not found.
    """
    if start_path is None:
        start_path = os.getcwd()

    current_path = os.path.abspath(start_path)

    while True:
        if os.path.exists(os.path.join(current_path, root_marker)):
            return current_path

        parent_path = os.path.dirname(current_path)
        if parent_path == current_path:  # Reached the filesystem root
            return None

        current_path = parent_path


class EnvValue(object):
    @staticmethod
    def initLangsmith():
        env = EnvValue.get_env_o()
        os.environ["LANGSMITH_TRACING"] = env['LANGSMITH_TRACING']
        os.environ["LANGSMITH_ENDPOINT"] = env['LANGSMITH_ENDPOINT']
        os.environ["LANGSMITH_API_KEY"] = env['LANGSMITH_API_KEY']
        os.environ["LANGSMITH_PROJECT"] = env['LANGSMITH_PROJECT']
        # OPENAI_API_KEY
        os.environ["OPENAI_API_KEY"] = EnvValue.get_open_ai_key()

    @staticmethod
    def get_env_o():
        # ROOT_DIR = os.path.dirname(os.path.abspath("../"))
        # ROOT_DIR = os.path.dirname(os.path.abspath("../"))
        ROOT_DIR = find_root_path()
        # pprint(ROOT_DIR)
        final_path = ROOT_DIR + '/.env'
        # pprint(final_path)
        config = dotenv_values(final_path)

        if config is None or len(config.keys()) == 0:
            # pprint('use environ')
            return os.environ
        else:
            # pprint('use .env')
            return config

    @staticmethod
    def gte_flyqueque_api_uuid():
        env = EnvValue.get_env_o()
        return env['FLY_QUEQUE_API_UUID']

    @staticmethod
    def get_google_ai_key():
        env = EnvValue.get_env_o()
        return env['google_ai_key']

    @staticmethod
    def get_open_ai_key():
        env = EnvValue.get_env_o()
        return env['open_ai_key']

    @staticmethod
    def get_neo4j_uri():
        env = EnvValue.get_env_o()
        return env['NEO4J_URI']

    @staticmethod
    def get_neo4j_username():
        env = EnvValue.get_env_o()
        return env['NEO4J_USERNAME']

    @staticmethod
    def get_neo4j_password():
        env = EnvValue.get_env_o()
        return env['NEO4J_PASSWORD']

    @staticmethod
    def get_flyqueque_domain():
        env = EnvValue.get_env_o()
        return env['FLYQUEQUE_API_DOMAIN']

    @staticmethod
    def get_geo_api_key():
        env = EnvValue.get_env_o()
        return env['geo_api_key']

    @staticmethod
    def get_GOOGLE_PLACE_API_TOKEN():
        env = EnvValue.get_env_o()
        return env['GOOGLE_PLACE_API_TOKEN']

    @staticmethod
    def get_aws_access_key():
        env = EnvValue.get_env_o()
        return env['AWS_ACCESS_KEY']

    @staticmethod
    def get_aws_secret_key():
        env = EnvValue.get_env_o()
        return env['AWS_SECRET_KEY']
