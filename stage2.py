import subprocess
import re

proc = subprocess.Popen("pylint netman_netconf_obj2.py", stdout=subprocess.PIPE, shell=True)
(output, err) = proc.communicate()

neighbor=re.search('rated at ([0-9]+.[0-9]+)',str(output))
result=neighbor.group(1)
result=float(result)
if result>=5.00:
    # print("greater")
    print("Score is greater than 5.00")
    exit(0)
else:
    # print("smaller")
    print("Score is lesser than 5.00")
    exit(1)