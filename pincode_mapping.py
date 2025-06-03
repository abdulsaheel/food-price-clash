"""
Pincode to City Mapping Module
Maps Indian pincodes to their nearest supported cities for food delivery services
"""

# Major Indian cities with pincode ranges and their delivery areas
PINCODE_CITY_MAPPING = {
    # Delhi NCR
    "110001": "Delhi NCR", "110002": "Delhi NCR", "110003": "Delhi NCR", "110004": "Delhi NCR",
    "110005": "Delhi NCR", "110006": "Delhi NCR", "110007": "Delhi NCR", "110008": "Delhi NCR",
    "110009": "Delhi NCR", "110010": "Delhi NCR", "110011": "Delhi NCR", "110012": "Delhi NCR",
    "110013": "Delhi NCR", "110014": "Delhi NCR", "110015": "Delhi NCR", "110016": "Delhi NCR",
    "110017": "Delhi NCR", "110018": "Delhi NCR", "110019": "Delhi NCR", "110020": "Delhi NCR",
    "110021": "Delhi NCR", "110022": "Delhi NCR", "110023": "Delhi NCR", "110024": "Delhi NCR",
    "110025": "Delhi NCR", "110026": "Delhi NCR", "110027": "Delhi NCR", "110028": "Delhi NCR",
    "110029": "Delhi NCR", "110030": "Delhi NCR", "110031": "Delhi NCR", "110032": "Delhi NCR",
    "110033": "Delhi NCR", "110034": "Delhi NCR", "110035": "Delhi NCR", "110036": "Delhi NCR",
    "110037": "Delhi NCR", "110038": "Delhi NCR", "110039": "Delhi NCR", "110040": "Delhi NCR",
    "110041": "Delhi NCR", "110042": "Delhi NCR", "110043": "Delhi NCR", "110044": "Delhi NCR",
    "110045": "Delhi NCR", "110046": "Delhi NCR", "110047": "Delhi NCR", "110048": "Delhi NCR",
    "110049": "Delhi NCR", "110050": "Delhi NCR", "110051": "Delhi NCR", "110052": "Delhi NCR",
    "110053": "Delhi NCR", "110054": "Delhi NCR", "110055": "Delhi NCR", "110056": "Delhi NCR",
    "110057": "Delhi NCR", "110058": "Delhi NCR", "110059": "Delhi NCR", "110060": "Delhi NCR",
    "110061": "Delhi NCR", "110062": "Delhi NCR", "110063": "Delhi NCR", "110064": "Delhi NCR",
    "110065": "Delhi NCR", "110066": "Delhi NCR", "110067": "Delhi NCR", "110068": "Delhi NCR",
    "110069": "Delhi NCR", "110070": "Delhi NCR", "110071": "Delhi NCR", "110072": "Delhi NCR",
    "110073": "Delhi NCR", "110074": "Delhi NCR", "110075": "Delhi NCR", "110076": "Delhi NCR",
    "110077": "Delhi NCR", "110078": "Delhi NCR", "110079": "Delhi NCR", "110080": "Delhi NCR",
    "110081": "Delhi NCR", "110082": "Delhi NCR", "110083": "Delhi NCR", "110084": "Delhi NCR",
    "110085": "Delhi NCR", "110086": "Delhi NCR", "110087": "Delhi NCR", "110088": "Delhi NCR",
    "110089": "Delhi NCR", "110090": "Delhi NCR", "110091": "Delhi NCR", "110092": "Delhi NCR",
    "110093": "Delhi NCR", "110094": "Delhi NCR", "110095": "Delhi NCR", "110096": "Delhi NCR",
    "110097": "Delhi NCR", "110098": "Delhi NCR", "110099": "Delhi NCR",
    
    # Gurgaon (Part of Delhi NCR)
    "122001": "Delhi NCR", "122002": "Delhi NCR", "122003": "Delhi NCR", "122004": "Delhi NCR",
    "122005": "Delhi NCR", "122006": "Delhi NCR", "122007": "Delhi NCR", "122008": "Delhi NCR",
    "122009": "Delhi NCR", "122010": "Delhi NCR", "122011": "Delhi NCR", "122015": "Delhi NCR",
    "122016": "Delhi NCR", "122017": "Delhi NCR", "122018": "Delhi NCR", "122022": "Delhi NCR",
    
    # Noida (Part of Delhi NCR) 
    "201301": "Delhi NCR", "201302": "Delhi NCR", "201303": "Delhi NCR", "201304": "Delhi NCR",
    "201305": "Delhi NCR", "201306": "Delhi NCR", "201307": "Delhi NCR", "201308": "Delhi NCR",
    "201309": "Delhi NCR", "201310": "Delhi NCR", "201311": "Delhi NCR", "201312": "Delhi NCR",
    "201313": "Delhi NCR", "201314": "Delhi NCR", "201315": "Delhi NCR", "201316": "Delhi NCR",
    "201317": "Delhi NCR", "201318": "Delhi NCR",
    
    # Faridabad (Part of Delhi NCR)
    "121001": "Delhi NCR", "121002": "Delhi NCR", "121003": "Delhi NCR", "121004": "Delhi NCR",
    "121005": "Delhi NCR", "121006": "Delhi NCR", "121007": "Delhi NCR", "121008": "Delhi NCR",
    "121009": "Delhi NCR", "121010": "Delhi NCR", "121011": "Delhi NCR", "121012": "Delhi NCR",
    "121013": "Delhi NCR", "121014": "Delhi NCR", "121015": "Delhi NCR",
    
    # Mumbai
    "400001": "Mumbai", "400002": "Mumbai", "400003": "Mumbai", "400004": "Mumbai",
    "400005": "Mumbai", "400006": "Mumbai", "400007": "Mumbai", "400008": "Mumbai",
    "400009": "Mumbai", "400010": "Mumbai", "400011": "Mumbai", "400012": "Mumbai",
    "400013": "Mumbai", "400014": "Mumbai", "400015": "Mumbai", "400016": "Mumbai",
    "400017": "Mumbai", "400018": "Mumbai", "400019": "Mumbai", "400020": "Mumbai",
    "400021": "Mumbai", "400022": "Mumbai", "400023": "Mumbai", "400024": "Mumbai",
    "400025": "Mumbai", "400026": "Mumbai", "400027": "Mumbai", "400028": "Mumbai",
    "400029": "Mumbai", "400030": "Mumbai", "400031": "Mumbai", "400032": "Mumbai",
    "400033": "Mumbai", "400034": "Mumbai", "400035": "Mumbai", "400036": "Mumbai",
    "400037": "Mumbai", "400038": "Mumbai", "400039": "Mumbai", "400040": "Mumbai",
    "400041": "Mumbai", "400042": "Mumbai", "400043": "Mumbai", "400044": "Mumbai",
    "400045": "Mumbai", "400046": "Mumbai", "400047": "Mumbai", "400048": "Mumbai",
    "400049": "Mumbai", "400050": "Mumbai", "400051": "Mumbai", "400052": "Mumbai",
    "400053": "Mumbai", "400054": "Mumbai", "400055": "Mumbai", "400056": "Mumbai",
    "400057": "Mumbai", "400058": "Mumbai", "400059": "Mumbai", "400060": "Mumbai",
    "400061": "Mumbai", "400062": "Mumbai", "400063": "Mumbai", "400064": "Mumbai",
    "400065": "Mumbai", "400066": "Mumbai", "400067": "Mumbai", "400068": "Mumbai",
    "400069": "Mumbai", "400070": "Mumbai", "400071": "Mumbai", "400072": "Mumbai",
    "400073": "Mumbai", "400074": "Mumbai", "400075": "Mumbai", "400076": "Mumbai",
    "400077": "Mumbai", "400078": "Mumbai", "400079": "Mumbai", "400080": "Mumbai",
    "400081": "Mumbai", "400082": "Mumbai", "400083": "Mumbai", "400084": "Mumbai",
    "400085": "Mumbai", "400086": "Mumbai", "400087": "Mumbai", "400088": "Mumbai",
    "400089": "Mumbai", "400090": "Mumbai", "400091": "Mumbai", "400092": "Mumbai",
    "400093": "Mumbai", "400094": "Mumbai", "400095": "Mumbai", "400096": "Mumbai",
    "400097": "Mumbai", "400098": "Mumbai", "400099": "Mumbai", "400100": "Mumbai",
    "400101": "Mumbai", "400102": "Mumbai", "400103": "Mumbai", "400104": "Mumbai",
    
    # Bengaluru
    "560001": "Bengaluru", "560002": "Bengaluru", "560003": "Bengaluru", "560004": "Bengaluru",
    "560005": "Bengaluru", "560006": "Bengaluru", "560007": "Bengaluru", "560008": "Bengaluru",
    "560009": "Bengaluru", "560010": "Bengaluru", "560011": "Bengaluru", "560012": "Bengaluru",
    "560013": "Bengaluru", "560014": "Bengaluru", "560015": "Bengaluru", "560016": "Bengaluru",
    "560017": "Bengaluru", "560018": "Bengaluru", "560019": "Bengaluru", "560020": "Bengaluru",
    "560021": "Bengaluru", "560022": "Bengaluru", "560023": "Bengaluru", "560024": "Bengaluru",
    "560025": "Bengaluru", "560026": "Bengaluru", "560027": "Bengaluru", "560028": "Bengaluru",
    "560029": "Bengaluru", "560030": "Bengaluru", "560031": "Bengaluru", "560032": "Bengaluru",
    "560033": "Bengaluru", "560034": "Bengaluru", "560035": "Bengaluru", "560036": "Bengaluru",
    "560037": "Bengaluru", "560038": "Bengaluru", "560039": "Bengaluru", "560040": "Bengaluru",
    "560041": "Bengaluru", "560042": "Bengaluru", "560043": "Bengaluru", "560044": "Bengaluru",
    "560045": "Bengaluru", "560046": "Bengaluru", "560047": "Bengaluru", "560048": "Bengaluru",
    "560049": "Bengaluru", "560050": "Bengaluru", "560051": "Bengaluru", "560052": "Bengaluru",
    "560053": "Bengaluru", "560054": "Bengaluru", "560055": "Bengaluru", "560056": "Bengaluru",
    "560057": "Bengaluru", "560058": "Bengaluru", "560059": "Bengaluru", "560060": "Bengaluru",
    "560061": "Bengaluru", "560062": "Bengaluru", "560063": "Bengaluru", "560064": "Bengaluru",
    "560065": "Bengaluru", "560066": "Bengaluru", "560067": "Bengaluru", "560068": "Bengaluru",
    "560069": "Bengaluru", "560070": "Bengaluru", "560071": "Bengaluru", "560072": "Bengaluru",
    "560073": "Bengaluru", "560074": "Bengaluru", "560075": "Bengaluru", "560076": "Bengaluru",
    "560077": "Bengaluru", "560078": "Bengaluru", "560079": "Bengaluru", "560080": "Bengaluru",
    "560081": "Bengaluru", "560082": "Bengaluru", "560083": "Bengaluru", "560084": "Bengaluru",
    "560085": "Bengaluru", "560086": "Bengaluru", "560087": "Bengaluru", "560088": "Bengaluru",
    "560089": "Bengaluru", "560090": "Bengaluru", "560091": "Bengaluru", "560092": "Bengaluru",
    "560093": "Bengaluru", "560094": "Bengaluru", "560095": "Bengaluru", "560096": "Bengaluru",
    "560097": "Bengaluru", "560098": "Bengaluru", "560099": "Bengaluru", "560100": "Bengaluru",
    
    # Hyderabad
    "500001": "Hyderabad", "500002": "Hyderabad", "500003": "Hyderabad", "500004": "Hyderabad",
    "500005": "Hyderabad", "500006": "Hyderabad", "500007": "Hyderabad", "500008": "Hyderabad",
    "500009": "Hyderabad", "500010": "Hyderabad", "500011": "Hyderabad", "500012": "Hyderabad",
    "500013": "Hyderabad", "500014": "Hyderabad", "500015": "Hyderabad", "500016": "Hyderabad",
    "500017": "Hyderabad", "500018": "Hyderabad", "500019": "Hyderabad", "500020": "Hyderabad",
    "500021": "Hyderabad", "500022": "Hyderabad", "500023": "Hyderabad", "500024": "Hyderabad",
    "500025": "Hyderabad", "500026": "Hyderabad", "500027": "Hyderabad", "500028": "Hyderabad",
    "500029": "Hyderabad", "500030": "Hyderabad", "500031": "Hyderabad", "500032": "Hyderabad",
    "500033": "Hyderabad", "500034": "Hyderabad", "500035": "Hyderabad", "500036": "Hyderabad",
    "500037": "Hyderabad", "500038": "Hyderabad", "500039": "Hyderabad", "500040": "Hyderabad",
    "500041": "Hyderabad", "500042": "Hyderabad", "500043": "Hyderabad", "500044": "Hyderabad",
    "500045": "Hyderabad", "500046": "Hyderabad", "500047": "Hyderabad", "500048": "Hyderabad",
    "500049": "Hyderabad", "500050": "Hyderabad", "500051": "Hyderabad", "500052": "Hyderabad",
    "500053": "Hyderabad", "500054": "Hyderabad", "500055": "Hyderabad", "500056": "Hyderabad",
    "500057": "Hyderabad", "500058": "Hyderabad", "500059": "Hyderabad", "500060": "Hyderabad",
    "500061": "Hyderabad", "500062": "Hyderabad", "500063": "Hyderabad", "500064": "Hyderabad",
    "500065": "Hyderabad", "500066": "Hyderabad", "500067": "Hyderabad", "500068": "Hyderabad",
    "500069": "Hyderabad", "500070": "Hyderabad", "500071": "Hyderabad", "500072": "Hyderabad",
    "500073": "Hyderabad", "500074": "Hyderabad", "500075": "Hyderabad", "500076": "Hyderabad",
    "500077": "Hyderabad", "500078": "Hyderabad", "500079": "Hyderabad", "500080": "Hyderabad",
    "500081": "Hyderabad", "500082": "Hyderabad", "500083": "Hyderabad", "500084": "Hyderabad",
    "500085": "Hyderabad", "500086": "Hyderabad", "500087": "Hyderabad", "500088": "Hyderabad",
    "500089": "Hyderabad", "500090": "Hyderabad", "500091": "Hyderabad", "500092": "Hyderabad",
    "500093": "Hyderabad", "500094": "Hyderabad", "500095": "Hyderabad", "500096": "Hyderabad",
    "500097": "Hyderabad", "500098": "Hyderabad", "500099": "Hyderabad", "500100": "Hyderabad",
    
    # Chennai
    "600001": "Chennai", "600002": "Chennai", "600003": "Chennai", "600004": "Chennai",
    "600005": "Chennai", "600006": "Chennai", "600007": "Chennai", "600008": "Chennai",
    "600009": "Chennai", "600010": "Chennai", "600011": "Chennai", "600012": "Chennai",
    "600013": "Chennai", "600014": "Chennai", "600015": "Chennai", "600016": "Chennai",
    "600017": "Chennai", "600018": "Chennai", "600019": "Chennai", "600020": "Chennai",
    "600021": "Chennai", "600022": "Chennai", "600023": "Chennai", "600024": "Chennai",
    "600025": "Chennai", "600026": "Chennai", "600027": "Chennai", "600028": "Chennai",
    "600029": "Chennai", "600030": "Chennai", "600031": "Chennai", "600032": "Chennai",
    "600033": "Chennai", "600034": "Chennai", "600035": "Chennai", "600036": "Chennai",
    "600037": "Chennai", "600038": "Chennai", "600039": "Chennai", "600040": "Chennai",
    "600041": "Chennai", "600042": "Chennai", "600043": "Chennai", "600044": "Chennai",
    "600045": "Chennai", "600046": "Chennai", "600047": "Chennai", "600048": "Chennai",
    "600049": "Chennai", "600050": "Chennai", "600051": "Chennai", "600052": "Chennai",
    "600053": "Chennai", "600054": "Chennai", "600055": "Chennai", "600056": "Chennai",
    "600057": "Chennai", "600058": "Chennai", "600059": "Chennai", "600060": "Chennai",
    "600061": "Chennai", "600062": "Chennai", "600063": "Chennai", "600064": "Chennai",
    "600065": "Chennai", "600066": "Chennai", "600067": "Chennai", "600068": "Chennai",
    "600069": "Chennai", "600070": "Chennai", "600071": "Chennai", "600072": "Chennai",
    "600073": "Chennai", "600074": "Chennai", "600075": "Chennai", "600076": "Chennai",
    "600077": "Chennai", "600078": "Chennai", "600079": "Chennai", "600080": "Chennai",
    "600081": "Chennai", "600082": "Chennai", "600083": "Chennai", "600084": "Chennai",
    "600085": "Chennai", "600086": "Chennai", "600087": "Chennai", "600088": "Chennai",
    "600089": "Chennai", "600090": "Chennai", "600091": "Chennai", "600092": "Chennai",
    "600093": "Chennai", "600094": "Chennai", "600095": "Chennai", "600096": "Chennai",
    "600097": "Chennai", "600098": "Chennai", "600099": "Chennai", "600100": "Chennai",
    
    # Pune
    "411001": "Pune", "411002": "Pune", "411003": "Pune", "411004": "Pune",
    "411005": "Pune", "411006": "Pune", "411007": "Pune", "411008": "Pune",
    "411009": "Pune", "411010": "Pune", "411011": "Pune", "411012": "Pune",
    "411013": "Pune", "411014": "Pune", "411015": "Pune", "411016": "Pune",
    "411017": "Pune", "411018": "Pune", "411019": "Pune", "411020": "Pune",
    "411021": "Pune", "411022": "Pune", "411023": "Pune", "411024": "Pune",
    "411025": "Pune", "411026": "Pune", "411027": "Pune", "411028": "Pune",
    "411029": "Pune", "411030": "Pune", "411031": "Pune", "411032": "Pune",
    "411033": "Pune", "411034": "Pune", "411035": "Pune", "411036": "Pune",
    "411037": "Pune", "411038": "Pune", "411039": "Pune", "411040": "Pune",
    "411041": "Pune", "411042": "Pune", "411043": "Pune", "411044": "Pune",
    "411045": "Pune", "411046": "Pune", "411047": "Pune", "411048": "Pune",
    "411049": "Pune", "411050": "Pune", "411051": "Pune", "411052": "Pune",
    "411057": "Pune", "411058": "Pune",
    
    # Ahmedabad
    "380001": "Ahmedabad", "380002": "Ahmedabad", "380003": "Ahmedabad", "380004": "Ahmedabad",
    "380005": "Ahmedabad", "380006": "Ahmedabad", "380007": "Ahmedabad", "380008": "Ahmedabad",
    "380009": "Ahmedabad", "380010": "Ahmedabad", "380011": "Ahmedabad", "380012": "Ahmedabad",
    "380013": "Ahmedabad", "380014": "Ahmedabad", "380015": "Ahmedabad", "380016": "Ahmedabad",
    "380017": "Ahmedabad", "380018": "Ahmedabad", "380019": "Ahmedabad", "380020": "Ahmedabad",
    "380021": "Ahmedabad", "380022": "Ahmedabad", "380023": "Ahmedabad", "380024": "Ahmedabad",
    "380025": "Ahmedabad", "380026": "Ahmedabad", "380027": "Ahmedabad", "380028": "Ahmedabad",
    "380050": "Ahmedabad", "380051": "Ahmedabad", "380052": "Ahmedabad", "380053": "Ahmedabad",
    "380054": "Ahmedabad", "380055": "Ahmedabad", "380058": "Ahmedabad", "380059": "Ahmedabad",
    "380060": "Ahmedabad", "380061": "Ahmedabad", "380063": "Ahmedabad",
    
    # Kolkata
    "700001": "Kolkata", "700002": "Kolkata", "700003": "Kolkata", "700004": "Kolkata",
    "700005": "Kolkata", "700006": "Kolkata", "700007": "Kolkata", "700008": "Kolkata",
    "700009": "Kolkata", "700010": "Kolkata", "700011": "Kolkata", "700012": "Kolkata",
    "700013": "Kolkata", "700014": "Kolkata", "700015": "Kolkata", "700016": "Kolkata",
    "700017": "Kolkata", "700018": "Kolkata", "700019": "Kolkata", "700020": "Kolkata",
    "700021": "Kolkata", "700022": "Kolkata", "700023": "Kolkata", "700024": "Kolkata",
    "700025": "Kolkata", "700026": "Kolkata", "700027": "Kolkata", "700028": "Kolkata",
    "700029": "Kolkata", "700030": "Kolkata", "700031": "Kolkata", "700032": "Kolkata",
    "700033": "Kolkata", "700034": "Kolkata", "700035": "Kolkata", "700036": "Kolkata",
    "700037": "Kolkata", "700038": "Kolkata", "700039": "Kolkata", "700040": "Kolkata",
    "700041": "Kolkata", "700042": "Kolkata", "700043": "Kolkata", "700044": "Kolkata",
    "700045": "Kolkata", "700046": "Kolkata", "700047": "Kolkata", "700048": "Kolkata",
    "700049": "Kolkata", "700050": "Kolkata", "700051": "Kolkata", "700052": "Kolkata",
    "700053": "Kolkata", "700054": "Kolkata", "700055": "Kolkata", "700056": "Kolkata",
    "700057": "Kolkata", "700058": "Kolkata", "700059": "Kolkata", "700060": "Kolkata",
    "700061": "Kolkata", "700062": "Kolkata", "700063": "Kolkata", "700064": "Kolkata",
    "700065": "Kolkata", "700066": "Kolkata", "700067": "Kolkata", "700068": "Kolkata",
    "700069": "Kolkata", "700070": "Kolkata", "700071": "Kolkata", "700072": "Kolkata",
    "700073": "Kolkata", "700074": "Kolkata", "700075": "Kolkata", "700076": "Kolkata",
    "700077": "Kolkata", "700078": "Kolkata", "700079": "Kolkata", "700080": "Kolkata",
    "700081": "Kolkata", "700082": "Kolkata", "700083": "Kolkata", "700084": "Kolkata",
    "700085": "Kolkata", "700086": "Kolkata", "700087": "Kolkata", "700088": "Kolkata",
    "700089": "Kolkata", "700090": "Kolkata", "700091": "Kolkata", "700092": "Kolkata",
    "700093": "Kolkata", "700094": "Kolkata", "700095": "Kolkata", "700096": "Kolkata",
    "700097": "Kolkata", "700098": "Kolkata", "700099": "Kolkata", "700100": "Kolkata",
    
    # Jaipur
    "302001": "Jaipur", "302002": "Jaipur", "302003": "Jaipur", "302004": "Jaipur",
    "302005": "Jaipur", "302006": "Jaipur", "302007": "Jaipur", "302008": "Jaipur",
    "302009": "Jaipur", "302010": "Jaipur", "302011": "Jaipur", "302012": "Jaipur",
    "302013": "Jaipur", "302014": "Jaipur", "302015": "Jaipur", "302016": "Jaipur",
    "302017": "Jaipur", "302018": "Jaipur", "302019": "Jaipur", "302020": "Jaipur",
    "302021": "Jaipur", "302022": "Jaipur", "302023": "Jaipur", "302024": "Jaipur",
    "302025": "Jaipur", "302026": "Jaipur", "302027": "Jaipur", "302028": "Jaipur",
    "302029": "Jaipur", "302030": "Jaipur", "302031": "Jaipur", "302032": "Jaipur",
    "302033": "Jaipur", "302034": "Jaipur", "302035": "Jaipur", "302036": "Jaipur",
    "302037": "Jaipur", "302038": "Jaipur", "302039": "Jaipur", "302040": "Jaipur",
    
    # Kochi
    "682001": "Kochi", "682002": "Kochi", "682003": "Kochi", "682004": "Kochi",
    "682005": "Kochi", "682006": "Kochi", "682007": "Kochi", "682008": "Kochi",
    "682009": "Kochi", "682010": "Kochi", "682011": "Kochi", "682012": "Kochi",
    "682013": "Kochi", "682014": "Kochi", "682015": "Kochi", "682016": "Kochi",
    "682017": "Kochi", "682018": "Kochi", "682019": "Kochi", "682020": "Kochi",
    "682021": "Kochi", "682022": "Kochi", "682023": "Kochi", "682024": "Kochi",
    "682025": "Kochi", "682026": "Kochi", "682027": "Kochi", "682028": "Kochi",
    "682029": "Kochi", "682030": "Kochi", "682031": "Kochi", "682032": "Kochi",
    "682033": "Kochi", "682034": "Kochi", "682035": "Kochi", "682036": "Kochi",
    "682037": "Kochi", "682038": "Kochi", "682039": "Kochi", "682040": "Kochi",
    
    # Lucknow
    "226001": "Lucknow", "226002": "Lucknow", "226003": "Lucknow", "226004": "Lucknow",
    "226005": "Lucknow", "226006": "Lucknow", "226007": "Lucknow", "226008": "Lucknow",
    "226009": "Lucknow", "226010": "Lucknow", "226011": "Lucknow", "226012": "Lucknow",
    "226013": "Lucknow", "226014": "Lucknow", "226015": "Lucknow", "226016": "Lucknow",
    "226017": "Lucknow", "226018": "Lucknow", "226019": "Lucknow", "226020": "Lucknow",
    "226021": "Lucknow", "226022": "Lucknow", "226023": "Lucknow", "226024": "Lucknow",
    "226025": "Lucknow", "226026": "Lucknow", "226027": "Lucknow", "226028": "Lucknow",
    "226029": "Lucknow", "226030": "Lucknow",
    
    # Indore
    "452001": "Indore", "452002": "Indore", "452003": "Indore", "452004": "Indore",
    "452005": "Indore", "452006": "Indore", "452007": "Indore", "452008": "Indore",
    "452009": "Indore", "452010": "Indore", "452011": "Indore", "452012": "Indore",
    "452013": "Indore", "452014": "Indore", "452015": "Indore", "452016": "Indore",
    "452017": "Indore", "452018": "Indore", "452020": "Indore",
    
    # Bhopal
    "462001": "Bhopal", "462002": "Bhopal", "462003": "Bhopal", "462004": "Bhopal",
    "462005": "Bhopal", "462006": "Bhopal", "462007": "Bhopal", "462008": "Bhopal",
    "462009": "Bhopal", "462010": "Bhopal", "462011": "Bhopal", "462012": "Bhopal",
    "462013": "Bhopal", "462014": "Bhopal", "462015": "Bhopal", "462016": "Bhopal",
    "462017": "Bhopal", "462018": "Bhopal", "462019": "Bhopal", "462020": "Bhopal",
    "462021": "Bhopal", "462022": "Bhopal", "462023": "Bhopal", "462024": "Bhopal",
    "462025": "Bhopal", "462026": "Bhopal", "462027": "Bhopal", "462028": "Bhopal",
    "462029": "Bhopal", "462030": "Bhopal", "462031": "Bhopal", "462032": "Bhopal",
    "462033": "Bhopal", "462034": "Bhopal", "462035": "Bhopal", "462036": "Bhopal",
    "462037": "Bhopal", "462038": "Bhopal", "462039": "Bhopal", "462040": "Bhopal",
    "462041": "Bhopal", "462042": "Bhopal", "462043": "Bhopal", "462044": "Bhopal",
    "462045": "Bhopal", "462046": "Bhopal",
    
    # Chandigarh
    "160001": "Chandigarh", "160002": "Chandigarh", "160003": "Chandigarh", "160004": "Chandigarh",
    "160005": "Chandigarh", "160006": "Chandigarh", "160007": "Chandigarh", "160008": "Chandigarh",
    "160009": "Chandigarh", "160010": "Chandigarh", "160011": "Chandigarh", "160012": "Chandigarh",
    "160013": "Chandigarh", "160014": "Chandigarh", "160015": "Chandigarh", "160016": "Chandigarh",
    "160017": "Chandigarh", "160018": "Chandigarh", "160019": "Chandigarh", "160020": "Chandigarh",
    "160021": "Chandigarh", "160022": "Chandigarh", "160023": "Chandigarh", "160024": "Chandigarh",
    "160025": "Chandigarh", "160026": "Chandigarh", "160027": "Chandigarh", "160028": "Chandigarh",
    "160029": "Chandigarh", "160030": "Chandigarh", "160031": "Chandigarh", "160032": "Chandigarh",
    "160033": "Chandigarh", "160034": "Chandigarh", "160035": "Chandigarh", "160036": "Chandigarh",
    "160037": "Chandigarh", "160038": "Chandigarh", "160039": "Chandigarh", "160040": "Chandigarh",
    "160041": "Chandigarh", "160042": "Chandigarh", "160043": "Chandigarh", "160044": "Chandigarh",
    "160045": "Chandigarh", "160046": "Chandigarh", "160047": "Chandigarh",
    
    # Coimbatore
    "641001": "Coimbatore", "641002": "Coimbatore", "641003": "Coimbatore", "641004": "Coimbatore",
    "641005": "Coimbatore", "641006": "Coimbatore", "641007": "Coimbatore", "641008": "Coimbatore",
    "641009": "Coimbatore", "641010": "Coimbatore", "641011": "Coimbatore", "641012": "Coimbatore",
    "641013": "Coimbatore", "641014": "Coimbatore", "641015": "Coimbatore", "641016": "Coimbatore",
    "641017": "Coimbatore", "641018": "Coimbatore", "641019": "Coimbatore", "641020": "Coimbatore",
    "641021": "Coimbatore", "641022": "Coimbatore", "641023": "Coimbatore", "641024": "Coimbatore",
    "641025": "Coimbatore", "641026": "Coimbatore", "641027": "Coimbatore", "641028": "Coimbatore",
    "641029": "Coimbatore", "641030": "Coimbatore", "641031": "Coimbatore", "641032": "Coimbatore",
    "641033": "Coimbatore", "641034": "Coimbatore", "641035": "Coimbatore", "641036": "Coimbatore",
    "641037": "Coimbatore", "641038": "Coimbatore", "641039": "Coimbatore", "641040": "Coimbatore",
    "641041": "Coimbatore", "641042": "Coimbatore", "641043": "Coimbatore", "641044": "Coimbatore",
    "641045": "Coimbatore", "641046": "Coimbatore", "641047": "Coimbatore", "641048": "Coimbatore",
    "641049": "Coimbatore", "641050": "Coimbatore",
    
    # Nagpur
    "440001": "Nagpur", "440002": "Nagpur", "440003": "Nagpur", "440004": "Nagpur",
    "440005": "Nagpur", "440006": "Nagpur", "440007": "Nagpur", "440008": "Nagpur",
    "440009": "Nagpur", "440010": "Nagpur", "440011": "Nagpur", "440012": "Nagpur",
    "440013": "Nagpur", "440014": "Nagpur", "440015": "Nagpur", "440016": "Nagpur",
    "440017": "Nagpur", "440018": "Nagpur", "440019": "Nagpur", "440020": "Nagpur",
    "440021": "Nagpur", "440022": "Nagpur", "440023": "Nagpur", "440024": "Nagpur",
    "440025": "Nagpur", "440026": "Nagpur", "440027": "Nagpur", "440028": "Nagpur",
    "440029": "Nagpur", "440030": "Nagpur", "440031": "Nagpur", "440032": "Nagpur",
    "440033": "Nagpur", "440034": "Nagpur", "440035": "Nagpur", "440036": "Nagpur",
    "440037": "Nagpur", "440038": "Nagpur", "440039": "Nagpur", "440040": "Nagpur",
}

