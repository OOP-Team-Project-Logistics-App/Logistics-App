from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory
        self.app_data = self._command_factory._app_data

    def start(self):
        output = []
        # self.app_data.load_system_state() TEMPORARY OUT OF USE SO WE CAN TEST CODE
        while True:
            try:
                input_line = input()
                if input_line.lower() == "end":
                    # self.app_data.save_system_state() TEMPORARY OUT OF USE SO WE CAN TEST CODE
                    break
                command = self._command_factory.create(input_line)
                output.append(command.execute())
            except ValueError as e:
                output.append(e.args[0])

        print("\n".join(output))