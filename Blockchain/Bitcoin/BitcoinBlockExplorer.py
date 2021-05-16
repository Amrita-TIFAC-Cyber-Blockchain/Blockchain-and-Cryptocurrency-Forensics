#####################################################################################################
# Program Name : BitcoinBlockExplorer.py															#
# Description  : Bitcoin Core Block File Analyser													#
#				 Takes the path to the folder of main/test net as input								#
#				 Analyses each blk file and stores results to a csv									#
# Author	   : Anuhya Gandavaram(git ID: AnuhyaGandavaram)										#
# Created Date : 19 Mar 2021																		#
# Last Modified: 15 May 2021																		#
# Execution	   : python BitcoinBlockExplorer.py C:\Users\<username>\AppData\Roaming\Bitcoin\blocks 	#
#####################################################################################################

import sys
import binascii
import os
import csv
import logging
import datetime
import time

## Magic Bytes 
test_magicbytes = '0b110907'	# magic bytes for test net
main_magicbytes = 'f9beb4d9'	# magic bytes for main net

## Constants
count = 0
cap = 65000
current = 1
folder_path = 'BitcoinBlockExplorer_Results'
counter = 1

## Excel Parameters
header = ['file name', 'number of blocks', 'block_number','block_size','block_size_int','version','previous_block','merkel_root','timestamp','bits','nonce','transaction_count','transaction_count_int']	#Headers for excel
row = ['','','','','','','','','','','','','']
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')	#logger format
timestamp = time.time()	#Timestamp for creating folders and saving logs

## Function to create Folders to store the parsed data
def create_folders_files():
	if not os.path.exists(folder_path):
		os.mkdir(folder_path)
	os.mkdir(folder_path+'\BC_'+str(int(timestamp)))
	global f, writer
	f = open(folder_path+'\BC_'+str(int(timestamp))+'\CD_'+str(counter)+'.csv','a+',newline='')
	writer = csv.writer(f)
	writer.writerow(header)

## Function to setup the logging parameters
def setup_logger(name, log_file, level=logging.INFO):
	logger = logging.getLogger(name)
	handler = logging.FileHandler(folder_path+'\BC_'+str(int(timestamp))+'\\'+log_file, mode='a+')
	handler.setFormatter(formatter)
	streamHandler = logging.StreamHandler()
	streamHandler.setFormatter(formatter)

	logger.setLevel(level)
	logger.addHandler(handler)
	logger.addHandler(streamHandler)

## Function to get the case details from the Investigator 
def get_case_details():
	choice = input("Before Proceding, Wish to add case details(y/n): ")
	if choice[0] == 'y' or choice[0] == 'Y':
		caseID = input("caseID: ")
		caseName = input("case Name: ")
		investigatorName = input("Investigator Name: ")
		reviewerName = input("Reviewer Name: ")
		caseDescription = input("Description: ")

## Function to Initiate and Create a Logger
def create_logger():
	setup_logger('basic_logger', 'bitlyse.log')
	global main_logger
	main_logger = logging.getLogger('basic_logger')
	setup_logger('time_logger', 'time.log')
	global time_logger
	time_logger = logging.getLogger('time_logger')

## Function to Validate the user input 
def validate_inputs():
	if(len(sys.argv) < 2):
		print("Please provide the input folder")
		exit()

## Function to find Magic Bytes in the blk File
def check_magic_bytes(file, file_data):
	if(main_magicbytes in str(file_data)):	#checking if magicbytes match with main net
		main_logger.info(file + ': magic bytes matched with main net')
		block_list = str(file_data).split(main_magicbytes)
	if(test_magicbytes in str(file_data)):	#checking if magic bytes match with test net
		main_logger.info(file + ": magic bytes matched with test net")
		block_list = str(file_data).split(test_magicbytes)
	return block_list

## Function to Check if Max Row Limit is reached in csv
def check_row_limit():
	global current, count, cap
	if((current+count > cap) and (current != 1)):
		counter = counter + 1
		f.close()
		f = open(folder_path+'\BC_'+str(int(timestamp))+'\CD_'+str(counter)+'.csv','a+',newline='')
		writer = csv.writer(f)
		writer.writerow(header)
		current = 1
	return current

## Function to populate the row for csv 
def make_row(block_list):
	global row
	row[3] = block_list[0:8]
	row[4] = int(row[3][::-1],16)
	row[5] = block_list[8:16]
	row[6] = block_list[12:80]
	row[7] = block_list[80:144]
	row[8] = block_list[144:152]
	row[9] = block_list[152:160]
	row[10] = block_list[160:168]
	row[11] = block_list[168:170]
	row[12] = int(row[11],16)

## Function to Parse the files in the folder and store results to csv
def parse_store_data():
	files = os.listdir(sys.argv[1])	#fetching list of files
	main_logger.info(str(files) + ' found in the path ' + sys.argv[1])
	for file in files:
		main_logger.info('analysing ' + file)
		file_name, file_extension = os.path.splitext(file)	#getting filename and extension
		if file_extension == '.dat' and file_name.startswith('blk'):	#analysing only for blk and .dat files
			main_logger.info('File extension matched with .dat for file ' + file)
			start_time = datetime.datetime.now()
			with open(sys.argv[1]+'\\'+file, "rb") as file_obj:
				main_logger.info(file + ' opened')
				time_logger.info(file + ' opened')
				file_data = binascii.hexlify(file_obj.read())
				if(main_magicbytes in str(file_data) or test_magicbytes in str(file_data)):
					row[0] = file
					block_list = check_magic_bytes(file, file_data)[1:-1]
					row[1] = len(block_list)	#getting the number of blocks in the file
					global count, writer
					count = row[1]
					current = check_row_limit()+count
					for i in range(count):
						row[2] = i+1
						make_row(block_list[i])
						writer.writerow(row)
				else:
					main_logger.error(file + ": no magic bytes found")
					print(file + " is not a Bitcoin file")
			main_logger.info(file + " closed")
			time_logger.info(file + " closed")
			file_obj.close()
			end_time = datetime.datetime.now()
			time_lapse = end_time - start_time
			time_logger.info("Total time for " + file + " is " + str(time_lapse))
	f.close()


def main():
	validate_inputs()
	get_case_details()
	create_folders_files()
	create_logger()
	parse_store_data()

## Main Caller
main()