#!/usr/bin/env bash
# download kernel files
wget http://adafruit-download.s3.amazonaws.com/libraspberrypi-bin-adafruit.deb

wget http://adafruit-download.s3.amazonaws.com/libraspberrypi-dev-adafruit.deb

wget http://adafruit-download.s3.amazonaws.com/libraspberrypi-doc-adafruit.deb

wget http://adafruit-download.s3.amazonaws.com/libraspberrypi0-adafruit.deb

wget http://adafruit-download.s3.amazonaws.com/raspberrypi-bootloader-adafruit-112613.deb

# install kernel files
sudo dpkg -i -B *.deb

# turn off Accelerated X Framebuffer
sudo mv /usr/share/X11/xorg.conf.d/99-fbturbo.conf ~

# reboot
sudo reboot

### todo: fix this so that everything runs before you have to reboot it

# install screen drivers
sudo modprobe spi-bcm2708
sudo modprobe fbtft_device name=adafruitts rotate=90
export FRAMEBUFFER=/dev/fb1
startx

# Setting the modules to auto-load
#sudo nano /etc/modules
echo "spi-bcm2708\nfbtft_device" >> /etc/modules

