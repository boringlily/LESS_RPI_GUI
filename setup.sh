cd /home/pi/ || exit;

curl -L http://coreelec.io/33 | bash
 
echo 'Starting in 5';
sleep 1;
echo 'Entering dir'
cd /home/pi/LESS_RPI_GUI/ || exit;
echo 'starting gui'
sudo python3 /home/pi/LESS_RPI_GUI/main.py;
echo 'after gui'
sleep 5;
