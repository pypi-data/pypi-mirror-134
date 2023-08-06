import cloudscraper
import json

def filter_typename(dict):
    return dict['__typename'] == 'AssetQuantityType'

def filter_quantityInEth_exists(dict):
    if 'quantityInEth' in dict:
        return True
    else:
        return False

def get_floor_price_in_eth(dict):
    return float(dict['quantity']) / 1000000000000000000

def get_floor_prices(slug):
    scraper = cloudscraper.create_scraper(
        browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
        }
    )

    url = 'https://opensea.io/collection/{}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'.format(slug)
    html = scraper.get(url).text
    json_string = html.split('</script>', 2)[0].split('window.__wired__=', 2)[1]
    data = json.loads(json_string)
    data_values = data['records'].values()
    data_list = [*data_values]
    data_list = list(filter(filter_typename, data_list))
    data_list = list(filter(filter_quantityInEth_exists, data_list))
    data_list = list(map(get_floor_price_in_eth, data_list))
    return data_list[0]

def osfloor(collection_url):
    name = str(collection_url.split('/')[4])
    return get_floor_prices(name)