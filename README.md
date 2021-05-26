# unMineable
Splunk application for importing unMineable's API data
## Install
* Copy the files from this to $SPLUNK_HOME/etc/apps/unMineable.
* Copy the inputs.conf file in the default folder to $SPLUNK_HOME/etc/apps/unMineable/local.
* Change  <YOUR_WALLET_ID> to your Doge wallet.
* Restart splunk

OR


* Copy the files from this to $SPLUNK_HOME/etc/apps/unMineable. Restart splunk
  * Note: I have an spl file but pointless for github.
* From the gui goto settings > data inputs > script.
* Click 'clone' for the line with $SPLUNK_HOME/etc/apps/unMineable/bin/doge.py <YOUR_WALLET_ID>.
* In the command filed enter $SPLUNK_HOME/etc/apps/unMineable/bin/doge.py <YOUR_WALLET_ID> replaceing <YOUR_WALLET_ID> with your doge wallet.


