#!/bin/bash


#clean eip
gcloud compute addresses delete kubernetes-the-hard-way


# clean controllers and disk
for i in 0 1 2; do
  echo Y | gcloud compute instances delete controller-${i}
done


for i in 0 1 2; do
  echo Y | gcloud compute instances delete worker-${i} \

done
