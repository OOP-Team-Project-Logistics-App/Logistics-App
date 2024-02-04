from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from models.truck import Truck


app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

engine.start()

#createdeliveryroute Sydney 10:10:01 Adelaide 10:10:21 Perth 10:12:21
#createdeliveryroute Sydney 10:10:01 Adelaide 10:10:11 Perth 10:12:21 throws error