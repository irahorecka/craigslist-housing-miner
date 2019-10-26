#ALL CL FILTERS AND STATES' CRAIGSLIST REGIONS IN DICTIONARY

class Filters:
    #A file to store room filters, rooming categories, and state keys in dictionaries
    #extra_filters is a general filter sheet for specifics - not all housing categories adhere to every part of this filter
    #e.g. you will not look for max_bedrooms for a room/share craigslist posts
    #create selectors in the future to limit which filters are mutable by the user per category they choose
    extra_filters = {'private_room' : None, #bool
        'private_bath' : None, #bool
        'cats_ok' : None, #bool
        'dogs_ok' : None, #bool
        'min_price' : None,
        'max_price' : None,
        'min_ft2' : None,
        'max_ft2' : None,
        'min_bedrooms' : None,
        'max_bedrooms' : None,
        'min_bathrooms' : None,
        'max_bathrooms' : None,
        'no_smoking' : None, #bool
        'is_furnished' : None, #bool
        'wheelchair_acccess' : None, #bool
        'has_image' : None #bool
    }

    distance_filters = {'search_distance': None,
        'zip_code': None
    }

    cat_dict = {'apa':'apts & housing for rent',
        'swp':'housing swap',
        'off':'office & commercial',
        'prk':'parking & storage',
        'reb':'real estate - by broker',
        'reo':'real estate - by owner',
        'roo':'rooms & shares',
        'sub':'sublets & temporary',
        'vac':'vacation rentals',
        'hou':'wanted: apts',
        'rew':'wanted: real estate',
        'sha':'wanted: room & share',
        'sbw':'wanted: sublet & temp'}

    apa_dict = {'aap':'apts & housing for rent',
        'swp':'housing swap',
        'off':'office & commercial',
        'prk':'parking & storage',
        'reb':'real estate - by broker',
        'reo':'real estate - by owner',
        'roo':'rooms & shares',
        'sub':'sublets & temporary',
        'vac':'vacation rentals',
        'hou':'wanted: apts',
        'rew':'wanted: real estate',
        'sha':'wanted: room & share',
        'sbw':'wanted: sublet & temp'}


