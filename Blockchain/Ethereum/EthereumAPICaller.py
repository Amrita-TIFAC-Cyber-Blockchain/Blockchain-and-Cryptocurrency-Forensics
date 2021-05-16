#################################################################################################
# Program Name : EthereumAPICaller.py															#
# Description  : Library of APIs from etherscan.com to gather data about Ethereum Blockchain	#
# Author       : Anuhya Gandavaram(git ID: AnuhyaGandavaram)									#
# Created Date : 02 May 2021																	#
# Last Updated : 15 May 2021																	#
# Execution	   : python EthereumAPICaller.py 													#
#################################################################################################

import requests
import json

## API Key
apikey = 'GCB5EHZCEAJ9KY88PEZITQB267SGWM1TW4'

## Sample Values
address = 'ddbd2b932c763ba5b1b7ae3b362eac3e8d40121a'
haash = '40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170'
block_number = '2165403'
timestamp = '1578638524'

## To receive user Input
choices = {1:'Get Account Balance of an Address',2:'Get Normal Transactions of an Address',3:'Get Internal Transactions of an address',
4:'Get Transactions from Hash',5:'Get Blocks Mined by an address',6:'Get Transaction Status by Hash',7:'Get Block Rewards',
8:'Get Block Countdown Time',9:'Get Block Number from Timestamp'}


for i in range(len(choices.keys())):
	print(str(i+1)+'. '+choices[i+1])
choice = int(input("Please Enter your Choice: "))


if choice==1 or choice==2 or choice==3 or choice==5:
	address = input("Enter Address (sample: ddbd2b932c763ba5b1b7ae3b362eac3e8d40121a): ")
elif choice==4 or choice==6:
	haash = input("Enter Hash (sample: 40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170): ")
elif choice==7 or choice==8:
	block_number = input("Enter Block Number (sample: 2165403): ")
elif choice==9:
	timestamp = input("Enter Timestamp (sample: 1578638524): ")
else:
	print("Invalid Choice\n")

## API Endpoints
account_balance_url = 'https://api.etherscan.io/api?module=account&action=balance&address=0x'+address+'&tag=latest&apikey='+apikey
normal_transaction_by_address_url = 'https://api.etherscan.io/api?module=account&action=txlist&address=0x'+address+'&startblock=0&endblock=99999999&sort=asc&apikey='+apikey
internal_transactions_by_address_url = 'https://api.etherscan.io/api?module=account&action=txlistinternal&address=0x'+address+'&startblock=0&endblock=2702578&sort=asc&apikey='+apikey
internal_transactions_by_hash_url = 'https://api.etherscan.io/api?module=account&action=txlistinternal&txhash=0x'+haash+'&apikey='+apikey
blocks_mined_by_address_url = 'https://api.etherscan.io/api?module=account&action=getminedblocks&address=0x'+address+'&blocktype=blocks&apikey='+apikey
transaction_receipt_status_by_hash_url = 'https://api.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash=0x'+haash+'&apikey='+apikey
block_rewards_by_number_url = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno='+block_number+'&apikey='+apikey
block_countdowntime_by_number_url = 'https://api.etherscan.io/api?module=block&action=getblockcountdown&blockno='+block_number+'&apikey='+apikey
block_number_by_timestamp_url = 'https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp='+timestamp+'&closest=before&apikey='+apikey


if choice==1:
	result = requests.post(account_balance_url).text
	result = json.loads(result)
	print('Account Balance: '+result['result']+' wei')
elif choice==2:
	result = requests.post(normal_transaction_by_address_url).text
	result = json.loads(result)
	print('Number of Transactions: '+str(len(result['result'])))
	print('Transaction Blocks')
	for i in range(len(result['result'])):
		print(result['result'][i]['blockNumber'])
elif choice==3:
	result = requests.post(internal_transactions_by_address_url).text
	result = json.loads(result)
	print('Number of Transactions: '+str(len(result['result'])))
	print('Transaction Blocks')
	for i in range(len(result['result'])):
		print(result['result'][i]['blockNumber'])
elif choice==4:
	result = requests.post(internal_transactions_by_hash_url).text
	result = json.loads(result)
	print('Transaction Block')
	for i in range(len(result['result'])):
		print(result['result'][i]['blockNumber'])
elif choice==5:
	result = requests.post(blocks_mined_by_address_url).text
	result = json.loads(result)
	print('Number of Blocks: '+str(len(result['result'])))
	print('Transaction Blocks')
	for i in range(len(result['result'])):
		print(result['result'][i]['blockNumber'])
elif choice==6:
	result = requests.post(transaction_receipt_status_by_hash_url).text
	result = json.loads(result)
	if(result['result']['status']==1):
		print('Success')
	else:
		print('Failure')
elif choice==7:
	result = requests.post(block_rewards_by_number_url).text
	result = json.loads(result)
	print('Block Reward: '+ result['result']['blockReward']+' wei')
elif choice==8:
	result = requests.post(block_countdowntime_by_number_url).text
	result = json.loads(result)
	print('Countdown Time: '+result['result']['EstimateTimeInSec'])
	print('Current Block: '+result['result']['CurrentBlock'])
	print('Blocks Left: '+result['result']['RemainingBlock'])
elif choice==9:
	result = requests.post(block_number_by_timestamp_url).text
	result = json.loads(result)
	print('Block Number: '+result['result'])
else:
	print('Thank you !!!')
