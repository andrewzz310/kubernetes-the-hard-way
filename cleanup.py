'''
Script to tear down the compute creations
'''
import subprocess

# clean eip
eip_clean = subprocess.call("./eip_cleanup.sh")

# clean controller and disk
controller_clean = subprocess.call("./controller_cleanup.sh")


