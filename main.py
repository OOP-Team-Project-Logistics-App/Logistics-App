from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from commands.initialize_trucks import InitializeTrucksCommand

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

InitializeTrucksCommand(app_data).execute()
engine.start()


