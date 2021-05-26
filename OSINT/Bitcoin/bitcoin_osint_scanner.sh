#####################################################################################################
#   Program Name: bitcoin_osint_scanner.sh                                                          #
#   Description: A OSINT bash tool to carry out bitcoin forensics.                                  #
#   Author: Anirudh Srinivas Balaji(git ID: Anirudh533)                                             #
#   Created Date: 09-05-2021                                                                        #
#   Last Updated: 26-05-2021                                                                        #
#   Execution: bash bitcoin_osint_scanner.sh                                                        #
#####################################################################################################

#Move to the particular directory
echo "Make sure you have the OSINT-SPY already installed and it is residing in your Desktop"
cd ~/Desktop/OSINT-SPY

#Getting user input
echo "Running Bitcoin OSINT scanner ... "
echo "Enter the date you would like to search:(Ex: 20210425) "
read btc_date


#   python3 osint-spy.py --btc_date $btc_date: Fetch bitcoin transactions the given date.
#   awk '/Pool_link::/ {print}': Prints only http/https links from the output along with the Pool_links::.
#   sed 's/Pool_link:://g': Ignores the Pool_links:// from the links(g - globally - throughout the code).
#   sed 's/https://g': Ignores the https:// from the links(g - globally - throughout the code).
#   cut -c 5-: Cuts http/https characters from the links for nmap to process it.
#   tr -d /: Ignores / from http/https links.
#   sed 's/tp://g': Deletes tp: from the domain names.
#   collected_urls.txt: Stores the output in links.txt

python3 osint-spy.py --btc_date $btc_date | awk '/Pool_link::/ {print}'| sed 's/Pool_link:://g' | sed 's/https://g' | cut -c 5- | tr -d / | sed 's/tp://g' > collected_urls.txt

#   Removes duplicate links and stores them in a new text file.
sort -u collected_urls.txt > final_urls.txt

#   Runs nmap, whois lookup against the final_urls.txt file and then finally stores the output in a new file called nmap_whois_output.txt.
nmap -iL final_urls.txt --script whois-ip > nmap_whois_output.txt