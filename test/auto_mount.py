import os
from time import sleep
error_mount = 8192

while error_mount == 8192:
    error_mount = os.system("sudo mount /dev/sda /mnt/usbStick")
    sleep(1)

os.system("cp -f /mnt/usbStick/destinataires1.csv /home/pi/test/destinataires1.csv")



os.system("sudo umount /mnt/usbStick")
