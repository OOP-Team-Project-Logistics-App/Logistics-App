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

Creates routes, assigns trucks and packages by ids to them. Possible package routes are shown through the "searchroute" command so we can get information about which route is most suitable for our package delivery. Shows information about routes through the "viewroute" command.
```
createdeliveryroute 2/21/22 Brisbane Sydney Melbourne
createdeliveryroute 2/21/01 Sydney Melbourne Adelaide
createdeliveryroute 2/22/15 Perth Adelaide Melbourne Sydney Brisbane Darwin Alice_Springs
assigntrucktoroute 1
assigntrucktoroute 2
createdeliverypackage Sydney Melbourne 5500 test@email_1.com
createdeliverypackage Adelaide Sydney 6000 test@email_2.com
createdeliverypackage Perth Alice_Springs 3000 test@email_3.com
searchroute 1
assignpackagetoroute 1 1
viewroute 1
searchroute 2
searchroute 3
assignpackagetoroute 1 2
assignpackagetoroute 2 2
assignpackagetoroute 3 3
viewunassignedpackages
showavailabletrucks
assigntrucktoroute 3
assignpackagetoroute 2 3
assignpackagetoroute 3 3
getpackageinfo 2
packagestatus 2
updateday 9
packagestatus 2
packagestatus 3
viewallroutes
createdeliveryroute 4/21/9 Adelaide Sydney Brisbane Darwin
updateday 4
packagestatus 3
updateday 25
createdeliveryroute 3/21/6 Brisbane Sydney Melbourne
createdeliveryroute 4/21/9 Adelaide Sydney Brisbane Darwin
viewallroutes
showavailabletrucks
end
```

```
Route 1: Brisbane -> Sydney -> Melbourne created.
Route 2: Sydney -> Melbourne -> Adelaide created.
Route 3: Perth -> Adelaide -> Melbourne -> Sydney -> Brisbane -> Darwin -> Alice_Springs created.
Truck with id 1001 was assigned to route id 1.
Truck with id 1001 was assigned to route id 2.
Package with id 1 created. --
-- Accepted in city: Sydney --
-- Delivery to: Melbourne --
-- Weight: 5500kg --
-- Contact Info: test@email_1.com --
Package with id 2 created. --
-- Accepted in city: Adelaide --
-- Delivery to: Sydney --
-- Weight: 6000kg --
-- Contact Info: test@email_2.com --
Package with id 3 created. --
-- Accepted in city: Perth --
-- Delivery to: Alice_Springs --
-- Weight: 3000kg --
-- Contact Info: test@email_3.com --
Route found for package 1:
Route 1: Brisbane Feb 21st 22:00h -> Sydney Feb 22nd 08:26h -> Melbourne Feb 22nd 18:31h
Route 2: Sydney Feb 21st 01:00h -> Melbourne Feb 21st 11:04h -> Adelaide Feb 21st 19:24h
Package with id 1 was assigned to route 1.
Information about Route 1: 
Route 1: Brisbane Feb 21st 22:00h -> Sydney Feb 22nd 08:26h -> Melbourne Feb 22nd 18:31h 
Truck ID: 1001, Model: Scania, Capacity: 42000kg, Max range: 8000km 
Packages:
Package ID 1:
Sydney -> Melbourne
Weight: 5500kg
Contact info: test@email_1.com
Route found for package 2:
Route 3: Perth Feb 22nd 15:00h -> Adelaide Feb 23rd 23:00h -> Melbourne Feb 24th 07:20h -> Sydney Feb 24th 17:25h -> Brisbane Feb 25th 03:52h -> Darwin Feb 26th 19:15h -> Alice_Springs Feb 27th 12:27h
Route found for package 3:
Route 3: Perth Feb 22nd 15:00h -> Adelaide Feb 23rd 23:00h -> Melbourne Feb 24th 07:20h -> Sydney Feb 24th 17:25h -> Brisbane Feb 25th 03:52h -> Darwin Feb 26th 19:15h -> Alice_Springs Feb 27th 12:27h
Package with id 1 was assigned to route 2.
This route has no locations in the direction of Adelaide to Sydney
Route 3 has no assigned truck
Package ID: 2
Start Location: Adelaide
End Location: Sydney
Package ID: 3
Start Location: Perth
End Location: Alice_Springs
-------
Scania:
Available: 9 trucks, Unavailable: 1 trucks
-------
Man:
Available: 15 trucks, Unavailable: 0 trucks
-------
Actros:
Available: 15 trucks, Unavailable: 0 trucks
Truck with id 1026 was assigned to route id 3.
Package with id 2 was assigned to route 3.
Package with id 3 was assigned to route 3.
Package ID 2:
Adelaide -> Sydney
Weight: 6000kg
Contact info: test@email_2.com
Package 2 status is Pending.
Current day is now Feb 24th 20:26h.
Package 2 status is Delivered.
Package 3 status is En route.
Information about in-progress routes:
Route 3: Perth Feb 22nd 15:00h -> Adelaide Feb 23rd 23:00h -> Melbourne Feb 24th 07:20h -> Sydney Feb 24th 17:25h -> Brisbane Feb 25th 03:52h -> Darwin Feb 26th 19:15h -> Alice_Springs Feb 27th 12:27h
Truck ID: 1026, Model: Actros, Capacity: 26000kg, Max range: 13000km
Packages:
Package ID 2:
Adelaide -> Sydney
Weight: 6000kg
Contact info: test@email_2.com
Package ID 3:
Perth -> Alice_Springs
Weight: 3000kg
Contact info: test@email_3.com
Set off time cannot be more than 30 days in the future
Current day is now Feb 28th 20:26h.
Package 3 status is Delivered.
Current day is now Mar 24th 20:26h.
Set off time cannot be in the past
Route 4: Adelaide -> Sydney -> Brisbane -> Darwin created.
Information about in-progress routes:
-------
Scania:
Available: 10 trucks, Unavailable: 0 trucks
-------
Man:
Available: 15 trucks, Unavailable: 0 trucks
-------
Actros:
Available: 15 trucks, Unavailable: 0 trucks
```