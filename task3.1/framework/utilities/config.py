from framework.utilities.fileUtil import JsonUtil


class ConfigManager:

    @classmethod
    def load_browser_config(cls):
        config = JsonUtil.load_data('./task3.1/toolsQAProject/config.json')
        return config
