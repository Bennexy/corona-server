url = "https://www.corona-in-zahlen.de/landkreise/sk%20münchen/"


print(url.split('/')[-2].split('%')[0])



data = {"landkreis": ["erding"]}
# {'landkreis': {'erding': {'orttype': 'landkreis', 'ortsnamen': 'erding', 'einwohner': '138.182', 'infektionen': '6.937', 'infektionsrate': '5,02%', 'neuinfektionen': '34,0', 'todesfaelle': '118', 'letalitätsrate': '1,70%'}}}




print(data['namen'])


