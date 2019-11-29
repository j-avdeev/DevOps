## Assignment 2 - RAID1
### What is RAID:
https://en.wikipedia.org/wiki/RAID

### Steps
1. Add simple RAID1 to on Virtual Machine from Assignment1:
*nix OS System on 1-st HDD, 2d and 3d HDDs are in RAID1.
2. How to test RAID1. Create file on RAID1 file system. Turn off VM and remove one of the HHDs from VM. Turn on VM. File should be accessble.
3. Add section with Assignment2 description into docx and send by e-mail for checking.

### Instruction examples:

- https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04
- (How to remove disk from RAID1) https://unix.stackexchange.com/questions/332061/remove-drive-from-soft-raid

## Assignment 3 - Gitlab CI
### What is going on?
In this assignment you will touch Gitlab CI

### Steps
1. Create/Install/Deploy your own Gitlab server.
For example you can use vm from bitnami collection: https://bitnami.com/stack/gitlab
2. Clone/Copy "sample-gitlabci-cpp-project" repo to your GitLab server
https://github.com/olindata/sample-gitlabci-cpp-project
3. If you are attentive, you found that sample-gitlabci-cpp-project uses Docker.
So you need to integrate Docker in your GitLab.
* 3.1. Install GitLab Runner (if you do not made it before)
https://docs.gitlab.com/runner/install/linux-repository.html
* 3.2. Integrate Docker
https://docs.gitlab.com/ee/ci/docker/README.html
https://docs.gitlab.com/ee/ci/docker/using_docker_images.html
4. Make some repairs if for some reason Job is failed.

## Assignment 4 - Zabbix

### What is going on?
In this assignment you will touch with Zabbix monitoring tool

### Steps
1. Create/Install/Deploy your own Zabbix server.
Hint: Zabbix supports preinstalled Zabbix-servers "Zabbix Appliances" VMware/VirtualBox/KVM images https://www.zabbix.com/download_appliance

Login:password for appliance is
* System
appliance:zabbix
* Frontend
Admin:zabbix
https://www.zabbix.com/documentation/4.0/manual/appliance

2. Setup agents:
* 2.1 Execute extended Web monitoring scenario setup, based on following manual https://www.zabbix.com/documentation/3.4/manual/web_monitoring/example
* 2.2 Agent for SMART status monitoring. On Windows or Linux host - as you prefer. This would be helpful (https://share.zabbix.com/storage-devices/smart-monitoring-with-smartmontools-lld) or other available tutorial.


## Assignment 5 - Docker
ToDo