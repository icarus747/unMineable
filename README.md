<img title="splunk dashboard" src="https://i.imgur.com/muUhK86.png">

# unMineable
Splunk application for importing unMineable's API data
## Install
* Copy the files from this to $SPLUNK_HOME/etc/apps/unMineable.
* Copy the inputs.conf file in the default folder to $SPLUNK_HOME/etc/apps/unMineable/local.
* Change  <YOUR_WALLET_ID> to your Doge wallet.
* Set disabled = 1  to disabled = 0
* Restart Splunk

OR

* Copy the files from this to $SPLUNK_HOME/etc/apps/unMineable. Restart Splunk
  * Note: I have an spl file but pointless for github.
* From the gui goto settings > data inputs > script.
* Click 'clone' for the line with $SPLUNK_HOME/etc/apps/unMineable/bin/doge.py <YOUR_WALLET_ID>.
* In the command filed enter $SPLUNK_HOME/etc/apps/unMineable/bin/doge.py <YOUR_WALLET_ID> replacing  <YOUR_WALLET_ID> with your doge wallet.


## How it works

Every 20 mins the python script is called to run which pulls your wallet data from unMineable's API in json format.
Right now to add more wallets just modify the inputs.conf file or follow the second option by cloning the script with a different wallet. The dashboard will have a drop down for different wallets. 

You will want to wait about 4 hours before you get a good data in the dashboard.  

If you wish to tip me, you contributions are welcome. And thank you in advance.

Monero Address:
44KaDc4rr1Jiiu2sKVcmjV9SDnGRzjZkFZq1LM33goirVHQ8tAYjFnUc81ZdSJ8RUqMPHmoNWkHoWZgKqG17fk3PJeG47En
