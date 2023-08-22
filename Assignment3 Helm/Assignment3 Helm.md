## Assignment 3 - Helm

### Prerequisites:
* Install Minikube in convenient way 

Minikube based on Docker Desktop | https://github.com/LianDuanTrain/K8S/tree/main/2-Install-Minikube

</details>

* Install Helm with version according to your Minikube version
https://github.com/LianDuanTrain/Helm3/tree/master/1%20Introduction%20and%20Installation \
https://www.youtube.com/watch?v=wtbqR_H0UV0

### Steps


1. Create/use Helm charts to deploy sample webapp

https://www.youtube.com/watch?v=jUYNS90nq8U \
https://github.com/devopsjourney1/helm-webapp

**



Make report with screens of app running in prod dev env

2. Create Assignment3 report and send it by e-mail (docx/link to google doc) or through creation repo fork + pull request.

### References
* I got problems with Docker Desktop install cause of brocken Hyper-V settings https://stackoverflow.com/questions/39684974/docker-for-windows-error-hardware-assisted-virtualization-and-data-execution-p

* I got problems with

```kubectl --namespace prod port-forward service/myhelmapp 8888:80```

instead use

```kubectl --namespace prod port-forward service/myhelmapp 80:80```
because in my case myhelmapp uses port 80. Use command to get which port myhelmapp uses

```kubectl get services```