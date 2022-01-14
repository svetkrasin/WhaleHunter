import requests

etherscan_api = ''
api_url_base = 'https://api.etherscan.io/api'

def get_total_nodes():
	api_url = 'https://api.etherscan.io/api?module=stats&action=nodecount&apikey={0}'.format(etherscan_api)
	print(api_url)

get_total_nodes()
