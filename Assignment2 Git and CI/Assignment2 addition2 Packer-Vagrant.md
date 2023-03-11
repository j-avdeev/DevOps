If our application runs on Desktop

### Steps


1. Gitlab setup (on VM/Docker/Minikube)
(VM variant) Download Gitlab-Bitnami vm image from https://bitnami.com/stack/gitlab/virtual-machine

2. Create repo in gitlab with sources of your app
Upload your web app to your Gitlab server.

3. Setup Gitlab runner/Jenkins.

* (optional) create test vm with Packer/Vagrant: install OS and environment from scratch or based on "Golden Image"
* after commit to gitlab start runner, which start app build on test vm
* runner installs app
* runner test that app starts (optional minimal)
* runner test that app working as needed (optional)

5. Run CI/CD Pipeline to check that it works.