##########################################################################################
#   Program Name: bitcoin_osint_scanner.py												 #
#   Description: A OSINT python tool to carry out bitcoin forensics.					 #
#   Author: Anirudh Srinivas Balaji(git ID: Anirudh533)				                     #										
#   Created Date: 07-05-2021															 #
#   Last Updated: 26-05-2021															 #
#   Execution: python3 bitcoin_osint_scanner.py											 #
##########################################################################################


import os
import subprocess
import sys
import time

# For timestamp logging
timestamp = time.time()

# Commands
search_btc_cmd    = "python3 osint-spy.py --btc_date "
email_search_cmd  = "python3 osint-spy.py --email "
domain_search_cmd = "python3 osint-spy.py --domain "

#Writing btc_date and domain output to a file
f = open('transactions_output_'+str(int(timestamp))+'.txt','w+')
links = list()
email_list = list()
sub = 'Pool_link::'
print ("Running Bitcoin OSINT scanner ... ")


#Getting user input as date and listing out transactions based on the date entered.
btc_date = input("Enter the date you would like to search:(Ex: 20210425) ")
cmd = search_btc_cmd + str(btc_date)
output = subprocess.run(cmd,stdout=subprocess.PIPE).stdout.decode('utf-8')
f.write(output)
outlines= str(output).splitlines()
print("\n\n\n\n\n\n\n\n")
for line in outlines:
    if sub in line:
        line = line.strip()
        line = line.split(' ')
        if line[1] not in links:
            links.append(line[1])
f.write(str(links))


## Domain Search #############
for link in links:
    cmd = domain_search_cmd + link
    output = subprocess.run(cmd,stdout=subprocess.PIPE).stdout.decode('cp1252')
    f.write(output)
    f.write('--------------------------------------------------------------------------------------\n')

##### Email Search #############
    outlines= str(output).splitlines()
    flag = 0
    for line in outlines:
        line = line.strip()
        if 'Extracted Emails::' in line:
            flag = 1
            continue
        if flag == 1 and line not in email_list:
            email_list.append(line)
f.close()

#Writing Email search outputs to a file named email_osint_findings.txt
f = open('emails_osint_findings.txt','w+')
for email in email_list:
    cmd = email_search_cmd + email
    output = subprocess.run(cmd,stdout=subprocess.PIPE).stdout.decode('utf-8')
    f.write("The details for the Email ID: " + email + '\n')
    f.write('---------------------------------------------------------------------------------------\n')
    if 'Profile not found' in output:
        f.write("Profile not Found!!")
        continue
    f.write(output)
    f.write('---------------------------------------------------------------------------------------\n')
f.close()