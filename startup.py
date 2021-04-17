'''
Script to run the startup processes for the cluster compute configurations
'''
import subprocess
'''
# compute
vpc_networks_create = subprocess.call("./vpc_networks_create.sh")

# static ip
eip_create = subprocess.call("./eip_create.sh")

'''

# Compute Instances for control plane
controller_instance_create = subprocess.call("./controller_instance_script.sh")


# Compute Instances for workers
k8_worker_create = subprocess.call("./k8_workers.sh")