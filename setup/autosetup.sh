mv -f /home/pi/Downloads/LESS_RPI_GUI-main /home/pi/

##### install python3 and pip
cd || exit;

sudo apt-get update

sudo apt-get install python3.6

command -v pip3

##### Install NeoPixel libraries
cd /home/pi/ || exit;

curl -L http://coreelec.io/33 | bash

##### Setup automations
sudo mv -f /home/pi/LESS_RPI_GUI-main/setup/autostart /etc/xdg/lxsession/LXDE-pi/

##### Finish instructions

printf "############################################\n\n packages have been installed\n
You can now restart the device to test the automations"