## 015 - Weather Observation Station 11
<br>

## Problem
Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.


## Input Format

The `STATION` table is described as follows :

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where `LAT_N` is the northern latitude and `LONG_W` is the western longitude.

<br>

---

## Solution


```SQL
select distinct city from station
where lower(left(city,1)) not in ('a','e','i','o','u') or lower(right(city,1)) not in ('a','e','i','o','u');
```

<br>

**Output**

```
Kissee Mills
Loma Mar
Sandy Hook
Tipton
Arlington
Turner
Slidell
Negreet
Glencoe
Chelsea
Chignik Lagoon
Pelahatchie
Hanna City
Dorrance
Albany
Monument
Manchester
Prescott
Graettinger
Cahone
Sturgis
Highwood
Waipahu
Bowdon
Tyler
Watkins
Republic
Millville
Bowdon Junction
Morenci
South El Monte
Hoskinston
Talbert
Mccomb
Kirk
Carlock
Seward
Gustine
Delano
Westphalia
Saint Elmo
Roy
Pattonsburg
Centertown
Norvell
Raymondville
Beaver Island
Odin
Jemison
West Hills
Barrigada
Hesperia
Wickliffe
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
Milledgeville
Prince Frederick
Pomona Park
Gretna
Yazoo City
Zionsville
Rio Oso
Jolon
Childs
Shreveport
Forest
Sizerock
Buffalo Creek
Algonac
Onaway
Irvington
Winsted
Woodbury
Samantha
Hackleburg
Soldier
Arrowsmith
Columbus
Bentonville
Kirkland
Grosse Pointe
Wilton
Busby
Robertsdale
Dale
Reeds
Hayfork
Mcbrides
Lee Center
Tennessee
Henderson
Udall
Palm Desert
Benedict
Oakfield
Tamms
Haubstadt
Chokio
Clancy
Scotts Valley
Norwood
Elkton
Bertha
Bridgeport
Cherry
Regina
Griffin
Pine Bluff
Mascotte
Baldwin
Netawaka
Pony
Franklin
Vulcan
Prairie Du Rocher
Alanson
Delta
Carver
Paron
Winchester
Jerome
Baton Rouge
Greenview
Lucerne Valley
Cromwell
Quinter
Whitewater
Round Pond
Clarkdale
Rockton
Pheba
Auburn
North Berwick
Grandville
Susanville
Rosie
Verona
Richland
Fremont
Philipsburg
Kensett
De Tour Village
Koleen
Winslow
Reasnor
West Grove
Frankfort Heights
Bono
Biggsville
Linthicum Heights
Marysville
Cape Girardeau
Pengilly
Newton Center
Crane Lake
Newbury
Kismet
Canton
Clipper Mills
Grayslake
Pierre Part
Bison
Bellevue
Ridgway
South Britain
Rydal
Lynnville
Deerfield
Montreal
Hope
Gowrie
Knob Lick
Crouseville
Cranks
Rives Junction
Ledyard
Norway
Eros
Rantoul
Richmond Hill
Fredericktown
Glen Carbon
Fredericksburg
Mc Henry
Wellington
Hoffman Estates
Howard Lake
Edgewater
Ducor
Salem
Sturdivant
Hagatna
East Haddam
Larkspur
Patriot
Corriganville
Carlos
Addison
Tarzana
Grapevine
Kanorado
Climax
Curdsville
Southport
Compton
Notasulga
Rumsey
Rogers
Pleasant Grove
Everton
Skanee
Springerville
Libertytown
Church Creek
Yellow Pine
Dumont
Gales Ferry
Ravenna
Williams
Decatur
Holbrook
Sherrill
Brownsdale
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
Hayesville
Jordan
White Horse Beach
Greenville
Macy
Flowood
Deep River
Napoleon
Leavenworth
Coldwater
Weldon
Yellville
Turners Falls
Delray Beach
Eustis
Mineral Point
Weldona
Midpines
Cascade
Tefft
Showell
Bayville
Brighton
Grimes
Nubieber
North Monmouth
Harmony
Beaufort
Union Star
Humeston
Baileyville
Lakeville
Firebrick
Pico Rivera
Ludington
Channing
West Baden Springs
Pawnee
Melber
Bainbridge
Sanders
Ottertail
Dupo
Montrose
Schleswig
Harbor Springs
Richmond
Siler
Reeves
Clifton
Casco
Crescent City
Madisonville
Albion
Lismore
Athens
Panther Burn
Hanscom Afb
Wildie
Mosca
Bennington
Lottie
Garland
Clutier
Lupton
Northfield
Daleville
Osage City
Cuba
Norris
Clopton
Renville
Saint Paul
Kirksville
Kingsland
Fairview
Lydia
Bridgton
Brownstown
Monona
Hartland
Andover
Lakota
Grand Terrace
Mesick
Dryden
Beverly
Marine On Saint Croix
Pocahontas
Fort Meade
Hayneville
Yoder
Gatewood
Madden
Losantville
Cheswold
Caseville
Pomona
Hopkinsville
Jack
Dixie
Hillside
Hawarden
Cannonsburg
North Branford
New Liberty
Woodstock Valley
Farmington
Honolulu
Pfeifer
Gridley
Fulton
Winter Park
Monroe
Del Mar
Greens Fork
Garden City
Blue River
New Ross
Brilliant
Olmitz
Allerton
Norphlet
Mechanic Falls
North Middletown
Keyes
Equality
Neon
Calhoun
Mullan
Coalgood
Walnut
Saint Petersburg
Julian
Veedersburg
Orange Park
Payson
Windom
Ludlow
Lindsay
Palatka
Bristol
Ukiah
Yuma
Zachary
Esmond
Waresboro
Hills
Montgomery City
Delavan
Magnolia
Byron
Dundee
Eureka Springs
Baker
Hyde Park
Groveoak
Kenner
Many
Berryton
Chilhowee
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
Orange City
Effingham
Corcoran
Alton
Greenway
Woodsboro
Strawn
Dent
Shingletown
Clio
Yalaha
Leakesville
Fort Lupton
Shasta
Agency
South Carrollton
Taft
Calpine
Knobel
Bullhead City
Tina
Anthony
Emmett
Haverhill
Middleboro
Siloam
Lena
Lee
Freeport
Mid Florida
Gorham
Bass Harbor
Granger
```
