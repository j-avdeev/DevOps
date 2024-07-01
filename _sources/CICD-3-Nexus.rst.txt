==============================================
Building a CI/CD Pipeline. Part3 Nexus Ansible
==============================================

1. Setup artifact manager tool, e.g. Nexus OSS, JFrox Artifactory free tier
2. Setup Ansible instance
3. Setup Jenkins "Publish over SSH" plugin to send JAR to Ansible server
4. (+0.5pts) Set Ansible playbook to create Docker image based on JAR and push image to DockerHub
5. (+0.5pts) Setup Jenkins-Nexus integration to send JAR to Nexus server. Modify Ansible playbook to create Docker image based on JAR grabbed from Nexus, modify playbook to send final Docker image to Nexus.
6. Add screenshot of JAR pushed to Nexus/Artifactory (if you made step 5) or Docker image pushed to DockerHub.

Jenkins-Artifactory integration: https://www.youtube.com/watch?v=k3_byI8Eql4