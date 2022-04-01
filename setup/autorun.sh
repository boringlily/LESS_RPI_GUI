
printf '\n\n###################################\n\n\tAutostart Enabled\n\n'

printf '\n\n Entering Directory\n\n'

sleep 2;

cd /home/pi/LESS_RPI_GUI/ || return;

printf 'Starting GUI'

sudo python3 /home/pi/LESS_RPI_GUI/main.py;

printf '\n\n###################################\n\n\tGUI has been Closed\n\n###################################\n'
sleep 5;
