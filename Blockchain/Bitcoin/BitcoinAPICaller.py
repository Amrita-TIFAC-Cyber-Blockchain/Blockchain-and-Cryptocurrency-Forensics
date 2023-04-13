#####################################################################################################
# Program Name : BitcoinAPICaller.py																
# Description  : Library of APIs from blockcypher.com to gather data about Bitcoin Blockchain 		
# Author       : Anuhya Gandavaram (git ID: AnuhyaGandavaram)										
# Created Date : 12 May 2021																		#
# Last Updated : 15 May 2021																		#
# Execution    : python BitcoinAPICaller.py 														
#####################################################################################################


from blockcypher import get_blockchain_overview
from blockcypher import get_block_overview
from blockcypher import get_block_overview
from blockcypher import get_address_overview
from blockcypher import get_address_details
from blockcypher import get_address_full
from blockcypher import get_wallet_addresses
from blockcypher import get_transaction_details
from blockcypher import get_broadcast_transactions
from blockcypher import get_transaction_details
from blockcypher import get_metadata

#API Key
apikey = 'f02279a7b29844e587c0b0fbadf49964'

## Sample Values
address = '1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD'
haash = '43fa951e1bea87c282f6725cf8bdc08bb48761396c3af8dd5a41a085ab62acc9'
block_height = '671142'
wallet_Name = 'alice'

## To receive user Input
choices = {1:'Overview',2:'Get Block from Hash',3:'Get Block from Height',4:'Get Balance',5:'Get Transaction Details of Address',
6:'Get Full Transaction of Address',7:'Get Wallet Addresses',8:'Get HD Wallet Addresses',9:'Get Transaction Details from Hash',
10:'Get Unconfirmed Transactions',11:'Get Confidence from Hash',12:'Get Metadata of Address'}


for i in range(len(choices.keys())):
	print(str(i+1)+'. '+choices[i+1])
choice = int(input("Please Enter your Choice: "))


if choice==2 or choice==9 or choice==11:
	haash = input("Enter Hash (sample: 43fa951e1bea87c282f6725cf8bdc08bb48761396c3af8dd5a41a085ab62acc9): ")
elif choice==4 or choice==5 or choice==6 or choice==12:
	address = input("Enter Address (sample: 1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD): ")
elif choice==3:
	block_height = input("Enter Block Height (sample: 671142): ")
elif choice==7 or choice==8:
	wallet_Name = input("Enter Wallet Name (sample: alice): ")
else:
	print()

if choice==1:
	result = get_blockchain_overview()
	print("Block Height: ",result['height'])
elif choice==2:
	result = get_block_overview(haash)
	print("Block Height: ",result['height'])
	print("Number of Transactions: ",len(result['txids']))
elif choice==3:
	result = get_block_overview(block_height, txn_limit=1, txn_offset=1)
	print("Number of Transactions: ",len(result['txids']))
elif choice==4:
	result = get_address_overview(address)
	print("Received: ",result['total_received']," sat")
	print("Sent: ",result['total_sent']," sat")
	print("Balance: ",result['balance']," sat")
elif choice==5:
	result = get_address_details(address)
	print("Received: ",result['total_received']," sat")
	print("Sent: ",result['total_sent']," sat")
	print("Balance: ",result['balance']," sat")
	print("Number of Transactions: ",result['n_tx'])
elif choice==6:
	result = get_address_full(address=address)
	print("Received: ",result['total_received']," sat")
	print("Sent: ",result['total_sent']," sat")
	print("Balance: ",result['balance']," sat")
	print("Number of Transactions: ",result['n_tx'])
elif choice==7:
	result = get_wallet_addresses(wallet_name=wallet_Name, api_key=apikey)
	print("Number of addresses associated: ",len(result['addresses']))
elif choice==8:
	result = get_wallet_addresses(wallet_name=wallet_Name, api_key=apikey, is_hd_wallet=True)
	print("Number of addresses associated: ",len(result['addresses']))
elif choice==9:
	result = get_transaction_details(haash)
	print("Block Height: ",result['block_height'])
	print("Total :",result['total']," sat")
elif choice==10:
	result = get_broadcast_transactions(limit=1)
	print("Number of Unconfirmed Transactions: ",len(result))
	print("Transaction Hash: ",result[0]['hash'])
elif choice==11:
	result = get_transaction_details(haash, confidence_only=True, api_key=apikey)
	print("Confidence: ",result['confidence'])
elif choice==12:
	result = get_metadata(address=address, api_key=apikey)
	print(result)
else:
	print('Thank you !!!')
