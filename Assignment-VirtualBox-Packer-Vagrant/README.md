Instructions for Assignment4
========================================
In this Assignment you will learn how to work with Packer and Vagrant (ang VirtualBox, Git by the way).

Actually in this Assignment you will:
* create VM box with settings from packer-template,
* convert VM box to VM image with Vagrant,
* clone from github npm-based application and test it with Grunt.

Packer - is an open source tool for creating identical machine images for multiple platforms from a single source configuration.
Vagrant - is a tool for building and managing virtual machine environments in a single workflow.


After installing the required tools, you will need to ensure that your computer can find the executables to run them. For this, you might need to modify the PATH environment variable. A good overview is at [superuser.com](https://superuser.com/questions/284342/what-are-path-and-other-environment-variables-and-how-can-i-set-or-use-them). You may need to search the web for instructions on how to set the PATH variable for your specific operating system and version. 

## Setting up your local machine

* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
* Install [Packer](https://www.packer.io/downloads.html)
* Clone the forked repo to your local machine using this command: `git clone https://github.com/j-avdeev/DevOps/tree/master/Assignment1-VirtualBox-Packer-Vagrant-Git`, or just download repo to your local machine.

## Part I: Building a box with Packer

From the packer-templates directory on your local machine:
* Copy packer binary file to "packer-templates" folder
* Looks like modern Node.js has problems with old Ubuntu 14 support (https://www.youtube.com/watch?v=1OjeWuo339s) so try to use more modern Ubuntu disto.
* Run `packer build -only=virtualbox-iso application-server.json` to create virtual machine box accrodingly to application-server scenario.
You may see various timeouts and errors, as shown below. If you do, read Troubleshooting or retry the command until the ISO download succeeds:

```
read: operation timed out
==> virtualbox-iso: ISO download failed.
Build 'virtualbox-iso' errored: ISO download failed.

checksums didn't match expected
==> virtualbox-iso: ISO download failed.
Build 'virtualbox-iso' errored: ISO download failed.

==> Some builds didn't complete successfully and had errors:
--> virtualbox-iso: ISO download failed.
```

* Run `cd virtualbox` to go to packer-templates/virtualbox folder
* Run `vagrant box add ubuntu-14.04.4-server-amd64-appserver_virtualbox.box --name devops-appserver`
* Run `vagrant up`
* Run `vagrant ssh` to connect to the server


## Part II: Cloning, developing, and running the web application

* On your virtual-ghost machine run `git clone https://github.com/chef/devops-kungfu.git devops-kungfu`
* Open http://localhost:8080 from your host-machine browse to see the app running.
* In the VM, run `cd devops-kungfu`
* To install app specific node packages, run `sudo npm install`. You may see several errors; they can be ignored for now.
* Now you can run tests with the command `grunt -v`. The tests will run, then quit with an error.

### Troubleshooting

If you encounter errors with Ubuntu version numbers not being available or checksum errors on Ubuntu,it means that this repository has not yet been updated for the latest Ubuntu version. Meanwhile, you can fix this error for yourself by editing the contents of the `application-server.json` and `control-server.json` template files inside the `packer-templates` folder.

* Find the newest version number and checksum from the [Ubuntu website for this release](http://releases.ubuntu.com/trusty/)
* Edit `PACKER_BOX_NAME` and `iso_checksum` in the template files to match that version number and checksum.

### Outcome

Create docx report with work description and Grunt test output and send by e-mail for checking.
