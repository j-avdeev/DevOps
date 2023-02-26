## Assignment 1.1 - Packer
### What is Packer:
Packer is an open source tool for creating identical machine images for multiple platforms from a single source configuration.
https://developer.hashicorp.com/packer/docs/intro

### Steps
1. Install Packer on your host machine (https://developer.hashicorp.com/packer/downloads)
2. Modify `*.pkr.hcl` and `http\preseed.cfg` files (see packer folder in Assignment1) so it have to
  * create ubuntu-server vm image
  * this image have to include installed Kubernetes **minikube** cluster
3. Create Assignment report and send it by e-mail (docx/link to google doc) or through creation repo fork + pull request.

### Instruction examples:

Install VirtualBox and run from folder, which include `http` folder to build vm image \
`packer.exe build ubuntu-server.pkr.hcl` 

