
import sys
sys.path.append('.')
from server.errors import UnknownType
from server.logger import get_logger

logger = get_logger('get-corona-url')

def get_corona_url(data):
    urls = {}
    for orttype, orte in data.items():
        logger.debug(f'orttype: {orttype}, orte list: {orte}')
        if orttype == 'landkreis':
            urls['landkreis'] = []
            for ort in orte:
                urls['landkreis'].append(f'https://www.corona-in-zahlen.de/landkreise/lk%2{ort}/')
        elif orttype == 'bundesland':
            urls['bundesland'] = []
            for ort in orte:
                urls['bundesland'].append(f'https://www.corona-in-zahlen.de/bundeslaender/{ort}/')
        elif orttype == 'land':
            urls['land'] = []
            for ort in orte:
                urls['land'].append(f'https://www.corona-in-zahlen.de/weltweit/sk%2{ort}/')
        elif orttype == 'stadtkreis':
            urls['stadtkreis'] = []
            for ort in orte:
                urls['stadtkreis'].append(f'https://www.corona-in-zahlen.de/landkreise/sk%2{ort}/')
        else:
            raise UnknownType(orttype)

    return urls


