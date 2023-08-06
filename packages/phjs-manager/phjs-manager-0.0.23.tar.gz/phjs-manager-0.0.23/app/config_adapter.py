from ConfigParser import RawConfigParser

class ConfigAdapter:
    config = RawConfigParser()
    sections = []
    data = {}
    """Adapter for config file"""
    def __init__(self, path):
        self.config.read(path)
        self.sections = self.config.sections()
        options = self.config.options(self.sections[0])
        for option in options:
            try:
                self.data[option] = self.config.getint(self.sections[0], option)
                if self.data[option] == -1:
                    print("skip:" + option)
            except:
                try:
                    self.data[option] = self.config.get(self.sections[0], option)
                except:
                    print("exception on " + option)
                    self.data[option] = None


    def get_socket_path(self):
        return self.data['socket_path']

    def get_container(self):
        return self.data['container']

    def get_run_command(self):
        return self.data['run_command']

    def get_start_port(self):
        return self.data['start_port']

    def get_bind_port(self):
        return self.data['bind_port']