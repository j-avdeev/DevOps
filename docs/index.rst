.. If you want to see how this was created, check out this article:
   https://redandgreen.co.uk/sphinx-to-github-pages-via-github-actions/

Deployment and life cycle of a modern software
==============================================


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   lectures
   assignments

Course Outline
==============

1. Virtualization, hypervisors (Virtualbox, VMware)
2. Version Control Systems (VCS) Git
3. Operating-system-level virtualization, also known as "containerization" (Docker)
4. Continuous Integration
5. Monitoring tools

```mermaid
  graph BT;
      1-RAID-Minikube --> 1.1-Packer+0.2-pts;
      1-RAID-Minikube --> 1.2-Hello-Minikube+0.2-pts;
      2-Git-CI-Jenkins --> 2.1-Git-CI-ArgoCD+0.25-pts;
      2-Git-CI-Jenkins --> 2.1-Git-CI-Packer/Vagrant+0.25-pts;
      3-Helm;
      Assignment4;
```

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

