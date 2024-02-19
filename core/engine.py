from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory
        self.app_data = self._command_factory._app_data

    def start(self):
        self.app_data.load_system_state()
        while True:
            try:
                input_line = input()
                if input_line.lower() == "end":
                    self.app_data.save_system_state()
                    break
                command = self._command_factory.create(input_line)
                print(command.execute())
            except ValueError as e:
                print(e)