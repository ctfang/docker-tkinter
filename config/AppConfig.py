class AppConfig:
    def __init__(self):
        self.data = {
            'title': "docker管理"
        }

    def get(strKey):
        config = AppConfig();
        return config.data[strKey]
