import unittest
from netmiko import ConnectHandler
import time
import re


 
# Our code to be tested
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height
 


class netman:
    def checkr3ip():
        R3={
            "host":"198.51.100.13",
            "username": "kevin",
            "password": "kevin",
            "secret": "kevin",
            "device_type": "cisco_ios"
        }
        connection = ConnectHandler(**R3)
        connection.enable()

        C1=["do show ip int br"]
        output=connection.send_config_set(C1)
        print(output)

        neighbor=re.search('Loopback5 +([0-9]+.[0-9]+.[0-9]+.[0-9]+)',output)
        ip=neighbor.group(1)

        print(ip)
        if ip=="10.1.3.1":
            return True
        else:
            return False
    def checkR1forsingleArea():
        return False


# The test based on unittest module
class TestGetAreaRectangle(unittest.TestCase):

    def runTest(self):
        rectangle = Rectangle(2, 3)
        # self.assertEqual(rectangle.get_area(), 6, "incorrect area")
        self.assertEqual(netman.checkr3ip(),True,"Incorrect loopbackIP")
        
 
# run the test
unittest.main()