class Countries:
    united_states = {
        'alabama': {'auburn': 'auburn, AL',
            'bham': 'birmingham, AL',
            'dothan': 'dothan, AL',
            'shoals': 'florence / muscle shoals',
            'gadsden': 'gadsden-anniston',
            'huntsville': 'huntsville / decatur',
            'mobile': 'mobile, AL',
            'montgomery': 'montgomery, AL',
            'tuscaloosa': 'tuscaloosa',
            },
        'alaska': {'anchorage': 'anchorage / mat-su',
            'fairbanks': 'fairbanks, AK',
            'kenai': 'kenai peninsula',
            'juneau': 'southeast alaska',
            },
        'arizona': {'flagstaff': 'flagstaff / sedona',
            'mohave': 'mohave county',
            'phoenix': 'phoenix, AZ',
            'prescott': 'prescott, AZ',
            'showlow': 'show low, AZ',
            'sierravista': 'sierra vista, AZ',
            'tucson': 'tucson, AZ',
            'yuma': 'yuma, AZ',
            'focus_dist': {'phoenix': ['cph', 'evl', 'nph', 'wvl']
                }
            },
        'arkansas': {'fayar': 'fayetteville, AR',
            'fortsmith': 'fort smith, AR',
            'jonesboro': 'jonesboro, AR',
            'littlerock': 'little rock',
            'texarkana': 'texarkana',
            },
        'california': {'bakersfield': 'bakersfield, CA',
            'chico': 'chico, CA',
            'fresno': 'fresno / madera',
            'goldcountry': 'gold country',
            'hanford': 'hanford-corcoran',
            'humboldt': 'humboldt county',
            'imperial': 'imperial county',
            'inlandempire': 'inland empire, CA',
            'losangeles': 'los angeles',
            'mendocino': 'mendocino county',
            'merced': 'merced, CA',
            'modesto': 'modesto, CA',
            'monterey': 'monterey bay',
            'orangecounty': 'orange county, CA',
            'palmsprings': 'palm springs, CA',
            'redding': 'redding, CA',
            'sacramento': 'sacramento',
            'sandiego': 'san diego',
            'sfbay': 'SF bay area',
            'slo': 'san luis obispo',
            'santabarbara': 'santa barbara',
            'santamaria': 'santa maria, CA',
            'siskiyou': 'siskiyou county',
            'stockton': 'stockton, CA',
            'susanville': 'susanville, CA',
            'ventura': 'ventura county',
            'visalia': 'visalia-tulare',
            'yubasutter': 'yuba-sutter, CA',
            'focus_dist': {'losangeles': ['wst', 'sfv', 'lac', 'sgv', 'lgb', 'ant'],
                'sandiego': ['csd', 'nsd', 'esd', 'ssd'],
                'sfbay': ['sfc', 'sby', 'eby', 'pen', 'nby', 'scz']
                }
            },
        'colorado': {'boulder': 'boulder, CO',
            'cosprings': 'colorado springs',
            'denver': 'denver, CO',
            'eastco': 'eastern CO',
            'fortcollins': 'fort collins / north CO',
            'rockies': 'high rockies',
            'pueblo': 'pueblo, CO',
            'westslope': 'western slope',
            },
        'connecticut': {'newlondon': 'eastern CT',
            'hartford': 'hartford, CT',
            'newhaven': 'new haven, CT',
            'nwct': 'northwest CT',
            },
        'delaware': {'delaware': 'Delaware'
            },
        'district_of_columbia': {'washingtondc': 'Washingtondc'
            },
        'florida': {'miami': 'broward county',
            'daytona': 'daytona beach',
            'keys': 'florida keys',
            'fortlauderdale': 'south florida',
            'fortmyers': 'ft myers / SW florida',
            'gainesville': 'gainesville, FL',
            'cfl': 'heartland florida',
            'jacksonville': 'jacksonville, FL',
            'lakeland': 'lakeland, FL',
            'miami': 'miami / dade county',
            'lakecity': 'north central FL',
            'ocala': 'ocala, FL',
            'okaloosa': 'okaloosa / walton',
            'orlando': 'orlando, FL',
            'panamacity': 'panama city, FL',
            'pensacola': 'pensacola, FL',
            'sarasota': 'sarasota-bradenton',
            'miami': 'south florida',
            'spacecoast': 'space coast, FL',
            'staugustine': 'st augustine, FL',
            'tallahassee': 'tallahassee',
            'tampa': 'tampa bay area',
            'treasure': 'treasure coast, FL',
            'miami': 'palm beach county',
            'focus_dist': {'miami': ['mdc', 'pbc'],
                'fortlauderdale': ['mdc', 'brw', 'pbc'],
                'fortmyers': ['lee', 'chl', 'col'],
                'miami': ['brw', 'pbc'],
                'miami': ['mdc', 'brw', 'pbc'],
                'tampa': ['hdo', 'hil', 'psc', 'pnl'],
                'miami': ['mdc', 'brw']
                }
            },
        'georgia': {'albanyga': 'albany, GA',
            'athensga': 'athens, GA',
            'atlanta': 'atlanta, GA',
            'augusta': 'augusta, GA',
            'brunswick': 'brunswick, GA',
            'columbusga': 'columbus, GA',
            'macon': 'macon / warner robins',
            'nwga': 'northwest GA',
            'savannah': 'savannah / hinesville',
            'statesboro': 'statesboro, GA',
            'valdosta': 'valdosta, GA',
            'focus_dist': {'atlanta': ['atl', 'nat', 'eat', 'sat', 'wat']
                }
            },
        'hawaii': {'honolulu': 'Honolulu'
            },
        'idaho': {'boise': 'boise, ID',
            'eastidaho': 'east idaho',
            'lewiston': 'lewiston / clarkston',
            'twinfalls': 'twin falls, ID',
            },
        'illinois': {'bn': 'bloomington-normal',
            'chambana': 'champaign urbana',
            'chicago': 'chicago',
            'decatur': 'decatur, IL',
            'lasalle': 'la salle co',
            'mattoon': 'mattoon-charleston',
            'peoria': 'peoria, IL',
            'rockford': 'rockford, IL',
            'carbondale': 'southern illinois',
            'springfieldil': 'springfield, IL',
            'quincy': 'western IL',
            'focus_dist': {'chicago': ['chc', 'nch', 'wcl', 'sox', 'nwi', 'nwc']
                }
            },
        'indiana': {'bloomington': 'bloomington, IN',
            'evansville': 'evansville, IN',
            'fortwayne': 'fort wayne, IN',
            'indianapolis': 'indianapolis',
            'kokomo': 'kokomo, IN',
            'tippecanoe': 'lafayette / west lafayette',
            'muncie': 'muncie / anderson',
            'richmondin': 'richmond, IN',
            'southbend': 'south bend / michiana',
            'terrehaute': 'terre haute, IN',
            },
        'iowa': {'ames': 'ames, IA',
            'cedarrapids': 'cedar rapids, IA',
            'desmoines': 'des moines, IA',
            'dubuque': 'dubuque',
            'fortdodge': 'fort dodge, IA',
            'iowacity': 'iowa city, IA',
            'masoncity': 'mason city, IA',
            'quadcities': 'quad cities, IA/IL',
            'siouxcity': 'sioux city, IA',
            'ottumwa': 'southeast IA',
            'waterloo': 'waterloo / cedar falls',
            },
        'kansas': {'lawrence': 'lawrence, KS',
            'ksu': 'manhattan, KS',
            'nwks': 'northwest KS',
            'salina': 'salina, KS',
            'seks': 'southeast KS',
            'swks': 'southwest KS',
            'topeka': 'topeka, KS',
            'wichita': 'wichita, KS',
            },
        'kentucky': {'bgky': 'bowling green, KY',
            'eastky': 'eastern kentucky',
            'lexington': 'lexington, KY',
            'louisville': 'louisville, KY',
            'owensboro': 'owensboro, KY',
            'westky': 'western KY',
            },
        'louisiana': {'batonrouge': 'baton rouge',
            'cenla': 'central louisiana',
            'houma': 'houma, LA',
            'lafayette': 'lafayette, LA',
            'lakecharles': 'lake charles, LA',
            'monroe': 'monroe, LA',
            'neworleans': 'new orleans',
            'shreveport': 'shreveport, LA',
            },
        'maine': {'maine': 'Maine'
            },
        'maryland': {'annapolis': 'annapolis, MD',
            'baltimore': 'baltimore, MD',
            'easternshore': 'eastern shore',
            'frederick': 'frederick, MD',
            'smd': 'southern maryland',
            'westmd': 'western maryland',
            },
        'massachusetts': {'boston': 'boston',
            'capecod': 'cape cod / islands',
            'southcoast': 'south coast, MA',
            'westernmass': 'western massachusetts',
            'worcester': 'worcester / central MA',
            'focus_dist': {'boston': ['gbs', 'nwb', 'bmw', 'nos', 'sob']
                }
            },
        'michigan': {'annarbor': 'ann arbor, MI',
            'battlecreek': 'battle creek, MI',
            'centralmich': 'central michigan',
            'detroit': 'detroit metro',
            'flint': 'flint, MI',
            'grandrapids': 'grand rapids, MI',
            'holland': 'holland, MI',
            'jxn': 'jackson, MI',
            'kalamazoo': 'kalamazoo, MI',
            'lansing': 'lansing, MI',
            'monroemi': 'monroe, MI',
            'muskegon': 'muskegon, MI',
            'nmi': 'northern michigan',
            'porthuron': 'port huron, MI',
            'saginaw': 'saginaw-midland-baycity',
            'swmi': 'southwest michigan',
            'thumb': 'the thumb, MI',
            'up': 'upper peninsula, MI',
            'focus_dist': {'detroit': ['mcb', 'wyn', 'okl']
                }
            },
        'minnesota': {'bemidji': 'bemidji, MN',
            'brainerd': 'brainerd, MN',
            'duluth': 'duluth / superior',
            'mankato': 'mankato, MN',
            'minneapolis': 'minneapolis / st paul',
            'rmn': 'rochester, MN',
            'marshall': 'southwest MN',
            'stcloud': 'st cloud, MN',
            'focus_dist': {'minneapolis': ['hnp', 'ram', 'ank', 'wsh', 'dak', 'csw']
                }
            },
        'mississippi': {'gulfport': 'gulfport / biloxi',
            'hattiesburg': 'hattiesburg, MS',
            'jackson': 'jackson, MS',
            'meridian': 'meridian, MS',
            'northmiss': 'north mississippi',
            'natchez': 'southwest MS',
            },
        'missouri': {'columbiamo': 'columbia / jeff city',
            'joplin': 'joplin, MO',
            'kansascity': 'kansas city, MO',
            'kirksville': 'kirksville, MO',
            'loz': 'lake of the ozarks',
            'semo': 'southeast missouri',
            'springfield': 'springfield, MO',
            'stjoseph': 'st joseph',
            'stlouis': 'st louis, MO',
            },
        'montana': {'billings': 'billings, MT',
            'bozeman': 'bozeman, MT',
            'butte': 'butte, MT',
            'greatfalls': 'great falls, MT',
            'helena': 'helena, MT',
            'kalispell': 'kalispell, MT',
            'missoula': 'missoula, MT',
            'montana': 'eastern montana',
            },
        'nebraska': {'grandisland': 'grand island, NE',
            'lincoln': 'lincoln, NE',
            'northplatte': 'north platte, NE',
            'omaha': 'omaha / council bluffs',
            'scottsbluff': 'scottsbluff / panhandle',
            },
        'nevada': {'elko': 'elko, NV',
            'lasvegas': 'las vegas',
            'reno': 'reno / tahoe',
            },
        'new_hampshire': {'nh': 'Nh'
            },
        'new_jersey': {'cnj': 'central NJ',
            'jerseyshore': 'jersey shore',
            'newjersey': 'north jersey',
            'southjersey': 'south jersey',
            },
        'new_mexico': {'albuquerque': 'albuquerque',
            'clovis': 'clovis / portales',
            'farmington': 'farmington, NM',
            'lascruces': 'las cruces, NM',
            'roswell': 'roswell / carlsbad',
            'santafe': 'santa fe / taos',
            },
        'new_york': {'albany': 'albany, NY',
            'binghamton': 'binghamton, NY',
            'buffalo': 'buffalo, NY',
            'catskills': 'catskills',
            'chautauqua': 'chautauqua, NY',
            'elmira': 'elmira-corning',
            'fingerlakes': 'finger lakes, NY',
            'glensfalls': 'glens falls, NY',
            'hudsonvalley': 'hudson valley, NY',
            'ithaca': 'ithaca, NY',
            'longisland': 'long island, NY',
            'newyork': 'new york city',
            'oneonta': 'oneonta, NY',
            'plattsburgh': 'plattsburgh-adirondacks',
            'potsdam': 'potsdam-canton-massena',
            'rochester': 'rochester, NY',
            'syracuse': 'syracuse, NY',
            'twintiers': 'twin tiers NY/PA',
            'utica': 'utica-rome-oneida',
            'watertown': 'watertown, NY',
            'focus_dist': {'newyork': ['mnh', 'brk', 'que', 'brx', 'stn', 'jsy', 'lgi', 'wch', 'fct']
                }
            },
        'north_carolina': {'asheville': 'asheville, NC',
            'boone': 'boone, NC',
            'charlotte': 'charlotte, NC',
            'eastnc': 'eastern NC',
            'fayetteville': 'fayetteville, NC',
            'greensboro': 'greensboro, NC',
            'hickory': 'hickory / lenoir',
            'onslow': 'jacksonville, NC',
            'outerbanks': 'outer banks',
            'raleigh': 'raleigh / durham / CH',
            'wilmington': 'wilmington, NC',
            'winstonsalem': 'winston-salem, NC',
            },
        'north_dakota': {'bismarck': 'bismarck, ND',
            'fargo': 'fargo / moorhead',
            'grandforks': 'grand forks',
            'nd': 'north dakota',
            },
        'ohio': {'akroncanton': 'akron / canton',
            'ashtabula': 'ashtabula, OH',
            'athensohio': 'athens, OH',
            'chillicothe': 'chillicothe, OH',
            'cincinnati': 'cincinnati, OH',
            'cleveland': 'cleveland, OH',
            'columbus': 'columbus, OH',
            'dayton': 'dayton / springfield',
            'limaohio': 'lima / findlay',
            'mansfield': 'mansfield, OH',
            'sandusky': 'sandusky, OH',
            'toledo': 'toledo, OH',
            'tuscarawas': 'tuscarawas co',
            'youngstown': 'youngstown, OH',
            'zanesville': 'zanesville / cambridge',
            },
        'oklahoma': {'lawton': 'lawton, OK',
            'enid': 'northwest OK',
            'oklahomacity': 'oklahoma city',
            'stillwater': 'stillwater, OK',
            'tulsa': 'tulsa, OK',
            },
        'oregon': {'bend': 'bend, OR',
            'corvallis': 'corvallis/albany',
            'eastoregon': 'east oregon',
            'eugene': 'eugene, OR',
            'klamath': 'klamath falls, OR',
            'medford': 'medford-ashland',
            'oregoncoast': 'oregon coast',
            'portland': 'portland, OR',
            'roseburg': 'roseburg, OR',
            'salem': 'salem, OR',
            'focus_dist': {'portland': ['mlt', 'wsc', 'clk', 'clc', 'nco', 'yam', 'grg']
                }
            },
        'pennsylvania': {'altoona': 'altoona-johnstown',
            'chambersburg': 'cumberland valley',
            'erie': 'erie, PA',
            'harrisburg': 'harrisburg, PA',
            'lancaster': 'lancaster, PA',
            'allentown': 'lehigh valley',
            'meadville': 'meadville, PA',
            'philadelphia': 'philadelphia',
            'pittsburgh': 'pittsburgh, PA',
            'poconos': 'poconos',
            'reading': 'reading, PA',
            'scranton': 'scranton / wilkes-barre',
            'pennstate': 'state college, PA',
            'williamsport': 'williamsport, PA',
            'york': 'york, PA',
            },
        'rhode_island': {'providence': 'Providence'
            },
        'south_carolina': {'charleston': 'charleston, SC',
            'columbia': 'columbia, SC',
            'florencesc': 'florence, SC',
            'greenville': 'greenville / upstate',
            'hiltonhead': 'hilton head',
            'myrtlebeach': 'myrtle beach, SC',
            },
        'south_dakota': {'nesd': 'northeast SD',
            'csd': 'pierre / central SD',
            'rapidcity': 'rapid city / west SD',
            'siouxfalls': 'sioux falls / SE SD',
            'sd': 'south dakota',
            },
        'tennessee': {'chattanooga': 'chattanooga, TN',
            'clarksville': 'clarksville, TN',
            'cookeville': 'cookeville, TN',
            'jacksontn': 'jackson, TN',
            'knoxville': 'knoxville, TN',
            'memphis': 'memphis, TN',
            'nashville': 'nashville, TN',
            'tricities': 'tri-cities, TN',
            },
        'texas': {'abilene': 'abilene, TX',
            'amarillo': 'amarillo, TX',
            'austin': 'austin, TX',
            'beaumont': 'beaumont / port arthur',
            'brownsville': 'brownsville, TX',
            'collegestation': 'college station, TX',
            'corpuschristi': 'corpus christi, TX',
            'dallas': 'dallas / fort worth',
            'nacogdoches': 'deep east texas',
            'delrio': 'del rio / eagle pass',
            'elpaso': 'el paso, TX',
            'galveston': 'galveston, TX',
            'houston': 'houston, TX',
            'killeen': 'killeen / temple / ft hood',
            'laredo': 'laredo, TX',
            'lubbock': 'lubbock, TX',
            'mcallen': 'mcallen / edinburg',
            'odessa': 'odessa / midland',
            'sanangelo': 'san angelo, TX',
            'sanantonio': 'san antonio',
            'sanmarcos': 'san marcos, TX',
            'bigbend': 'southwest TX',
            'texoma': 'texoma',
            'easttexas': 'tyler / east TX',
            'victoriatx': 'victoria, TX',
            'waco': 'waco, TX',
            'wichitafalls': 'wichita falls, TX',
            'focus_dist': {'dallas': ['dal', 'ftw', 'mdf', 'ndf', 'sdf']
                }
            },
        'utah': {'logan': 'logan, UT',
            'ogden': 'ogden-clearfield',
            'provo': 'provo / orem',
            'saltlakecity': 'salt lake city',
            'stgeorge': 'st george, UT',
            },
        'vermont': {'vermont': 'Vermont'
            },
        'virginia': {'charlottesville': 'charlottesville, VA',
            'danville': 'danville',
            'fredericksburg': 'fredericksburg, VA',
            'norfolk': 'norfolk / hampton roads',
            'harrisonburg': 'harrisonburg, VA',
            'lynchburg': 'lynchburg, VA',
            'blacksburg': 'new river valley',
            'richmond': 'richmond, VA',
            'roanoke': 'roanoke, VA',
            'swva': 'southwest VA',
            'winchester': 'winchester, VA',
            },
        'washington': {'bellingham': 'bellingham, WA',
            'kpr': 'kennewick-pasco-richland',
            'moseslake': 'moses lake, WA',
            'olympic': 'olympic peninsula',
            'pullman': 'pullman / moscow',
            'seattle': 'seattle-tacoma',
            'skagit': 'skagit / island / SJI',
            'spokane': "spokane / coeur d'alene",
            'wenatchee': 'wenatchee, WA',
            'yakima': 'yakima, WA',
            'focus_dist': {'seattle': ['see', 'est', 'sno', 'kit', 'tac', 'oly', 'skc']
                }
            },
        'west_virginia': {'charlestonwv': 'charleston, WV',
            'martinsburg': 'eastern panhandle',
            'huntington': 'huntington-ashland',
            'morgantown': 'morgantown, WV',
            'wheeling': 'northern panhandle',
            'parkersburg': 'parkersburg-marietta',
            'swv': 'southern WV',
            'wv': 'west virginia (old)',
            },
        'wisconsin': {'appleton': 'appleton-oshkosh-FDL',
            'eauclaire': 'eau claire, WI',
            'greenbay': 'green bay, WI',
            'janesville': 'janesville, WI',
            'racine': 'kenosha-racine',
            'lacrosse': 'la crosse, WI',
            'madison': 'madison, WI',
            'milwaukee': 'milwaukee, WI',
            'northernwi': 'northern WI',
            'sheboygan': 'sheboygan, WI',
            'wausau': 'wausau, WI',
            },
        'wyoming': {'wyoming': 'Wyoming'
            }
    }
    canada = {
        'alberta': {'calgary': 'calgary, AB',
            'edmonton': 'edmonton, AB',
            'ftmcmurray': 'ft mcmurray, AB',
            'lethbridge': 'lethbridge, AB',
            'hat': 'medicine hat, AB',
            'peace': 'peace river country',
            'reddeer': 'red deer, AB',
            },
        'british_columbia': {'cariboo': 'cariboo, BC',
            'comoxvalley': 'comox valley, BC',
            'abbotsford': 'fraser valley, BC',
            'kamloops': 'kamloops, BC',
            'kelowna': 'kelowna / okanagan',
            'kootenays': 'kootenays, BC',
            'nanaimo': 'nanaimo, BC',
            'princegeorge': 'prince george, BC',
            'skeena': 'skeena-bulkley',
            'sunshine': 'sunshine coast, BC',
            'vancouver': 'vancouver, BC',
            'victoria': 'victoria, BC',
            'whistler': 'whistler / squamish',
            'focus_dist': {'vancouver': ['van', 'nvn', 'bnc', 'rds', 'pml', 'rch']
                }
            },
        'manitoba': {'winnipeg': 'Winnipeg'
            },
        'new_brunswick': {'newbrunswick': 'Newbrunswick'
            },
        'newfoundland_and_labrador': {'newfoundland': 'Newfoundland'
            },
        'northwest_territories': {'territories': 'territories',
            'yellowknife': 'yellowknife, NT',
            },
        'nova_scotia': {'halifax': 'Halifax'
            },
        'ontario': {'barrie': 'barrie, ON',
            'belleville': 'belleville, ON',
            'brantford': 'brantford-woodstock',
            'chatham': 'chatham-kent, ON',
            'cornwall': 'cornwall, ON',
            'guelph': 'guelph, ON',
            'hamilton': 'hamilton-burlington',
            'kingston': 'kingston, ON',
            'kitchener': 'kitchener-waterloo-cambridge',
            'londonon': 'london, ON',
            'niagara': 'niagara region',
            'ottawa': 'ottawa-hull-gatineau',
            'owensound': 'owen sound, ON',
            'peterborough': 'peterborough, ON',
            'sarnia': 'sarnia, ON',
            'soo': 'sault ste marie, ON',
            'sudbury': 'sudbury, ON',
            'thunderbay': 'thunder bay, ON',
            'toronto': 'toronto',
            'windsor': 'windsor, ON',
            'focus_dist': {'toronto': ['tor', 'drh', 'yrk', 'bra', 'mss', 'oak']
                }
            },
        'prince_edward_island': {'pei': 'Pei'
            },
        'quebec': {'montreal': 'montreal, QC',
            'quebec': 'Québec (ville)',
            'saguenay': 'saguenay, QC',
            'sherbrooke': 'sherbrooke, QC',
            'troisrivieres': 'trois-rivieres, QC',
            },
        'saskatchewan': {'regina': 'regina, SK',
            'saskatoon': 'saskatoon, SK',
            },
        'yukon_territory': {'whitehorse': 'Whitehorse'
            }
    }
    territories = {'micronesia': 'guam-micronesia',
	'puertorico': 'puerto rico',
	'virgin': 'virgin islands'
    }
    austria = {'vienna': 'Vienna'
    }
    belgium = {'brussels': 'Brussels'
    }
    bulgaria = {'bulgaria': 'Bulgaria'
    }
    croatia = {'zagreb': 'Zagreb'
    }
    czech_republic = {'prague': 'Prague'
    }
    denmark = {'copenhagen': 'Copenhagen'
    }
    finland = {'helsinki': 'Helsinki'
    }
    france = {'bordeaux': 'Bordeaux',
        'rennes': 'Bretagne',
        'grenoble': 'Grenoble',
        'lille': 'Lille',
        'loire': 'Loire (vallée)',
        'lyon': 'Lyon',
        'marseilles': 'Marseille',
        'montpellier': 'Montpellier',
        'cotedazur': "Nice / Côte d'Azur",
        'rouen': 'Normandie',
        'paris': 'Paris, FR',
        'strasbourg': 'Strasbourg',
        'toulouse': 'Toulouse'
    }
    germany = {'berlin': 'Berlin',
        'bremen': 'Bremen',
        'cologne': 'Köln',
        'dresden': 'Dresden',
        'dusseldorf': 'Düsseldorf',
        'essen': 'Essen / Ruhr',
        'frankfurt': 'Frankfurt',
        'hamburg': 'Hamburg',
        'hannover': 'Hannover',
        'heidelberg': 'Heidelberg',
        'kaiserslautern': 'Kaiserslautern',
        'leipzig': 'Leipzig',
        'munich': 'München',
        'nuremberg': 'Nürnberg',
        'stuttgart': 'Stuttgart'
    }
    greece = {'athens': 'Athens'
    }
    hungary = {'budapest': 'Budapest'
    }
    iceland = {'reykjavik': 'Reykjavik'
    }
    ireland = {'dublin': 'Dublin'
    }
    italy = {'bologna': 'bologna',
        'florence': 'firenze / toscana',
        'genoa': 'genova',
        'milan': 'milano',
        'naples': 'napoli / campania',
        'perugia': 'perugia',
        'rome': 'roma',
        'sardinia': 'sardegna',
        'sicily': 'sicilia',
        'torino': 'torino',
        'venice': 'venezia / veneto'
    }
    luxembourg = {'luxembourg': 'Luxembourg'
    }
    netherlands = {'amsterdam': 'Amsterdam'
    }
    norway = {'oslo': 'Oslo'
    }
    poland = {'warsaw': 'Warsaw'
    }
    portugal = {'faro': 'Faro / Algarve',
        'lisbon': 'Lisboa',
        'porto': 'Porto'
    }
    romania = {'bucharest': 'Bucharest'
    }
    russian_federation = {'moscow': 'москва',
        'stpetersburg': 'с. петербург, RU'
    }
    spain = {'alicante': 'Alicante',
        'baleares': 'Baleares',
        'barcelona': 'barcelona',
        'bilbao': 'Bilbao',
        'cadiz': 'cádiz',
        'canarias': 'Canarias',
        'granada': 'Granada',
        'madrid': 'madrid',
        'malaga': 'málaga',
        'sevilla': 'sevilla',
        'valencia': 'valencia'
    }
    sweden = {'stockholm': 'Stockholm'
    }
    switzerland = {'basel': 'Basel',
        'bern': 'Bern',
        'geneva': 'Genève',
        'lausanne': 'Lausanne',
        'zurich': 'Zürich'
    }
    turkey = {'istanbul': 'Istanbul'
    }
    ukraine = {'ukraine': 'Ukraine'
    }
    united_kingdom = {'aberdeen': 'Aberdeen',
        'bath': 'bath, UK',
        'belfast': 'Belfast',
        'birmingham': 'Birmingham / West Mids',
        'brighton': 'Brighton',
        'bristol': 'Bristol',
        'cambridge': 'Cambridge, UK',
        'cardiff': 'Cardiff / Wales',
        'coventry': 'coventry, UK',
        'derby': 'derby, UK',
        'devon': 'Devon &amp; Cornwall',
        'dundee': 'Dundee',
        'norwich': 'East Anglia',
        'eastmids': 'East Midlands',
        'edinburgh': 'Edinburgh',
        'essex': 'essex, UK',
        'glasgow': 'Glasgow',
        'hampshire': 'Hampshire',
        'kent': 'kent, UK',
        'leeds': 'Leeds',
        'liverpool': 'Liverpool',
        'london': 'london, UK',
        'manchester': 'manchester, UK',
        'newcastle': 'Newcastle / NE England',
        'nottingham': 'nottingham, UK',
        'oxford': 'oxford, UK',
        'sheffield': 'Sheffield'
    }
    bangladesh = {'bangladesh': 'Bangladesh'
    }
    china = {'beijing': '北京 ',
        'chengdu': '成都',
        'chongqing': '重庆',
        'dalian': '大连 ',
        'guangzhou': '广州',
        'hangzhou': '杭州',
        'nanjing': '南京',
        'shanghai': '上海 ',
        'shenyang': '沈阳',
        'shenzhen': '深圳',
        'wuhan': '武汉',
        'xian': '西安'
    }
    guam_micronesia = {'micronesia': 'Micronesia'
    }
    hong_kong = {'hongkong': 'Hongkong'
    }
    india = {'ahmedabad': 'ahmedabad',
        'bangalore': 'bangalore',
        'bhubaneswar': 'bhubaneswar',
        'chandigarh': 'chandigarh',
        'chennai': 'chennai (madras)',
        'delhi': 'delhi',
        'goa': 'goa',
        'hyderabad': 'hyderabad',
        'indore': 'indore',
        'jaipur': 'jaipur',
        'kerala': 'kerala',
        'kolkata': 'kolkata (calcutta)',
        'lucknow': 'lucknow',
        'mumbai': 'mumbai',
        'pune': 'pune',
        'surat': 'surat surat'
    }
    indonesia = {'jakarta': 'Jakarta'
    }
    iran = {'tehran': 'Tehran'
    }
    iraq = {'baghdad': 'Baghdad'
    }
    israel_and_palestine = {'haifa': 'haifa',
        'jerusalem': 'jerusalem',
        'telaviv': 'tel aviv',
        'ramallah': 'west bank'
    }
    japan = {'fukuoka': '福岡',
        'hiroshima': '広島',
        'nagoya': '名古屋',
        'okinawa': '沖縄',
        'osaka': '大阪・神戸・京都',
        'sapporo': '札幌',
        'sendai': '仙台',
        'tokyo': '東京'
    }
    korea = {'seoul': 'Seoul'
    }
    kuwait = {'kuwait': 'Kuwait'
    }
    lebanon = {'beirut': 'Beirut'
    }
    malaysia = {'malaysia': 'Malaysia'
    }
    pakistan = {'pakistan': 'Pakistan'
    }
    philippines = {'bacolod': 'bacolod',
        'naga': 'bicol region',
        'cdo': 'cagayan de oro',
        'cebu': 'cebu',
        'davaocity': 'davao city',
        'iloilo': 'iloilo',
        'manila': 'manila',
        'pampanga': 'pampanga',
        'zamboanga': 'zamboanga'
    }
    singapore = {'singapore': 'Singapore'
    }
    taiwan = {'taipei': 'Taipei'
    }
    thailand = {'bangkok': 'Bangkok'
    }
    united_arab_emirates = {'dubai': 'Dubai'
    }
    vietnam = {'vietnam': 'Vietnam'
    }
    australia = {'adelaide': 'adelaide, SA',
        'brisbane': 'brisbane, QLD',
        'cairns': 'cairns, QLD',
        'canberra': 'canberra, ACT',
        'darwin': 'darwin, NT',
        'goldcoast': 'Gold Coast',
        'melbourne': 'melbourne, VIC',
        'ntl': 'Newcastle, NSW',
        'perth': 'perth, WA',
        'sydney': 'sydney, NSW',
        'hobart': 'Tasmania',
        'wollongong': 'wollongong, NSW'
    }
    new_zealand = {'auckland': 'auckland, NZ',
        'christchurch': 'christchurch',
        'dunedin': 'dunedin, NZ',
        'wellington': 'wellington'
    }
    argentina = {'buenosaires': 'Buenosaires'
    }
    bolivia = {'lapaz': 'Lapaz'
    }
    brazil = {'belohorizonte': 'Belo Horizonte',
        'brasilia': 'Brasília',
        'curitiba': 'Curitiba',
        'fortaleza': 'Fortaleza',
        'portoalegre': 'Porto Alegre',
        'recife': 'Recife',
        'rio': 'Rio de Janeiro',
        'salvador': 'Salvador, Bahia',
        'saopaulo': 'São Paulo'
    }
    caribbean_islands = {'caribbean': 'Caribbean'
    }
    chile = {'santiago': 'Santiago'
    }
    colombia = {'colombia': 'Colombia'
    }
    costa_rica = {'costarica': 'Costarica'
    }
    dominican_republic = {'santodomingo': 'Santodomingo'
    }
    ecuador = {'quito': 'Quito'
    }
    el_salvador = {'elsalvador': 'Elsalvador'
    }
    guatemala = {'guatemala': 'Guatemala'
    }
    mexico = {'acapulco': 'acapulco',
        'bajasur': 'baja california sur',
        'chihuahua': 'chihuahua',
        'juarez': 'ciudad juárez',
        'guadalajara': 'guadalajara, MX',
        'guanajuato': 'guanajuato',
        'hermosillo': 'hermosillo',
        'mazatlan': 'mazatlán',
        'mexicocity': 'ciudad de méxico',
        'monterrey': 'monterrey',
        'oaxaca': 'oaxaca',
        'puebla': 'puebla, MX',
        'pv': 'puerto vallarta',
        'tijuana': 'tijuana, MX',
        'veracruz': 'veracruz',
        'yucatan': 'yucatán'
    }
    nicaragua = {'managua': 'Managua'
    }
    panama = {'panama': 'Panama'
    }
    peru = {'lima': 'Lima'
    }
    puerto_rico = {'puertorico': 'Puertorico'
    }
    uruguay = {'montevideo': 'Montevideo'
    }
    venezuela = {'caracas': 'Caracas'
    }
    virgin_islands_us = {'virgin': 'Virgin'
    }
    egypt = {'cairo': 'Cairo'
    }
    ethiopia = {'addisababa': 'Addisababa'
    }
    ghana = {'accra': 'Accra'
    }
    kenya = {'kenya': 'Kenya'
    }
    morocco = {'casablanca': 'Casablanca'
    }
    south_africa = {'capetown': 'Cape Town',
        'durban': 'Durban',
        'johannesburg': 'Johannesburg',
        'pretoria': 'Pretoria'
    }
    tunisia = {'tunis': 'tunisia'
    }