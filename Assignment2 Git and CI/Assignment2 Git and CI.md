## Assignment 2 - Git and CI

### Gitlab Docs:
https://docs.gitlab.com/

Video how it looks like (from 6:28): https://youtu.be/PeWiS-Shwos?t=388

### Steps


1. Gitlab setup (on VM/Docker/Minikube)
(VM variant) Download Gitlab-Bitnami vm image from https://bitnami.com/stack/gitlab/virtual-machine

2. Create repo in gitlab with sources of your app
Upload https://github.com/olindata/sample-gitlabci-cpp-project to your Gitlab server.

* To unblock SSH https://docs.bitnami.com/virtual-machine/faq/get-started/enable-ssh/ and then configure authentication, for example password-based https://docs.bitnami.com/virtual-machine/faq/get-started/enable-ssh-password/
* https://askubuntu.com/questions/204400/ssh-public-key-no-supported-authentication-methods-available-server-sent-publ

3. Setup runner (Gitlab, Docker, Jenkins, ArgroCD)
* Install GitLab Runner using the official GitLab repositories https://docs.gitlab.com/runner/install/linux-repository.html

* (Gitlab variant) Update /etc/gitlab/gitlab.rb to disable https on gitlab (yes, it is not for production)
```
    # use here your IP, but is must be HTTP
    external_url 'http://192.168.88.228'
    nginx['redirect_http_to_https'] = false
    nginx['ssl_verify_client'] = "off"
```
* Reconfigure GitLab for the changes to take effect:
```
    $ sudo gitlab-ctl reconfigure
```
* Register runner. Choose **shell** executor type. Use your ip and registration-token for command below:
```
    $ sudo gitlab-runner register --url http://192.168.88.228/ --registration-token yqjsLYNFrbjaC-QhmycE
```

4. Edit .gitlab-ci.yml to run runner in shell mode (without Docker)
```
    job:
      script:
            - g++ helloworld.cpp -o helloworld
```

5. Run Pipeline: **CI/CD > Pipelines > Run pipeline**

In Job Logs you should see something like this:
```
Running with gitlab-runner 14.3.2 (e0218c92)
  on debian Zv4xR9-x
Preparing the "shell" executor
00:00
Using Shell executor...
Preparing environment
00:00
Running on debian...
Getting source from Git repository
00:00
Fetching changes with git depth set to 50...
Reinitialized existing Git repository in /home/gitlab-runner/builds/Zv4xR9-x/0/root/sample-gitlabci-cpp-project/.git/
Checking out 69a8ab3b as main...
Removing helloworld
Skipping Git submodules setup
Executing "step_script" stage of the job script
00:01
$ g++ helloworld.cpp -o helloworld
Job succeeded
```
Make report with screens of:
  * `minicube version` command output
  * opened Dashboard in your web-browser (on your host)

6. Create Assignment2 report and send it by e-mail (docx/link to google doc) or through creation repo fork + pull request.
