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
--------------

1. Virtualization, hypervisors (Virtualbox, VMware)
2. Version Control Systems (VCS) Git
3. Operating-system-level virtualization, also known as "containerization" (Docker)
4. Continuous Integration
5. Monitoring tools


Videos
------
- DevOps Lecture 01: DevOps Lifecycle | - |[2020'RUS](https://www.youtube.com/watch?v=BD2BxNY6F58) 
- DevOps Lecture 02: RAID VM Docker | [2021'RUS](https://www.youtube.com/watch?v=FRlZuZ6d14E) | [2020'RUS](https://www.youtube.com/watch?v=BC19Gl2u4wc) | [2019'ENG](https://www.youtube.com/watch?v=lOhF1R2QrkU) 
- DevOps Lecture: Docker [2021'RUS](https://www.youtube.com/watch?v=MclSAaC4A_c)
- DevOps Lecture 03: Git GitLab CI | [2019'ENG](https://www.youtube.com/watch?v=NILYhfa35vs) | [2020'RUS](https://www.youtube.com/watch?v=S85in_KPPnY)
- DevOps Lecture 04: Zabbix Web Scenario | [2019'ENG](https://www.youtube.com/watch?v=Qe9_KXIAW98)
- DevOps Lecture 05: Zabbix Agent | [2019'ENG](https://www.youtube.com/watch?v=uUteBUB85_A) | [2020'RUS](https://youtu.be/Ak9VbVCpkjk)

References
----------
- Github Student Pack https://education.github.com/pack

- Bash
  * `Beginner's Guide to the Bash Terminal (ENG) <https://www.youtube.com/watch?v=oxuRxtrO2Ag>`_ (cd, making directory, editing files, sudo etc.)
  * Bash - [Linux Command Line Pipes and Redirection (ENG)](https://www.youtube.com/watch?v=mV_8GbzwZMM)
- Kubernetes
  * [Minikube video tutorial (RUS)](https://www.youtube.com/watch?v=Amkkr4_nsyc)
  * [Kubenetes course by Слёрм (RUS)](https://www.youtube.com/playlist?list=PL8D2P0ruohOBSA_CDqJLflJ8FLJNe26K-)

- Git
  * Git — инструмент для совместной работы с нуля и до регламента в команде — Александр Васильев [RUS] | https://www.youtube.com/watch?v=XfpNNPo5ypk
  * Git Cheat Sheet https://github.com/arslanbilal/git-cheat-sheet
  * Git, list of links https://github.com/dictcp/awesome-git
- Cloud
  * [AWS Solution Architect interview questions & concepts](https://www.teamblind.com/article/AWS-Solution-Architect-interview-questions--concepts-in7y48S7)
  * [Google Cloud Platform Free Tier](https://cloud.google.com/free/)

- How to convert docx to rst \
  `pandoc -f docx -t rst -i in.docx -o out.rst`

- [MLOps: Continuous delivery and automation pipelines in machine learning](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [Coursera: Проектирование и реализация систем машинного обучения](https://www.coursera.org/learn/machine-learning-design)
- Kubernetes The Hard Way by Kelsey Hightower. This tutorial walks you through setting up Kubernetes the hard way https://github.com/kelseyhightower/kubernetes-the-hard-way
- I took some funny pictures from [Udacity: Intro to DevOps](https://classroom.udacity.com/courses/ud611/)

Textbooks:
----------

* O'Reilly Media, Linux in a Nutshell
* Джез Хамбл, Дейвид Фарли, Непрерывное развертывание: Автоматизация процессов сборки, тестирования и внедрения новых версий программ
* O'Reilly, Managing Kubernetes: Operating Kubernetes Clusters in the Real World by Craig Tracey, Brendan Burns
* O'Reilly, Cloud Native DevOps with Kubernetes, Justin Domingus and John Arundel


.. list-table:: Assignment Deadlines 'Autumn 2023
   :widths: 30 20 20 20 20
   :header-rows: 1

   * - ...
     - 1-Git-Jenkins
     - 2-Docker
     - 3-Kubernetes
     - 4-Monitoring
   * - Soft Deadline (50% reduction if missed)
     - 15.10.2023 (1 pts)
     - 22.10.2023 (1 pts)
     - 15.04.2023 (0.5 pts)
     - 15.04.2023 (0.5 pts)
   * - Hard Deadline (100% reduction if missed)
     - 22.10.2023 (0.5 pts)
     - 05.11.2023 (0.5 pts)
     - 22.04.2023 (0.25 pts)
     - 22.04.2023 (0.25 pts)


Some assignments has Additions. Additional assignments are optional. Additional assignments have no deadlines.


.. mermaid::

   graph BT;
      1-RAID-Minikube --> 1.1-Packer+0.2-pts;
      1-RAID-Minikube --> 1.2-Hello-Minikube+0.2-pts;
      2-Git-CI-Jenkins --> 2.1-Git-CI-ArgoCD+0.25-pts;
      2-Git-CI-Jenkins --> 2.1-Git-CI-Packer/Vagrant+0.25-pts;
      3-Helm;
      Assignment4;


