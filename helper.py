##
# Created By Anil Soni
# Interfacing OBD through python
##
import os

__all__ = ["get_eth_name", "get_mac"]
__version__ = 0.1
def get_eth_name():
  # Get name of the Ethernet interface
  try:
    for root, dirs, files in os.walk('/sys/class/net'):
      for dir_ in dirs:
        if dir_[:3]=='enx' or dir_[:3]=='eth':
          interface=dir_
  except:
    interface="None"
  return interface


def get_mac(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open("/sys/class/net/{}/address".format(interface)).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

def
