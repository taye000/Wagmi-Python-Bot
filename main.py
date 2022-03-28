from tokens import cmc_token
import requests
import json
import pprint

def write_json(data, filename='response.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_cmc_data(crypto):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    params = {
    'symbol': crypto,
    'convert':'USD'
    }
    headers = {
    'X-CMC_PRO_API_KEY': cmc_token
    }

    response = requests.get(url, headers=headers, params=params).json()

    price = response['data'][crypto][0]['quote']['USD']['price']

    return price

def main():
    print(get_cmc_data('BTC'))
    print(get_cmc_data('ETH'))
    print(get_cmc_data('WAGMI'))


if __name__ == "__main__":
    main()



    




