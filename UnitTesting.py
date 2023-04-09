import unittest
from netmiko import ConnectHandler
import time
import re

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

        neighbor=re.search('Loopback99 +([0-9]+.[0-9]+.[0-9]+.[0-9]+)',output)
        ip=neighbor.group(1)

        if ip=="10.1.3.1":
            return True
        else:
            return False
        
    def checkR1forsingleArea():
        R1={
            "host":"198.51.100.11",
            "username": "kevin",
            "password": "kevin",
            "secret": "kevin",
            "device_type": "cisco_ios"
        }
        connection = ConnectHandler(**R1)
        connection.enable()

        C1=["do show ip ospf statistics"]
        output=connection.send_config_set(C1)

        res = re.findall('Area ',output)
        length=len(res)

        if length==1:
            return True
        else:
            return False
    
    def checkpingfromR2toR5():
        R1={
            "host":"198.51.100.12",
            "username": "kevin",
            "password": "kevin",
            "secret": "kevin",
            "device_type": "cisco_ios"
        }
        connection = ConnectHandler(**R1)
        connection.enable()

        C1=["do ping 10.1.5.1 source 10.1.2.1"]
        output=connection.send_config_set(C1)

        neighbor=re.search('(5/5)',output)
        result=neighbor.group(1)

        if result=="5/5":
            return True
        else:
            return False


# The test based on unittest module
class Test(unittest.TestCase):

    def runTest(self):
        print("Running Test1")
        self.assertEqual(netman.checkr3ip(),True,"Incorrect loopbackIP")
        print("Running Test2")
        self.assertEqual(netman.checkR1forsingleArea(),True,"Multiple areas found")
        print("Running Test3")
        self.assertEqual(netman.checkpingfromR2toR5(),True,"Ping Failed")
        

 
# run the test
unittest.main()