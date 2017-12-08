import os
from time import sleep
error_mount = 8192

while error_mount == 8192:
    error_mount = os.system("sudo mount /dev/sda /mnt/usbStick")
    sleep(1)

os.system("cp -f /mnt/usbStick/destinataires.csv /home/pi/test/recipients.csv")
os.system("cp -f /mnt/usbStick/liste_capteurs.csv /home/pi/test/sensors_list.csv")
os.system("cp -f /mnt/usbStick/frequence_alerte.csv /home/pi/test/alert_frequence.csv")



os.system("sudo umount /mnt/usbStick")
