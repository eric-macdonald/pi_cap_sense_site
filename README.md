Capacitive sensing website

Add this line to the "crontab -e"
@reboot python /home/pi/capsense_site/capsense_site.py &

curl https://get.pimoroni.com/touchphat  | bash
pip install -U Flask

with webbrowser add IP:5000 to see served webpage.
Refresh to see new data

Future version should update immediately.
