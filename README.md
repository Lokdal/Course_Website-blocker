# Simple website blocker

Never catch yourself using Facebook on the job again. This script runs in the background and allows the user to specify websites to block and when to block them.

# Usage

In "sites.txt", write the address of a website you want blocked. Enter one per line.

In "settings.txt", configure the times at which the blocker should be active. 
**Only change "demo_version" to "False" if you know what you are doing. I'm not responsible for the loss of your pre-existing host file.**

Run the "Website-blocker.pyw" script and watch it modify the file demo_hosts according to time of day. If you set "demo_version" to "False", you will need to run the script as an administrator.
