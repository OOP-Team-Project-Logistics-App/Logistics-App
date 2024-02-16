from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from commands.initialize_trucks import InitializeTrucksCommand

app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)

InitializeTrucksCommand(app_data).execute()
engine.start()

"""
createdeliveryroute 2/16/20 Brisbane Sydney Melbourne Adelaide Alice_Springs Darwin Perth
createdeliverypackage Sydney Melbourne 25000 test1@asd.dsa  
createdeliverypackage Melbourne Alice_Springs 5000 test2@asd.dsa
createdeliverypackage Alice_Springs Perth 25500 test3@asd.dsa
createdeliverypackage Alice_Springs Darwin 500 test4@asd.dsa
viewunassignedpackages
assigntrucktoroute 1
assignpackagetoroute 1 1
assignpackagetoroute 2 1
assignpackagetoroute 3 1
assignpackagetoroute 4 1
updateday 1
packagestatus 1
updateday 2
packagestatus 1
packagestatus 2
viewallroutes
packagestatus 3
packagestatus 4 
showavailabletrucks
updateday 1
packagestatus 4
showavailabletrucks
createdeliveryroute 2/21/11 Brisbane Sydney Melbourne Adelaide Alice_Springs Darwin Perth
assigntrucktoroute 2
assignpackagetoroute 4 1
createdeliverypackage Sydney Alice_Springs 5000 test5@asd.dsa
assignpackagetoroute 5 1
packagestatus 4
packagestatus 5
updateday 2
packagestatus 4
packagestatus 5
end
"""

"""
createdeliveryroute 2/16/11 Brisbane Sydney Melbourne Adelaide Alice_Springs Darwin Perth
assigntrucktoroute 1
createdeliverypackage Brisbane Melbourne 30000 test5@asd.dsa
createdeliverypackage Adelaide Darwin 7000 test5@asd.da
assignpackagetoroute 1 1
assignpackagetoroute 2 1
updateday 2
createdeliverypackage Darwin Perth 29999 test@asd.dsa
assignpackagetoroute 3 1
viewallroutes
end
"""