def get_city_from_pincode(pincode: str) -> str:
    """
    Get the nearest supported city for a given pincode.
    
    Args:
        pincode (str): The pincode to lookup
        
    Returns:
        str: The nearest supported city name, or None if not found
    """
    pincode = pincode.strip()
    
    # Direct lookup first
    if pincode in PINCODE_CITY_MAPPING:
        return PINCODE_CITY_MAPPING[pincode]
    
    # If exact match not found, try to find nearest by prefix matching
    # This handles cases where we don't have exact pincode but have nearby ones
    if len(pincode) >= 3:
        prefix = pincode[:3]
        for pc, city in PINCODE_CITY_MAPPING.items():
            if pc.startswith(prefix):
                return city
    
    return None

def get_supported_cities():
    """
    Get list of all supported cities.
    
    Returns:
        list: List of supported city names
    """
    return list(set(PINCODE_CITY_MAPPING.values()))

def validate_pincode(pincode: str) -> bool:
    """
    Validate if a pincode is in correct format.
    
    Args:
        pincode (str): The pincode to validate
        
    Returns:
        bool: True if valid format, False otherwise
    """
    pincode = pincode.strip()
    return len(pincode) == 6 and pincode.isdigit()

def get_nearby_cities(pincode: str, radius: int = 2) -> list:
    """
    Get nearby cities within a certain pincode radius.
    
    Args:
        pincode (str): The base pincode
        radius (int): How many pincode numbers to search around
        
    Returns:
        list: List of nearby cities
    """
    if not validate_pincode(pincode):
        return []
    
    base_num = int(pincode)
    nearby_cities = set()
    
    # Search within radius
    for i in range(-radius, radius + 1):
        nearby_pincode = str(base_num + i).zfill(6)
        city = get_city_from_pincode(nearby_pincode)
        if city:
            nearby_cities.add(city)
    
    return list(nearby_cities)
