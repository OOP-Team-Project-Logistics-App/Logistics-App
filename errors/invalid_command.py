class InvalidCommand(Exception):
    def __init__(self, cmd: str):
        super().__init__(f"Command {cmd} is invalid.")