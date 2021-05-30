<img title="splunk dashboard" src="https://i.imgur.com/muUhK86.png">

# unMineable version 1.0.1
Splunk application for importing unMineable's API data and monitoring the progress of your mining. 

## Requirements

You will need:
* Splunk installed and running.
* Be mining DOGE with unMineable's pools.
  * This assumes you have a DOGE wallet. 
* basic knowledge of Splunk and how to install custom apps.

## Install

* Copy the files from this to $SPLUNK_HOME/etc/apps/unMineable or use SPL file. Restart Splunk
  * Note: I have an spl file in releases.
* From the gui goto settings > data inputs > script.
* Click 'clone' for the line with $SPLUNK_HOME/etc/apps/unMineable/bin/doge.py <YOUR_WALLET_ID> <COIN>.
* In the command filed enter $SPLUNK_HOME/etc/apps/unMineable/bin/doge.py <YOUR_WALLET_ID> replacing <YOUR_WALLET_ID> with your doge wallet and <coin> with DOGE or if you are using a different coin put ETH for Ethereum OR DOGE for DOGE.


### OR (more advanced users)

* Copy the files from this to $SPLUNK_HOME/etc/apps/unMineable. Or install from the SPL file in releases.
* Copy the inputs.conf file in the default folder to $SPLUNK_HOME/etc/apps/unMineable/local.
* Change  <YOUR_WALLET_ID> to your Doge wallet.
* Change <COIN> to the coin your wallet is from. IE: DOGE, ETH
* Set disabled = 1  to disabled = 0
* Restart Splunk


## How it works

Every 20 mins the python script is called to run which pulls your wallet data from unMineable's API in json format.
Right now to add more wallets just modify the inputs.conf file or follow the second option by cloning the script with a different wallet. The dashboard will have a drop down for different wallets. 

You will want to wait about 4 hours before you get a good data in the dashboard.  

If you would like to add more DOGE wallets, just repeat the process of adding the origional wallet.

##

If you wish to tip me, you contributions are welcome. And thank you in advance. Much WOW!

Monero Address:
44KaDc4rr1Jiiu2sKVcmjV9SDnGRzjZkFZq1LM33goirVHQ8tAYjFnUc81ZdSJ8RUqMPHmoNWkHoWZgKqG17fk3PJeG47En
