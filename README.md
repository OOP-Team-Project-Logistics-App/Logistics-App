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
createdeliveryroute Sydney Melbourne Adelaide
createdeliveryroute Alice_Springs Adelaide Melbourne Sydney Brisbane
createdeliveryroute Perth Adelaide Melbourne Sydney Brisbane Darwin Alice_Springs
viewroute 1
viewroute 2
viewroute 3
viewroute 4
createdeliverypackage Adelaide Sydney 1000
assigntrucktoroute 3
assignpackagetoroute 1 3
end
```

end command currently not working