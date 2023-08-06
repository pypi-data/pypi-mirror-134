import requests
import argparse


def read_args():
    arg_parser = argparse.ArgumentParser(description="Get configuration parameters")
    arg_parser.add_argument(
        "url",
        nargs="+",
        help="Url to connect to.  1 = local, 2 = www.prodigyhelmsman.co.za",
    )
    args = arg_parser.parse_args()
    url_option = args.url[0]
    if url_option == "1":
        def_url = 'http://localhost:8000/api/'
    else:
        def_url = 'www.prodigyhelmsman.co.za/api/'
    return def_url


active_url = read_args()
url_list = [
    ["_list_countries_method", 'list_countries'],
    [
        '_list_countries_method?curr_iso=LSL',
        'list_countries filter currency=LSL (Lesotho loti)',
    ],
    ['_find_country_method?cca=ZAF', 'find_country filter cca3 = ZAF'],
    ['_find_country_method?cca=ZA', 'find_country filter cca3 = ZA'],
]

for method, end_point in url_list:
    print(f'API Endpoint:\t{end_point}')
    print(f'Url:\t\t{active_url}')
    print(f'Method:\t{method}')
    response = requests.get(f'{active_url}{method}')
    ret_data = response.json()
    for rec in ret_data:
        print(rec)
    print(response.status_code)
    print()


print('API Endpoint: delete_country where cca = ZA')
print('Method: _delete_country_method')
response = requests.get(f'{active_url}_list_countries_method')
ret_data = response.json()
for rec in ret_data:
    print(rec)
response = requests.post(f'{active_url}_delete_country_method', {'cca': 'DER'})
ret_data = response.json()
for rec in ret_data:
    print(rec)
print(response.status_code)
response = requests.get(f'{active_url}_list_countries_method')
ret_data = response.json()
for rec in ret_data:
    print(rec)
print()

pass
