## 17 - Weather Observation Station 12
<br>

## Problem
Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

<br>

---

## Solution


```SQL
select distinct city from station
where lower(left(city,1)) not in ('a','e','i','o','u') and lower(right(city,1)) not in ('a','e','i','o','u');
```

<br>

**Output**

```
Kissee Mills
Loma Mar
Sandy Hook
Tipton
Turner
Slidell
Negreet
Chignik Lagoon
Hanna City
Monument
Manchester
Prescott
Graettinger
Sturgis
Highwood
Bowdon
Tyler
Watkins
Republic
Bowdon Junction
Hoskinston
Talbert
Mccomb
Kirk
Carlock
Seward
Roy
Pattonsburg
Centertown
Norvell
Beaver Island
Jemison
West Hills
Culdesac
Roselawn
Forest Lakes
San Simeon
Little Rock
Portland
New Century
Hampden
Pine City
Sandborn
Seaton
Prince Frederick
Pomona Park
Yazoo City
Jolon
Childs
Shreveport
Forest
Sizerock
Buffalo Creek
Winsted
Woodbury
Hackleburg
Soldier
Columbus
Kirkland
Wilton
Busby
Reeds
Hayfork
Mcbrides
Lee Center
Henderson
Palm Desert
Benedict
Tamms
Haubstadt
Clancy
Scotts Valley
Norwood
Bridgeport
Cherry
Griffin
Pine Bluff
Baldwin
Pony
Franklin
Vulcan
Prairie Du Rocher
Carver
Paron
Winchester
Greenview
Lucerne Valley
Cromwell
Quinter
Whitewater
Round Pond
Rockton
North Berwick
Richland
Fremont
Philipsburg
Kensett
Koleen
Winslow
Reasnor
Frankfort Heights
Linthicum Heights
Pengilly
Newton Center
Newbury
Kismet
Canton
Clipper Mills
Pierre Part
Bison
Ridgway
South Britain
Rydal
Deerfield
Montreal
Knob Lick
Cranks
Rives Junction
Ledyard
Norway
Rantoul
Richmond Hill
Fredericktown
Glen Carbon
Fredericksburg
Mc Henry
Wellington
Hoffman Estates
Ducor
Salem
Sturdivant
Larkspur
Patriot
Carlos
Climax
Southport
Compton
Rumsey
Rogers
Libertytown
Church Creek
Dumont
Gales Ferry
Williams
Decatur
Holbrook
Sherrill
Linden
Sedgwick
Fort Atkinson
Peachtree City
Rocheport
West Somerset
Clovis
Heyburn
Peabody
Marion Junction
Randall
Jordan
White Horse Beach
Macy
Flowood
Deep River
Napoleon
Leavenworth
Coldwater
Weldon
Turners Falls
Delray Beach
Mineral Point
Midpines
Tefft
Showell
Brighton
Grimes
Nubieber
North Monmouth
Harmony
Beaufort
Humeston
Firebrick
Ludington
Channing
West Baden Springs
Melber
Sanders
Schleswig
Harbor Springs
Richmond
Siler
Reeves
Clifton
Crescent City
Panther Burn
Hanscom Afb
Bennington
Garland
Clutier
Lupton
Northfield
Norris
Clopton
Saint Paul
Kingsland
Fairview
Bridgton
Brownstown
Hartland
Mesick
Dryden
Beverly
Marine On Saint Croix
Pocahontas
Yoder
Gatewood
Madden
Cheswold
Jack
Hawarden
Cannonsburg
North Branford
New Liberty
Woodstock Valley
Farmington
Pfeifer
Gridley
Fulton
Winter Park
Del Mar
Greens Fork
Garden City
Blue River
New Ross
Brilliant
Norphlet
Mechanic Falls
North Middletown
Keyes
Neon
Calhoun
Mullan
Coalgood
Walnut
Saint Petersburg
Julian
Veedersburg
Payson
Windom
Ludlow
Lindsay
Bristol
Zachary
Hills
Montgomery City
Delavan
Byron
Baker
Hyde Park
Groveoak
Kenner
Many
Berryton
Newark
Cowgill
Novinger
Goodman
Cobalt
South Haven
West Hyannisport
Jackson
Lapeer
Peaks Island
Hazlehurst
Chester
Clarkston
Healdsburg
Hotchkiss
Ravenden Springs
Kell
Strasburg
Five Points
Norris City
Coaling
Corcoran
Greenway
Strawn
Dent
Shingletown
Fort Lupton
South Carrollton
Taft
Knobel
Bullhead City
Haverhill
Siloam
Freeport
Gorham
Bass Harbor
Granger
```
