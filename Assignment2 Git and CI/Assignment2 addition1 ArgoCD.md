If our application runs in Kubernetes cluster

### Steps


1. Gitlab setup (on VM/Docker/Minikube)
(VM variant) Download Gitlab-Bitnami vm image from https://bitnami.com/stack/gitlab/virtual-machine

2. Create repo in gitlab with sources of your app
Upload your web app to your Gitlab server.

3. Setup ArgroCD. ArgoCD should:
* after commit to gitlab start build (if needed) of app
* ArgoCD deploy app to kubernetes
* ArgoCD test that app starts (optional minimal)
* ArgoCD test that app working as needed (optional)

5. Run CI/CD Pipeline to check that it works.