r"""A collection of relevant constants used throughout Tropycal scripts."""
from matplotlib import path

#Tropical or subtropical storm types (including depressions)
TROPICAL_STORM_TYPES = frozenset(['SD','SS','TD','TS','HU','TY','ST'])

#Tropical or subtropical storm types (excluding depressions)
NAMED_TROPICAL_STORM_TYPES = frozenset(['SS','TS','HU','TY','ST'])

#Tropical only storm types
TROPICAL_ONLY_STORM_TYPES = frozenset(['TD','TS','HU','TY','ST'])

#Tropical only storm types
SUBTROPICAL_ONLY_STORM_TYPES = frozenset(['SD','SS'])

#Standard 00/06/12/18 UTC hours
STANDARD_HOURS = frozenset(['0000','0600','1200','1800'])

#Accepted basins
ALL_BASINS = frozenset(['north_atlantic','east_pacific','west_pacific','north_indian','south_atlantic','south_indian','australia','south_pacific'])

#Accepted NHC basins
NHC_BASINS = frozenset(['north_atlantic','east_pacific'])

#NHC Cone Radii, in nautical miles
CONE_SIZE_ATL = {
    2022: [16,26,39,52,67,84,100,142,200],
    2021: [16,27,40,55,69,86,102,148,200],
    2020: [16,26,41,55,69,86,103,151,196],
    2019: [16,26,41,54,68,102,151,198],
    2018: [16,26,43,56,74,103,151,198],
    2017: [16,29,45,63,78,107,159,211],
    2016: [16,30,49,66,84,115,165,237],
    2015: [16,32,52,71,90,122,170,225],
    2014: [16,33,52,72,92,125,170,226],
    2013: [16,33,52,72,92,128,177,229],
    2012: [16,36,56,75,95,141,180,236],
    2011: [16,36,59,79,98,144,190,239],
    2010: [16,36,62,85,108,161,220,285],
    2009: [16,36,62,89,111,167,230,302],
    2008: [16,39,67,92,118,170,233,305],
}

CONE_SIZE_PAC = {
    2022: [16,25,38,51,65,79,93,120,146],
    2021: [16,25,37,51,64,77,89,114,138],
    2020: [16,25,38,51,65,78,91,115,138],
    2019: [16,25,38,48,62,88,115,145],
    2018: [16,25,39,50,66,94,125,162],
    2017: [16,25,40,51,66,93,116,151],
    2016: [16,27,42,55,70,100,137,172],
    2015: [16,26,42,54,69,100,143,182],
    2014: [16,30,46,62,79,105,154,190],
    2013: [16,30,49,66,82,111,157,197],
    2012: [16,33,52,72,89,121,170,216],
    2011: [16,33,59,79,98,134,187,230],
    2010: [16,36,59,82,102,138,174,220],
    2009: [16,36,59,85,105,148,187,230],
    2008: [16,36,66,92,115,161,210,256],
}

#Create path for Pacific (Atlantic crossover into Pacific)
points = [[7.21, -80.930362], [8.081609, -81.765323], [8.472996, -83.632999], [9.037626, -83.654972], [9.612204, -84.753604], [9.893720, -85.676456], [10.423608, -85.852237], [10.666626, -85.665470], [11.055048, -85.714908], [12.195689, -86.802555], [13.154990, -87.890201], [13.534473, -89.801822], [13.892023, -90.532413], [13.929348, -91.208072], [14.190449, -91.806827], [15.205295, -92.916446], [15.861564, -93.729435], [16.199455, -94.685245], [16.154315, -95.220816], [15.842772, -95.869010], [15.684175, -96.396353], [15.795206, -96.995108], [17.269657, -101.038077], [18.331367, -103.493521], [18.820821, -103.894522], [19.163633, -104.685538], [19.376235, -105.037100], [20.383552, -105.685294], [20.995079, -105.333731], [21.368986, -105.234854], [22.001926, -105.646842], [22.337671, -105.668814], [23.878597, -106.921256], [25.866927, -109.459098], [26.379855, -109.211905], [26.694378, -109.448111], [26.733633, -109.821646], [27.081423, -109.945243], [27.171868, -110.343497], [27.625425, -110.637381], [27.861216, -110.563224], [27.934037, -111.085074], [28.736637, -111.952994], [30.805827, -113.150504], [32.600318, -117.193473], [40.05, -124.081901], [89.0, -124.08], [89.0, -179.9], [0.1, -179.9], [0.1, -80.930362], [7.21, -80.930362]]
points = [[i[0],i[1]+360.0] for i in points]
PATH_PACIFIC = path.Path(points)

#Create path for Atlantic (Pacific crossover into Atlantic)
points = [[8.517611, -77.062646], [8.8, -81.6],[10.053014, -83.124868],[11.176022, -83.806021],[14.219437, -83.278677],[15.197045, -83.366568],[15.789919, -84.311392],[15.958997, -85.102408],[15.974841, -85.789053],[15.758202, -86.937124],[15.906175, -87.695181],[15.689463, -88.156607],[15.869192, -88.491690],[15.974841, -88.925650],[16.399290, -88.464083],[16.946558, -88.227877],[19.077781, -87.552218],[20.097293, -87.524752],[20.822962, -86.898532],[21.156325, -86.799655],[21.514493, -86.975436],[21.616666, -88.123507],[21.151079, -90.102868],[20.938318, -90.380273],[20.022350, -90.501123],[19.733061, -90.682397],[19.313698, -90.753808],[18.789280, -91.533838],[18.659219, -92.478662],[18.466546, -92.841211],[18.430070, -93.407007],[18.221488, -94.143090],[18.143204, -94.494653],[18.508224, -94.807763],[18.700850, -95.186792],[18.742470, -95.719629],[19.355165, -96.318384],[19.836439, -96.450219],[20.738098, -97.175317],[22.108507, -97.768579],[25.187509, -97.702661],[27.724832, -97.197290],[29.212076, -94.978052], [35.8, -95.4], [35.8, -0.1], [0.1, -0.1], [0.1, -77.062646], [8.517611, -77.062646]]
points = [[i[0],i[1]+360.0] for i in points]
PATH_ATLANTIC = path.Path(points)