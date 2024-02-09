# Logistics-App

Teamwork in Python OOP Module in Telerik Academy

**Logistics App** is an application aiming to expand an Australian company's activities to the freight industry. The app is going to be used to manage the delivery of packages between hubs in major Australian cities.

**Contributors:**

|       Name            |                   Github Username                 |
|:---------------------:|:-------------------------------------------------:|
| Valentin Penev        | [FalseBeliefs](https://github.com/FalseBeliefs)   |
| Konstantin Ivanov     | [dnrubinart](https://github.com/dnrubinart)       |
| Radostin Mihaylov     | [radoooo11](https://github.com/radoooo11)         |


## **TEMPORARY INPUT AND OUTPUT FOR TESTS**

Creates routes, assigns trucks and packages by ids to them. Shows information about routes through the "viewroute" command.
```
createdeliveryroute 2/19/21 Brisbane Sydney Melbourne
createdeliveryroute 2/19/21 Sydney Melbourne Adelaide
createdeliveryroute 2/19/21 Perth Adelaide Melbourne Sydney Brisbane Darwin Alice_Springs
assigntrucktoroute 1
createdeliverypackage Sydney Melbourne 5500 0412345678
searchroute 1
assignpackagetoroute 1 1
assigntrucktoroute 2
assigntrucktoroute 3
createdeliverypackage Adelaide Darwin 6000 0512345678
createdeliverypackage Perth Sydney 3000 0512345678
assignpackagetoroute 2 3
assignpackagetoroute 3 3
viewroute 1
viewroute 2
viewroute 3
end
```

```
Route 1: Brisbane -> Sydney -> Melbourne created.
Route 2: Sydney -> Melbourne -> Adelaide created.
Route 3: Perth -> Adelaide -> Melbourne -> Sydney -> Brisbane -> Darwin -> Alice_Springs created.
Truck with id 1001 was assigned to route id 1.
Package with id 1 created. --
-- Accepted in city: Sydney --
-- Delivery to: Melbourne --
-- Weight: 5500kg --
-- Contact Info: 0412345678 --
Route found for package 1: Route 1: Brisbane (Feb 19th 21:00h) -> Sydney (Feb 20th 07:26h) -> Melbourne (Feb 20th 17:31h)
Route found for package 1: Route 2: Sydney (Feb 19th 21:00h) -> Melbourne (Feb 20th 07:04h) -> Adelaide (Feb 20th 15:24h)
Package with id 1 was assigned to route 1.
Truck with id 1002 was assigned to route id 2.
Truck with id 1026 was assigned to route id 3.
Package with id 2 created. --
-- Accepted in city: Adelaide --
-- Delivery to: Darwin --
-- Weight: 6000kg --
-- Contact Info: 0512345678 --
Package with id 3 created. --
-- Accepted in city: Perth --
-- Delivery to: Sydney --
-- Weight: 3000kg --
-- Contact Info: 0512345678 --
Package with id 2 was assigned to route 3.
Package with id 3 was assigned to route 3.
Information about Route 1: 
Route 1: Brisbane (Feb 19th 21:00h) -> Sydney (Feb 20th 07:26h) -> Melbourne (Feb 20th 17:31h) 
Truck ID: 1001, Model: Scania, Capacity: 42000kg, Max range: 8000km 
Packages:
Package ID 1:
Sydney -> Melbourne
Weight: 5500kg
Contact info: 0412345678
Information about Route 2: 
Route 2: Sydney (Feb 19th 21:00h) -> Melbourne (Feb 20th 07:04h) -> Adelaide (Feb 20th 15:24h) 
Truck ID: 1002, Model: Scania, Capacity: 42000kg, Max range: 8000km 
Packages:
No packages assigned to this route.
Information about Route 3: 
Route 3: Perth (Feb 19th 21:00h) -> Adelaide (Feb 21st 05:00h) -> Melbourne (Feb 21st 13:20h) -> Sydney (Feb 21st 23:25h) -> Brisbane (Feb 22nd 09:52h) -> Darwin (Feb 24th 01:15h) -> Alice_Springs (Feb 24th 18:27h) 
Truck ID: 1026, Model: Actros, Capacity: 26000kg, Max range: 13000km 
Packages:
Package ID 2:
Adelaide -> Darwin
Weight: 6000kg
Contact info: 0512345678
Package ID 3:
Perth -> Sydney
Weight: 3000kg
Contact info: 0512345678
```