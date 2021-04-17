
# clean 3 controller nodes
for i in 0 1 2; do
  echo Y | gcloud compute instances delete controller-${i}
done

# clean worker nodes
for i in 0 1 2; do
  echo Y | gcloud compute instances delete worker-${i} \

done
