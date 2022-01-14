import json
from operator import add
from unittest import result
from urllib import response
import requests

etherscan_api = 'SECRET_API'
api_url_base = 'https://api.etherscan.io/api'

def parse(response: requests.Response):
	content = response.json()
	result = content["result"]
	if "status" in content.keys():
		status = bool(int(content["status"]))
		message = content["message"]
	else:
		jsonrpc = content["jsonrpc"]
		cid = int(content["id"])
	return result

def get_node_count():
	url = "https://api.etherscan.io/api?module=stats&action=nodecount&apikey={0}".format(etherscan_api)
	response = requests.get(url, headers={"User-Agent": ""})
	content = parse(response)
	return content

def get_list_of_normal_transactions(address: str, start_block: int = 0, endblock: int = get_node_count(), page: int = 1, offstet: int = 10, sort: str = "asc"):
	url = "https://api.etherscan.io/api?module=account&action=txlist&address={0}&startblock={1}&endblock={2}&page={3}&offset={4}&sort={5}&apikey={6}".format(address, start_block, endblock, page, offstet, sort, etherscan_api)
	response = requests.get(url, headers={"User-Agent": ""})
	content = parse(response)
	return content

node_size = get_node_count()["TotalNodeCount"]
print(node_size)
list_of_normal_transactions = get_list_of_normal_transactions(address="")
print(list_of_normal_transactions)