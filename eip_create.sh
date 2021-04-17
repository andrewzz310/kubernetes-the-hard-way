#!/bin/bash

# allocate an static ip to be attached to the external load balancer fronting the k8 api servers
gcloud compute addresses create kubernetes-the-hard-way \
  --region $(gcloud config get-value compute/region)

