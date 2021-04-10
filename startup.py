'''
Script to run the startup processes for the cluster compute configurations
'''
import subprocess

vpc_networks_create = subprocess.call("./vpc_networks_create.sh")
eip_create = subprocess.call("./eip_create.sh")
controller_instance_create = subprocess.call("./controller_instance_script.sh")
k8_worker_create = subprocess.call("k8_workers.sh")