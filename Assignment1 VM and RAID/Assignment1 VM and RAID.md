## Assignment 1 - VM and RAID1
### What is RAID:
https://en.wikipedia.org/wiki/RAID

### Steps
1. Create virtual machine with debian/ubuntu/centos or download
   preinstalled image (https://www.osboxes.org/). It should be withoug GUI.
   1.1 You will need at least 20 GB of free space on your VM for steps 6 and 7
2. Set hostname = your surname.
3. Add simple raid1 to virtual machine: \*nix os system on 1-st hdd, 2d
   and 3d hdds are in raid1. 1 (with star). Only two hdds. Os system on
   raid1, based on this two hdd.
4. How to test raid1. Create file on raid1 file system. Turn off vm and
   remove one of the hhds from vm. Turn on vm. File should be
   accessible.
5. Add new hdd and sync it to raid1.
6. Install and run local Kubernetes cluster with **minikube**  
  * Use steps from `Kubernetes install Tools` https://kubernetes.io/docs/tasks/tools/ 
Make report with screens of:
  * `minicube version` command output
  * opened Dashboard in your web-browser
  * web-abblication in your web-browser (http://localhost:7080/ in tutorial)
7. Deploy hello-minikube app
8. Create Assignment1 report and send it by e-mail (docx/link to google doc) or through creation repo fork + pull request.

### Instruction examples:

- https://www.digitalocean.com/community/tutorials/how-to-create-raid-arrays-with-mdadm-on-ubuntu-16-04
- [How to remove disk from RAID1](https://unix.stackexchange.com/questions/332061/remove-drive-from-soft-raid)
- Minikube video tutorial (RUS) https://www.youtube.com/watch?v=Amkkr4_nsyc
- How to convert docx to rst \
  `pandoc -f docx -t rst -i in.docx -o out.rst`
