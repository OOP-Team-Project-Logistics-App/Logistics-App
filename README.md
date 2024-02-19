# Logistics-App

Teamwork in Python OOP Module in Telerik Academy

**Logistics App** is an application aiming to expand an Australian company's activities to the freight industry. The app is going to be used to manage the delivery of packages between hubs in major Australian cities.

**Contributors:**

|       Name            |                   Github Username                 |
|:---------------------:|:-------------------------------------------------:|
| Valentin Penev        | [FalseBeliefs](https://github.com/FalseBeliefs)   |
| Konstantin Ivanov     | [dnrubinart](https://github.com/dnrubinart)       |
| Radostin Mihaylov     | [radoooo11](https://github.com/radoooo11)         |

## Features

> [!NOTE]
> Before testing the features, ensure that you are logged into one of the three accounts: employee, supervisor, or manager. Each account has different permissions, allowing you to thoroughly test the functionality. After testing with one account, make sure to log out before logging into another account.

**Create delivery route** - creates a delivery route with an unique id and at least two locations. It takes departure time in the format of month/day/hour and locations.
```py
login Employee Epassword
createdeliveryroute 2/21/6 Brisbane Sydney Melbourne
createdeliveryroute 2/21/8 Sydney Melbourne Adelaide
```
**Create delivery package** - creates a delivery package with a unique id. It takes as parameters a pick-up location and delivery location, weight in kilograms, and the customer's contact information.
```py
login Employee Epassword
createdeliverypackage Sydney Melbourne 45 test@email.com
```
**Search route** - searches for a suitable route for the package based on the package's pick-up and delivery locations. It takes the package id as parameter and returns the available routes with their respective departure or arrival times at each location.
```py
login Employee Epassword
createdeliveryroute 2/21/6 Brisbane Sydney Melbourne
createdeliveryroute 2/21/8 Sydney Melbourne Adelaide
createdeliverypackage Sydney Melbourne 45 test@email.com
searchroute 1
```
**Assign truck to route** - automatically finds and assigns an available and suitable truck to a route according to the route's total distance. It takes route id as parameter.
```py
login Employee Epassword
createdeliveryroute 2/21/6 Alice_Springs Adelaide Melbourne Sydney Brisbane
createdeliveryroute 2/23/10 Perth Darwin Alice_Springs Adelaide Melbourne Sydney Brisbane
assigntrucktoroute 1
assigntrucktoroute 2
```
**Assign package to route** - assigns a package to route by taking package id and route id as parameters. A truck has to be already assigned to the route since it takes into consideration the truck's total capacity.
```py
login Employee Epassword
createdeliveryroute 2/21/6 Alice_Springs Adelaide Melbourne Sydney Brisbane
createdeliverypackage Alice_Springs Adelaide 10000 test1@email.com
createdeliverypackage Adelaide Sydney 10000 test2@email.com
createdeliverypackage Adelaide Brisbane 3000 test3@email.com
assigntrucktoroute 1
assignpackagetoroute 1 1
assignpackagetoroute 2 1
assignpackagetoroute 3 1
```
**Get package info** - returns information about the package after providing package id.
```py
login Employee Epassword
createdeliverypackage Sydney Melbourne 45 test@email.com
getpackageinfo 1
```
**View unassigned packages** - returns start and end location about all packages who have yet to be assigned to a route. Supervisor or manager account is required to use this command.
```py
login Supervisor Spassword
createdeliverypackage Alice_Springs Adelaide 10000 test1@email.com
createdeliverypackage Adelaide Sydney 10000 test2@email.com
createdeliverypackage Adelaide Brisbane 3000 test3@email.com
viewunassignedpackages
```
**Package status** - returns information about the current status of a package(not assigned/pending/en route/delivered). It takes package id as parameter.
```py
login Employee Epassword
createdeliveryroute 2/21/6 Brisbane Sydney Melbourne Adelaide
assigntrucktoroute 1
createdeliverypackage Sydney Adelaide 5000 test@email.com
assignpackagetoroute 1 1
packagestatus 1
updateday 2
packagestatus 1
```
**Show available trucks** - returns information about the current availability of the trucks. It takes into account their different types.
```py
login Employee Epassword
createdeliveryroute 2/21/6 Darwin Brisbane Sydney Melbourne Adelaide Alice_Springs
assigntrucktoroute 1
updateday 1
showavailabletrucks
```
**View all routes** - returns detailed information about all ongoing routes. The information includes the departure time at the starting location and arrival times at the rest of the locations. It also provides information about which truck is assigned to the route and all the packages assigned, or if there are none. Manager access is required.
```py
login Manager Mpassword
createdeliveryroute 2/21/8 Brisbane Sydney Melbourne Adelaide Alice_Springs Darwin
createdeliveryroute 2/21/8 Perth Darwin Adelaide Melbourne
createdeliverypackage Perth Melbourne 5000 test@email.com
assigntrucktoroute 1
assigntrucktoroute 2
assignpackagetoroute 1 2
updateday 2
viewallroutes
```

## Example input and expected output

**Example input:**
```
createdeliveryroute 2/21/22 Brisbane Sydney Melbourne
login Employee Epassword
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
logout
login Supervisor Spassword
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
logout
login Manager Mpassword
viewallroutes
showavailabletrucks
end
```
**Expected output:**
```
User isn't logged in.
Employee has logged in.
Route 1: Brisbane -> Sydney -> Melbourne created.
Route 2: Sydney -> Melbourne -> Adelaide created.
Route 3: Perth -> Adelaide -> Melbourne -> Sydney -> Brisbane -> Darwin -> Alice_Springs created.
Truck with id 1001 was assigned to route id 1.
Truck with id 1001 was assigned to route id 2.
Package with id 1 created.
-- Accepted in city: Sydney --
-- Delivery to: Melbourne --
-- Weight: 5500kg --
-- Contact Info: test@email_1.com --
Package with id 2 created.
-- Accepted in city: Adelaide --
-- Delivery to: Sydney --
-- Weight: 6000kg --
-- Contact Info: test@email_2.com --
Package with id 3 created.
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
Only supervisors and managers are allowed to view all unassigned packages!
User logged out.
Supervisor has logged in.
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
Current day is now Feb 25th 20:52h.
Package 2 status is Delivered.
Package 3 status is En route.
Only managers are allowed to view all delivery routes in progress!
Set off time cannot be more than 30 days in the future.
Current day is now Feb 29th 20:52h.
Package 3 status is Delivered.
Current day is now Mar 25th 20:52h.
Set off time cannot be in the past.
Route 4: Adelaide -> Sydney -> Brisbane -> Darwin created.
Only managers are allowed to view all delivery routes in progress!
User logged out.
Manager has logged in.
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
## Optional future implementations:

- **Truck history** - a comprehensive record-keeping journal of each route undertaken by a certain truck.
- **Fuel calculation** - a method to calculate the fuel consumption based on factors like distance and weight. It will show information about when the truck has to be refueled.
- **Resting time management** - it will track automatically driving time and enforce the mandatory resting periods.