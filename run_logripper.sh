oc project logripper
oc delete jobs logripper
oc apply -f logripper.yaml
sleep 10
pod=$(kubectl get pods --selector=job-name=logripper --output=jsonpath='{.items[*].metadata.name}')
rm temp.log
oc logs -f pods/$pod > temp.log