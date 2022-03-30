
echo '\n\n###################################\n\n\tAutostart Enabled\n\n'
sleep 1;
echo -n '\nEntering Directory'

cd /home/pi/LESS_RPI_GUI/ || exit;

echo 'Starting GUI'

sudo python3 /home/pi/LESS_RPI_GUI/main.py;

echo '\n\n###################################\n\n\tGUI has been Closed\n\n###################################\n'
sleep 5;
