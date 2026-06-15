# Physical Architecture requirements - OUTDATED AND NEEDS WORK

# Primary Objectives
Impervious to terrorism
Physical separation of networks aiding logical separation

# Broad Ideas

* Location 53.103480, 18.092934
* Defended by the military from the outside
* Defended by UOP from the inside
* Antiterrorist approach to corridor layout
* Small Datacenter
* Future proofed for a network of small datacenters
* High-tech Reactor underground (SMR (eg. BWRX-300)), overproduction fed back to grid
    * Second redundant power supply from grid
    * UPS for management stack
    * Access to water from Wistula and Brda
* Floors -4 to 2 (floor 1 being ground level)
* Water + Air based cooling (water cools air) - for datacenter
* Zespół elektrociepłowni delivers cold air in return for hot water from the reactor
* Zespół elektrociepłowni is defended by the military from the outside
* Zespół elektrociepłowni can reverse air flow to provide suction for possible gas attack - the air should be directed with a chimney up high
* Water based cooling - for BWRX-300
* Main pipe from Wistula through BWRX-300 through zespół elektrociepłowni 
    * Overproduced hot water goes to Brda
    * Second pipe from Brda through BWRX-300 through zespół elektrociepłowni 
        * Overproduced hot water goes to Wistula
* Separate room for Management stack physically separated for Public Cloud
    * ToR switches management access
    * SAN management access
    * Panic room
* Separate room for Management stack for BWRX-300 and building security
* Public Cloud (contracts for critical nation-wide services)
* Office for Public Cloud nearby (suggested by morfo - Arkada on Fordońska)
* Railroad stop for Low-Enriched Uranium supply and tech supply
* Warehouse / Workshop part for loading, unloading and prep of resources and tech
* Tunnel for reacto replacement  used as atomic bunker - gathering point

# Floor Plan - outdated


## BUILDING A
* Building A 2nd floor - office, security unit, private datacenter

  * Faraday Cage in Entire Building A concrete

    * Elevator and stairs from 1
    * No Guest access
    * Panic room in office
    * no windows
* Office for buildings security
    * Management stack for BWRX-300(?) and building operability
        * Secondary Vent Control
        * Secondary Electricity control
    * Private DC - some good new-fashioned, main supercomputer
    * No outside world access for network connectivity
    * Direct Fiber Links to control panel of BWRX-300(?)
    * Retina data and RBAC
    * UPS for Mainframe only
    * Latrine (side by side with latrine of security unit to allow for breach)
    * Elevator to -1, -2 and -3
* Security unit
    * Armory
?! Vent to -1
? Roof access
* Latrine

* Cabled cameras to outside and inside
* Bulletproof openable windows to outside
* bulletproof one-sided mirror window overlook from security unit to the warehouse
        * openable slits to aim at the entire warehouse




## BUILDING B
* Building B 1st floor (ground) - datacenter, public cloud datacenter,  warehouse
    * Canteen
    * No windows
    * No network devices - just compute and patch panels (kings requirement;)
    * No storage devices - just compute and patch panels (kings requirement;)
    * Stairs and elevator to 2
    * Access to 2nd floor via elevator and stairs in the warehouse
    * Access to 1st floor via elevator and stairs in the warehouse
    * Access from the outside via retina scan
    * room for Management redundant building control stack 
    * physically separated from Public Cloud
    * Redundant VMs for HA of Mainframe hosted services (redundancy for possible failure and Mainframe maintenance)
    * ToR switches management access
    * SAN management access
    * Panic room
* Public cloud area reserved for compute + patch panels
* -1st floor
    * UPS for public and building electricity
    * ToR switches
    * SAN Storage
    * Cooling source for
        * Public Cloud
        * Public Management Stack
        * IBM Mainframe
        * Vent entrance goes up with a ladder
            * stopped by 3 meters of solid concrete below 1st floor
            * Smaller vents lead out to 1st floor (impossible to climb through)
            * Fiber pipes allow for replacement or addition of cables
* small heated office
    * panic room
* Elevator to 2nd, -2nd
* Stairs to 2nd floor panic room
    * Panic button to enter the stairs
    * Panic button to exit the stairs to +2 office
    * Doors close automatically and have their own battery
* Retina scan to get out of the room towards networking area
* Latrine
* Cold air suit point
    * For network engineers to not get cold when working in a highly vented area
    * For reactor engineers to not get irradiated
* Primary Vent control
* Primary Electricity control
* Electric network grid/sockets for public
    * Outside grid network switch for IBM Mainframe and building electricity (redundant power)
* flooding prevention system (pipes and water tanks for the reactor are underneath) - output from the 3rd reactor water flow system will become output for the sewage system
* -2nd floor ( teraz ground level )
    * Elevator to 2nd floor office / panic room
    * Hazmat suit point
    * Stairs to decontamination chamber accessed with retina
    * Direct access to bunker via decontamination chamber
        * Exit to the bunker with retina scan or panic button
        * Entrance from the bunker to decontamination with retina
        * Entrance from decontamination chamber to ‘reactor room’ with button
        * Exit from ‘reactor room’ to decontamination with a button
        * Decontamination chamber contains panic button to exit to the bunker
    * Supplies are moved through the bunker to the contamination chamber and then to -3rd floor
    * -4th floor
        * Water tanks
        * Przyreaktorowy basen paliwowy
        * Turbina
        * Generator
        * amortyzatory sejsmiczne 
        * instalacja odbioru chłodziwa na dnie

# pipelines - hydraulics


# Requirements
    * Cabling (electricity, fiber, input, output, UPS, retina)
    * Piping in/out
        * Latrines piping
        * Flood prevention piping
        * input /output to vistula and brda
    * Cooling in
    * Heating in
    * Soft requirement - concrete reinforcement layout
    * Thickness of walls
    * Riverside atomic shelter/tunnel for reactor replacement and army rest

# Suggested Dimensions (to be redone)
Poziom 0: Grunt. (67m ponad poziomem morza - przypominam, że Wisła jest nad poziomem morza 25m)
Poziom -1: (0 do -7 m) (67mnpm do 60mnpm)– Infrastruktura krytyczna, UPS.
Poziom -2: (-7 do -14 m)(60mnpm do 53mnpm) – Pokój techników i sterownia. Bezpieczna odległość od reaktora, osłona biologiczna od góry.
Poziom -3: (-14 do -21 m)(53mnpm do 46mnpm) – Logistyka i materiały niebezpieczne. Tutaj kończy się Twój tunel (rampa). To jest "Hala Przeładunkowa".
Poziom -4: (Dno szybu na głębokości ok. -50 m (15 metrów npm.)).
