import sys
import requests
from bs4 import BeautifulSoup
sys.path.append('.')

from server.logger import get_logger
from server.errors import UnknownType

logger = get_logger('corona-get-data')


def get_corona_data(urls):
    data = {}
    for datatype, url in urls.items():
        if datatype == 'landkreis':
            data['landkreis'] = get_info_kreis(url)
        elif datatype == 'stadtkreis':
            data['stadtkreis'] = get_info_kreis(url)
        elif datatype == 'bundesland':
            data['bundesland'] = get_info_land(url)
        elif datatype == 'bundesland':
            data['bundesland'] = get_info_land(url)
        else:
            UnknownType(f'datatype {datatype}, url {url}')

    return data


def get_info_kreis(urls):

    data_out = {}

    for url in urls:

        land = url.split("%")[-1].replace('2', '').replace('0', '').rstrip('/')

        data = {}

        unparsed_page = requests.get(url).content

        parsed_page = BeautifulSoup(unparsed_page, 'html.parser')

        all_raw_data = parsed_page.find('div', class_='row row-cols-1 row-cols-md-3')
        raw_data = list(all_raw_data.find_all('b'))

        if url.split('/')[-2].split('%')[0] == "sk":
            orttype = "stadtkreis"
        elif url.split('/')[-2].split('%')[0] == "lk":
            orttype = "landkreis"
        else:
            raise UnknownType(f"landkreis type {url.split('/')[-2].split('%')[0]} not known")
        
        data['orttype'] = orttype

        data['ortsnamen'] = land

        data['einwohner'] = str(raw_data[0]).translate({ord(i): None for i in '\n <b>/'})

        data['infektionen'] = str(raw_data[1]).translate({ord(i): None for i in '\n <b>/'})

        data['infektionsrate'] = str(raw_data[2]).translate({ord(i): None for i in '\n <b>/'})

        data['neuinfektionen'] = str(raw_data[3]).translate({ord(i): None for i in '\n <b>/'})

        data['todesfälle'] = str(raw_data[4]).translate({ord(i): None for i in '\n <b>/'})

        data['letalitätsrate'] = str(raw_data[5]).translate({ord(i): None for i in '\n <b>/'})

        data_out[land] = data

    return data_out

def get_info_land(urls):

    data_out = {}

    for url in urls:

        land = url.split('/')[-2]

        data = {}
        raw_data = []

        unparsed_page = requests.get(url).content

        parsed_page = BeautifulSoup(unparsed_page, 'html.parser')

        all_raw_data = parsed_page.find_all('div', class_='row row-cols-1 row-cols-md-3')
        for extracted_data in all_raw_data:
            for i in extracted_data.find_all('b'):
                raw_data.append(i)

        data['orttype'] = url.split('/')[-3]

        data['ortsnamen'] = land

        data['einwohner'] = str(raw_data[0]).translate({ord(i): None for i in '\n <b>/'})

        data['infektionen'] = str(raw_data[1]).translate({ord(i): None for i in '\n <b>/'})

        data['infektionsrate'] = str(raw_data[2]).translate({ord(i): None for i in '\n <b>/'})

        data['neuinfektionen'] = str(raw_data[3]).translate({ord(i): None for i in '\n <b>/'})

        data['todesfälle'] = str(raw_data[4]).translate({ord(i): None for i in '\n <b>/'})

        data['letalitätsrate'] = str(raw_data[5]).translate({ord(i): None for i in '\n <b>/'})

        data['erstimpfungen'] = str(raw_data[6]).translate({ord(i): None for i in '\n <b>/'})

        data['impfquote (erstimpfung)'] = str(raw_data[7]).translate({ord(i): None for i in '\n <b>/'})

        data['impfquote (vollstaeding)'] = str(raw_data[8]).translate({ord(i): None for i in '\n <b>/'})

        data_out[land] = data

    return data_out





















