# import os
# q=os.system("pylint netman_netconf_obj2.py")
# print(q)
# exit(0)

# import commands
# status, output = commands.getstatusoutput("cat /etc/services")

import subprocess
import re

proc = subprocess.Popen("pylint netman_netconf_obj2.py", stdout=subprocess.PIPE, shell=True)
(output, err) = proc.communicate()

neighbor=re.search('rated at ([0-9]+.[0-9]+)',str(output))
result=neighbor.group(1)
print(result)
print(type(result))
result=float(result)
print(type(result))
if result>=5.00:
    print("greater")
else:
    print("smaller")