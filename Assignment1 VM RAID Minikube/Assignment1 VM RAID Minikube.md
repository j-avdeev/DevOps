## Assignment 1 - VM and RAID1
### What is RAID:
https://en.wikipedia.org/wiki/RAID

### Steps
1. Create virtual machine with debian/ubuntu/centos or download
   preinstalled image (https://www.osboxes.org/). It should be withoug GUI.
2. Set hostname = your surname.
3. Add simple raid1 to virtual machine: \*nix os system on 1-st hdd, 2d
   and 3d hdds are in raid1. 1 (with star). Only two hdds. Os system on
   raid1, based on this two hdd.
4. How to test raid1. Create file on raid1 file system. Turn off vm and
   remove one of the hhds from vm. Turn on vm. File should be
   accessible.
5. Add new hdd and sync it to raid1.

I recommend to set VM network to Network bridge mode. In my case VM get IP from my router as my host so it is easier opeate, in your network case situation can be differ.

For following minikube installation I recommend to install minikube inside your VM (not outside on your host) - with Docker driver, so Docker installation is prerequisite (see https://docs.docker.com/engine/install/ accordingly to your VM OS, _Install using the repository_ looks easy).

Also you will need to extend your VM CPU and RAM to run minikube: \
CPU: 2 core or more \
RAM: ~1900 MB (1800 MB min for minikube + OS)

6. Install and run local Kubernetes cluster with **minikube**  
  * Use steps from `Kubernetes install Tools` https://kubernetes.io/docs/tasks/tools/ 

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
```
minikube version
```
```
minikube start
```
Add current user to docker group to get availability to run docker
```
sudo usermod -aG docker $USER && newgrp docker
```
Run minikube with docker driver
```
minikube start --driver=docker
```
To check that minikube successfully started
```
minikube status
```
install kubectl (https://kubernetes.io/ru/docs/tasks/tools/install-kubectl/)

install Dashboard (https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)

Create sample user
https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md + for details see 1:40 (https://www.youtube.com/watch?v=HpMel0AVu_Y)
```
kubectl -n kubernetes-dashboard create token admin-user
```
run (maybe you will need to wait a bit until Dashboard pod start)
```
kubectl proxy --address 0.0.0.0 --accept-hosts '.*'
```
then open in other ssh session command
```
kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8443:443 --address 0.0.0.0
```
Start web-browser on you host, Dashboard should be available on
https://192.168.8.190:8443/ \
where 192.168.8.190 - is you VM ip address

Insert your token to access Dashboard

Make report with screens of:
  * `minicube version` command output
  * opened Dashboard in your web-browser (on your host)

8. Create Assignment1 report and send it by e-mail (docx/link to google doc) or through creation repo fork + pull request.

### Instruction examples:

- https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04
- [How to remove disk from RAID1](https://unix.stackexchange.com/questions/332061/remove-drive-from-soft-raid)
- Minikube video tutorial (RUS) https://www.youtube.com/watch?v=Amkkr4_nsyc
- How to access Kubernetes Dashboard from outside network https://stackoverflow.com/questions/53957413/how-to-access-kubernetes-dashboard-from-outside-network 
- How to convert docx to rst \
  `pandoc -f docx -t rst -i in.docx -o out.rst`
