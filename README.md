# Logistics-App

Teamwork in Python OOP Module in Telerik Academy

**Logistics App** is an application aiming to expand an Australian company's activities to the freight industry. The app is going to be used to manage the delivery of packages between hubs in major Australian cities.

**Contributors:**

|       Name            |                   Github Username                 |
|:---------------------:|:-------------------------------------------------:|
| Valentin Penev        | [FalseBeliefs](https://github.com/FalseBeliefs)   |
| Konstantin Ivanov     | [dnrubinart](https://github.com/dnrubinart)       |
| Radostin Mihaylov     | [radoooo11](https://github.com/radoooo11)         |


## **TEMPORARY INPUT FOR TESTS**

Checks routes and the ids of the assigned trucks to them. Shows them through the "viewroute" command.
```
createtrucks
createdeliveryroute Brisbane Sydney Melbourne
createdeliveryroute Perth Adelaide Melbourne Sydney Brisbane Darwin Alice_Springs
assigntrucktoroute 1
createdeliverypackage Sydney Melbourne 5500 0412345678
assignpackagetoroute 1 1
assigntrucktoroute 2
createdeliverypackage Adelaide Darwin 6000 0512345678
createdeliverypackage Perth Sydney 3000 0512345678
assignpackagetoroute 2 2
assignpackagetoroute 3 2
viewroute 1
viewroute 2
end
```