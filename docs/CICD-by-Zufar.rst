==============================================================================================================
Building a CI/CD Pipeline with AWS, K8S, Docker, Ansible, Git, Github, Apache Maven, and Jenkins \| HackerNoon
==============================================================================================================

Source: https://hackernoon.com/building-a-cicd-pipeline-with-aws-k8s-docker-ansible-git-github-apache-maven-and-jenkins


.. rubric:: **Motivation**
   :name: h-motivation

CI/CD is a technique for delivering apps to customers,
achieved by adding automation to different stages of
app development. I believe that grasping CI/CD
(Continuous Integration and Continuous Deployment) can
empower developers to gain a better understanding of
how backend project artifacts exist beyond the
boundaries of the project repository. This
comprehension can also create a fundamental shift in a
developer's perspective. Instead of merely viewing
their work as lines of code, they can start to embrace
the broader context of their project as a valuable
product.


In this article, we aim to demystify the CI/CD process
through practical application. We'll take you through
a step-by-step tutorial, breaking it down module by
module, where you'll build a CI/CD pipeline manually.
To do this, we'll harness the power of contemporary
DevOps tools like **AWS, Docker, Kubernetes, Ansible,
Git, Apache Maven,** and **Jenkins**. So, let's begin
this journey!


.. rubric:: **[Module 1]: AWS EC2 Virtual Server**
   :name: h-module-1-aws-ec-2-virtual-server

This module is dedicated to the creation of an AWS EC2
Virtual Server instance. As part of this article, you
will be setting up three EC2 instances for Jenkins,
Ansible, and Kubernetes. For now, you can proceed with
the next modules and revisit this module in "[module
2]: Jenkins", “[module 6]: Ansible" and "[module 7]:
Kubernetes" sections.

| 

.. rubric:: **Step 1: Create an AWS Account**
   :name: h-step-1-create-an-aws-account

Go to https://aws.amazon.com.

Click the button **Create an AWS Account**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-1.png
    :scale: 50 %
    
    The screenshot of AWS main web page with the
    pointer to "Create an AWS Account" button

Follow the instructions on the create account web
page.

.. rubric:: **Step 2: Sign In to your AWS Account**
   :name: h-step-2-sign-in-to-your-aws-account
    
Go to https://console.aws.amazon.com/console/home.
Click the **Sign In** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-2.png
    :scale: 50 %

    The screenshot of AWS main web page with the
    pointer to "Sign In" button

Enter all necessary credentials on this web page.

.. rubric:: **Step 3: Find EC2 Virtual Server**
    :name: h-step-3-find-ec-2-virtual-server
    
Find EC2 in the search box.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-3.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    the search box

Choose EC2 Virtual Server by clicking **EC2 Service**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-4.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "EC2" AWS service

Click the button **Launch Instance**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-5.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Launch instance" button


.. rubric:: **Step 4: Configure “Name and tags“
    section**
    :name: h-step-4-configure-name-and-tags-section

Go to the **“Name and tags”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-6.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Name and tags" section

Provide a name for a new AWS EC2 Virtual Server
instance in the **“Name”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-7.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Name" input box in "Name and tags" section

You can also add additional tags for your virtual
server by clicking **”Add additional tags”**.


.. rubric:: **Step 5: Configure “Application and OS
    Images (Amazon Machine Image)“ section**
    :name: h-step-5-configure-application-and-os-images-amazon-machine-image-section

Go to the **"Application and OS Images (Amazon Machine
Image)"** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-8.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Application and OS Images (Amazon Machine Image)"
    section

.. note::
    To play with the virtual server for **FREE**:

    #. Select the operating system for your virtual
        server - **Amazon Linux**.
    #. In the **Amazon Machine Image (AMI)** section,
        select a machine with the **Free tier eligible
        tag**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-9.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "OS" and "Machine type" buttons in "Application and
    OS Images (Amazon Machine Image)" section


.. rubric:: **Step 6: Configure “Instance type“
    section**
    :name: h-step-6-configure-instance-type-section

Go to the **”Instance type”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-10.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Instance type" section

To play with the virtual server for **FREE**:

Select a type with the **Free tier eligible
tag** in the **Instance type** section.

For me it is **t2.micro (Family: t2 1cCPU 1 GiB
Memory Current generation:true)**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-11.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Instance type" dropdown in "Instance type" section

.. rubric:: **Step 7: Configure “Configure storage“
    section**
    :name: h-step-7-configure-configure-storage-section

Go to the **”Configure storage”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-12.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Configure storage" section

.. note::
    To play with the virtual server for **FREE**:
    Do not change default settings. Free tier eligible
    customers can get **30 GB of EBS General Purpose
    (SSD) or Magnetic storage**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-13.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    storage possible configurations in "Configure
    storage" section

.. rubric:: **Step 8: Configure “Network settings“
    section**
    :name: h-step-8-configure-network-settings-section

Go to the **“Network settings“** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-14.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Network settings" section

You need to set up the security of your virtual
server. To do this,

#. Click on the **“Create security group”** button.
#. Add the name of your new security group in
the **“Security group name”** section.
#. Add a description of your new security group in
the **“Description”** section.

By default, your virtual server is accessible via
(**Type - SSH, Protocol - TCP, Port - 22**). If you
need additional connection types, add them by adding
additional inbound security group rules.    

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-15.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Security group" in "Network settings" section

.. rubric:: **Step 9: Configure “Key pair (login)“
   section**
   :name: h-step-9-configure-key-pair-login-section

Go to the **”Key pair (Login)”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-16.png

    The screenshot of AWS web page with the pointer to
    "Ket pair (login)" section

Create a new key-pair if you haven't created it yet.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-17.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Key pair name", "Key pair type", "Private key file
    format" in "Ket pair (login)" section

If you haven't created **“key-pair”** yet:

#. Click the **“Create new key pair”** button.
#. Give your new key-pair a name in the **“Key pair
   name”** section.
#. Select key-pair type **RSA** or **ED25519**. I
   choose the **RSA** type.
#. Select Private key file format. Choice
   of **.pem** and **.ppk**. I choose
   the **.pem** format.
#. Click on the **“Create key pair”** button.
#. You will get a pop-up window that will prompt you
   to download the Private key file. Agree and
   download the file to your computer.

.. rubric:: **Step 10: Launch the EC2 Virtual Server
   Instance**
   :name: h-step-10-launch-the-ec-2-virtual-server-instance

Launch the EC2 Virtual Server instance by clicking the
button **“Launch instance”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-18.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Launch Instance" button

After the completion of the EC2 Virtual Server
instance creation process, you will see the following.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-19.png
    :scale: 50 %

    The screenshot of the AWS web page displaying a
    'Success' notification, indicating the successful
    completion of the EC2 Virtual Server instance
    creation process

Then you should go to the **“Instances“** section by
clicking **“View all instances”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-20.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    running EC2 instance

Now you can see that your AWS EC2 Virtual Server
instance is running.

--------------

.. rubric:: **[Module 2]: Jenkins Server**
   :name: h-module-2-jenkins-server

Now, let’s configure JenkinsServer on the EC2 Virtual
Server instance.

.. rubric:: **Step 1: Create an AWS EC2 Virtual Server
   instance**
   :name: h-step-1-create-an-aws-ec-2-virtual-server-instance

You need a virtual server to run Jenkins.

Follow instructions from **[Module 1]: AWS EC2 Virtual
Server** section of this tutorial to finish this step
and create an EC2 virtual server instance with the
name JenkinsServer.

.. warning::
   Do not forget to add a security group setup. It
   allows **Jenkins** and **SSH** to work on
   port **8080** and **22** respectively.

.. note::
   Use the name **“JenkinsServer”** to distinguish
   your EC2 Virtual Server instance.

.. note::
   Create **“CI_CD_Pipeline”** security group
   and **“CI_CD_Pipeline_Key_Pair“** for a
   new **“JenkinsServer”** AWS EC2 instance. You can
   reuse them further in the article.

.. rubric:: **Step 2: Connect to an AWS EC2 Virtual
   Server instance**
   :name: h-step-2-connect-to-an-aws-ec-2-virtual-server-instance

Go to **AWS Console home page** → **EC2 Management
Console Dashboard** → **Instances.**

Then you should choose **JenkinsServer** and then
click the **“Connect”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-21.png
    :scale: 50 %

    The screenshot of AWS "Instances" web page with the
    pointer to "Connect" button


Then you will see this web page. You should again
click the **“Connect”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-22.png
    :scale: 50 %

    The screenshot of AWS "Connect to Instance" web
    page with the pointer to "Connect" button


Now you can see EC2 virtual server instance online
terminal.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-23.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    online terminal

.. rubric:: **Step 3: Download the Jenkins
   repository**
   :name: h-step-3-download-the-jenkins-repository

Now you need to download Jenkins on your EC2 virtual
server instance.

Follow these instructions:

#. Go to Jenkins
   download `webpage <https://www.jenkins.io/download>`__.

#. You can see Stable (LTS) and Regular releases
   (Weekly) options. Choose `Red
   Hat/Fedora/Alma/Rocky/CentOS <https://pkg.jenkins.io/redhat-stable>`__\ LTS
   option.

You will see this web page.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-24.png
    :scale: 50 %

    The screenshot of Jenkins download web page

3. Copy **“sudo get..”** command and execute it to
   download Jenkins files from the Jenkins repository
   on the Internet and save them to the specified
   location on your EC2 virtual server instance.

.. code:: bash

   sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo

Now Jenkins is downloaded.


.. rubric:: **Step 4: Import Jenkins key**
   :name: h-step-4-import-jenkins-key

To finish the Jenkins installation, we need to import
the Jenkins key.

To import the Jenkins key we need to copy the **“sudo
rpm..”** command and execute it.

.. code:: bash

   sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key

.. container:: notice notice-info

   This way **“rpm”** package manager can verify that
   the Jenkins packages you install are exactly the
   ones published by the Jenkins project, and that
   they haven't been tampered with or corrupted.

.. rubric:: **Step 5: Install Java**
   :name: h-step-5-install-java

To run Jenkins, we need to install **Java** on our EC2
virtual server instance.

To install **Java**, use this command.

| 

.. code:: bash

   sudo amazon-linux-extras install java-openjdk11 -y

| 

Verify whether
**Java**
was installed correctly using this command:

.. code:: bash

   java -version

You will see something like that.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-25.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    online terminal with installed JDK 11

.. rubric:: **Step 6: Install fontconfig**
   :name: h-step-6-install-fontconfig

To run Jenkins, you need to install **fontconfig** on
our EC2 virtual server instance.

Use this command.

.. code:: bash

   sudo yum install fontconfig java-11-openjdk -y

.. note::

   Fontconfig is a library designed to provide
   system-wide font configuration, customization and
   application access. It's required by Jenkins
   because Jenkins has features that render fonts.

.. rubric:: **Step 7: Install Jenkins**
   :name: h-step-7-install-jenkins

In earlier steps, you configured your EC2 virtual
server instance to use a specific Jenkins repository
and then you imported the GPG key associated with this
repository. Now, you need to run the command that will
search all the repositories it knows about, including
the Jenkins one you added, to find the Jenkins
package. Once it finds the Jenkins package in the
Jenkins repository, it will download and install it.

Let’s run this command.

.. code:: bash

   sudo yum install jenkins -y

.. rubric:: **Step 8: Start Jenkins**
   :name: h-step-8-start-jenkins

You can start Jenkins using this command.

.. code:: bash

   sudo systemctl start jenkins

To check that Jenkins is running use this command.

.. code:: bash

   sudo systemctl status jenkins

You will see the output as it is on the screenshot
below:

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-26.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    online terminal with installed Jenkins

Jenkins should now be up and running.

.. rubric:: **Step 9: Access Jenkins**
   :name: h-step-9-access-jenkins

To access the Jenkins application, open any web
browser and enter your EC2 instance’s public IP
address or domain name followed by port 8080.

.. code:: bash

   http://<your-ec2-ip>:8080

The first time you access Jenkins, it will be locked
with an autogenerated password.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-27.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to Administrator
    password

You need to display this password using the following
command.

.. code:: bash

   sudo cat /var/lib/jenkins/secrets/initialAdminPassword

Copy this password, return to your browser, paste it
into the Administrator password field, and click
"Continue".

Then you will be able to see this web page.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-28.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to "Customize
    Jenkins" web page

Now, you can use your Jenkins Server.

.. rubric:: **Step 10: Create new Jenkins pipeline**
   :name: h-step-10-create-new-jenkins-pipeline

Now, as Jenkins is working fine, you can start
creating the Jenkins pipeline. To create Jenkins
pipeline you need to create a new “Freestyle project”.
To create a new “Freestyle project” you need to go to
the Jenkins dashboard and click the **“New
Item”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-29.png
    :scale: 50 %

    The screenshot of Jenkins Dashboard web page with
    the pointer to "New Item" button

Enter the name of the Github “Freestyle project”
(“pipeline” name is going to be used further) and then
click the button **“OK”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-30.png
    :scale: 50 %

    The screenshot of Jenkins New Item web page with
    the pointer to "Item name" item box

Then provide the **Description** of the pipeline.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-31.png
    :scale: 50 %

    The screenshot of Jenkins Job configuration web
    page with the pointer to "Description" input box

Then click the button “Apply” and “Save”. After that,
it means you created the fundament of the pipeline
which is going to be built in this tutorial.

.. rubric:: **[Module 3]: Git and Github**
   :name: h-module-3-git-and-github

Now as Jenkins is running on AWS EC2 Virtual Server
instance, you can configure Git with the pipeline.

.. container:: notice notice-info

   Git is a `free and open
   source <https://git-scm.com/about/free-and-open-source>`__ distributed
   version control system (VCS) designed to help
   software teams keep track of every modification to
   the code in a special kind of database. If a
   mistake is made, developers can turn back the clock
   and compare earlier versions of the code to help
   fix the mistake while minimizing disruption to all
   team members. VCS is especially useful
   for `DevOps <https://www.atlassian.com/devops/what-is-devops>`__ teams
   since they help them to reduce development time and
   increase successful deployments [1].

Git as the most popular version control system enables
us to pull the latest code from your project Github
repository to your EC2 virtual server instance where
your Jenkins is installed.

.. rubric:: **Step 1: Install Git**
   :name: h-step-1-install-git

Use this command to install Git.

.. code:: bash

   sudo yum install git -y

Now verify Git is working, using this command.

.. code:: bash

   git --version

Now Git is working fine on EC2 Virtual Server
instance.

.. rubric:: **Step 2: Open Jenkins dashboard**
   :name: h-step-2-open-jenkins-dashboard

As Git is working fine on EC2 Virtual Server instance,
we can integrate Jenkins with Git now.

To start this integration let’s install Jenkins Github
plugin.

Go to Jenkins dashboard section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-32.png
    :scale: 50 %

    The screenshot of Jenkins dashboard

.. rubric:: **Step 3: Open Jenkins Plugin Manager**
   :name: h-step-3-open-jenkins-plugin-manager

Click the button **“Manage Jenkins”** and then click
the button **“Manage Plugins”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-33.png
    :scale: 50 %

    The screenshot of Jenkins dashboard with the
    pointer to "Manage Plugins" button


.. rubric:: **Step 4: Find Github Jenkins plugin**
   :name: h-step-4-find-github-jenkins-plugin

Click the button **“Available plugins”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-34.png
    :scale: 50 %

    The screenshot of Jenkins Plugin Manager web page
    with the pointer to "Available plugins" button

Find the **Github** plugin Search box.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-35.png
    :scale: 50 %

    The screenshot of Jenkins Plugin Manager web page
    with the pointer to "Github" plugin

Select **Github** plugin.

.. rubric:: **Step 5: Install Github Jenkins plugin**
   :name: h-step-5-install-github-jenkins-plugin

Select **Github** plugin. And then click the
button **“Install without restart”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-36.png
    :scale: 50 %

    The screenshot of Jenkins Plugin Manager web page
    with the pointer to "Install without restart"
    button

Wait for the end of the Github plugin downloading.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-37.png
    :scale: 50 %

    The screenshot of Jenkins Plugin Manager web page
    with the downloading Github plugin

Yes! The Jenkins Github plugin is installed.

.. rubric:: **Step 6: Configure Github Jenkins
   Plugin**
   :name: h-step-6-configure-github-jenkins-plugin

Now as the GitHub Jenkins plugin is installed, you can
configure this plugin to integrate Jenkins with Git
finally. To do that you need to return to the main
page by clicking the button “Go back to the top page”.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-38.png
    :scale: 50 %

    The screenshot of Jenkins Plugin Manager web page
    with the pointer to "Go back to the top page"
    button

Then on the main page, you need to click the
button **“Manage Jenkins”** and then click the
button **“Global tool configuration”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-39.png
    :scale: 50 %

    The screenshot of Jenkins Plugin Manager web page
    with the pointer to "Global tool configuration"
    button

Then on the Global Tool Configuration web page you
should go to the Git section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-40.png
    :scale: 50 %

    The screenshot of Jenkins Global Tool Configuration
    web page with the pointer to "Name" and "Path to
    Git executable" input boxes

In the Git section, you need to configure Git by
providing the name and path to Git on the computer.

Then click the
**“Apply”** and **“Save”** buttons**.*\*

Here, you have finished configuring the Jenkins Github
plugin.

.. rubric:: **Step 7: Integrate Git into the
   pipeline**
   :name: h-step-7-integrate-git-into-the-pipeline

Now, as the Jenkins Github plugin is installed and
configured, you're now able to utilize this plugin
within your pipeline. This will allow your pipeline
which you created in module 2 to pull your project
code from the specified GitHub repository.

Well, to integrate this plugin into your pipeline you
need to go to the Source Code Management section and
choose Git in your pipeline. Then you need to provide
your project repository URL. If your project
repository is public on Github, you do not need to
provide credentials. If the project repository is
private on Github, you need to provide credentials.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-41.png
    :scale: 50 %

    The screenshot of Jenkins Job configuration web
    page with "Source Code Management" settings

You can use my project with the next Repositiry
URL: `https://github.com/Sunagatov/Hello.git <https://github.com/Sunagatov/Hello.git>`__.

Just copy and paste it to the “\ **Repository
URL”** input. Then click the
**“Apply”** and **“Save”** buttons to finish the
integration Git with the pipeline.

.. rubric:: **Step 8: Test Git integrated into the
   pipeline**
   :name: h-step-8-test-git-integrated-into-the-pipeline

Now you can use your updated pipeline to pull a
project from Github. To do that you need to click
the **“Build Now”**button. As a result, you will see a
successful build in the build history.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-42.png
    :scale: 50 %

    The screenshot of Jenkins web page with pointers to
    "Build Now" button and "Build History" section

Open the first build from the build history.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-43.png
    :scale: 50 %

    The screenshot of Jenkins Pull_Code_From_Github_Job
    with successful job result

Now you can see the successful job result of the first
build. If you open your AWS EC2 terminal. You can
check that the pipeline works well.

Just use this command.

.. code:: bash

   cd /var/lib/jenkins/workspace/{your pipeline name}

This way you can see that your project from Github was
pulled to your AWS EC2 virtual server instance.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-44.png
    :scale: 50 %

    The screenshot of Github project downloaded into
    EC2 instance terminal

.. rubric:: **[Module 4]: Apache Maven**
   :name: h-module-4-apache-maven

.. note::

   **Apache Maven** is a widely used build automation
   and project management tool in software
   development. It streamlines the process of
   compiling, testing, and packaging code by managing
   project dependencies and providing a consistent
   build lifecycle. Maven employs XML-based
   configuration files (POM files) to define project
   structure, dependencies, and tasks, enabling
   developers to efficiently manage and deploy complex
   software projects.

Now that you have integrated Git into the pipeline,
you can enhance the pipeline further by incorporating
Apache Maven which enables you to build, test, and
package your project. To do that you need to install
Apache Maven on your AWS EC2 Virtual Server instance
where Jenkins and Git were installed.

.. rubric:: **Step 1: Download Apache Maven**
   :name: h-step-1-download-apache-maven

To download Apache Maven go to the
**“/opt”** directory.

.. code:: bash

   cd /opt

And then use this command.

.. code:: bash

   sudo wget https://dlcdn.apache.org/maven/maven-3/3.9.4/binaries/apache-maven-3.9.4-bin.tar.gz

This command will download the latest official Apache
Maven (check the latest version on the official Apache
Maven website). To find the latest official Apache
Maven release, use the
link `https://maven.apache.org/download.cgi <https://maven.apache.org/download.cgi>`__.


.. rubric:: **Step 2: Extract Apache Maven from the
   archive**
   :name: h-step-2-extract-apache-maven-from-the-archive

Use this command, to extract Apache Maven from the
downloaded archive:

.. code:: bash

   sudo tar -xvzf apache-maven-*.tar.gz

.. rubric:: **Step 3: Add JAVA_HOME and M2_HOME**
   :name: h-step-3-add-java-home-and-m-2-home

Move to the root folder using this command.

.. code:: bash

   cd ~

Edit **.bash_profile** file using this command.

.. code:: bash

   vi .bash_profile

Add **JAVA_HOME** and M2_HOME variables.

Assign the path to JDK11 for **JAVA_HOME** and path to
the maven directory for **M2_HOME** variable.

To find JDK path, use this command.

.. code:: bash

   sudo find / -name java

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-45.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal web page with .bash_profile file

.. note::

   **How to use VIM**

   -  To **edit** the file press the keyboard
      button **“ I “** to insert data.
   -  To **save** the file press the keyboard button “
      esc “ and enter “:w“.
   -  To **exit** from the file press the keyboard
      button **“ esc “** and enter **“:q”**.

Save the changes.

Then, execute this command to refresh system
variables.

.. code:: bash

   source .bash_profile

To verify **$PATH**, use this command.

.. code:: bash

   echo $PATH

To verify **Apache Maven**, use this command.

.. code:: bash

   mvn -v

If you have done everything correctly, you will be
able to view the version of Apache Maven.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-46.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal web page with the version of Apache Maven

.. rubric:: **Step 4: Install Apache Maven Jenkins
   plugin**
   :name: h-step-4-install-apache-maven-jenkins-plugin

Since Apache Maven can be used on an EC2 instance, you
can install the Apache Maven plugin to integrate it
with the pipeline.

**To achieve this, follow these steps:**

#. Navigate to **“Dashboard“** **→ “Manage Jenkins“ →
   “Manage Plugins“ → “Available”.**
#. In the search box, enter **“Maven”**.
#. Choose **“Maven Integration”** plugin.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-47.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to Maven plugin

Wait for the end of the downloading process.

And then click the button **“Go back to the top
page”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-48.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to Maven plugin
    downloading process

.. rubric:: **Step 5: Configure Apache Maven Jenkins
   plugin**
   :name: h-step-5-configure-apache-maven-jenkins-plugin

With the successful installation of the Apache Maven
Jenkins plugin, you are now able to utilize this
plugin within the pipeline which you created and
updated in modules 2 and 3.

**To do so, follow these steps:**

#. Go to **“Dashboard“** **→ “Manage Jenkins“ →
   “Global Tool Coonfiguration“ → “JDK”**
#. Click the button **“Add JDK”.**
#. Uncheck **“Install automatically”.**

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-49.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to JDK
    configuration

Then go to **“Maven”** section. Click the
button **“Add Maven”**. Uncheck **“Install
automatically”.**

Then add **name** and **MAVEN_HOME** path.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-50.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to Apache Maven
    configuration

Click the **“Apply”** and **“Save”** buttons.

Here, you have finished configuring the Apache Maven
Jenkins plugin.

.. rubric:: **Step 6: Integrate Apache Maven into the
   pipeline**
   :name: h-step-6-integrate-apache-maven-into-the-pipeline

Now as the Apache Maven GitHub plugin is installed and
configured, you're now able to utilize Apache Maven
within your pipeline. This will allow your pipeline
which you created in the “[module 2]: Jenkins Server”
to build your project code to create a jar artifact.

**To integrate Apache Maven into the pipeline you need
to follow these steps:**

#. Navigate to **“Dashboard“** **→ “CI_CD_Pipeline“ →
   “Configure“ → “Build Steps”.**
#. Click **“Add build step”** button.
#. Choose **“Invoke top-level Maven targets”** option.
#. Choose **“Apache-Maven”** as **“Maven Version”.**
#. Add **“clean package”** command
   to **“Goals”** input.
#. Click **“Advanced“** button.
#. Add “pom.xml” to **“POM”** input.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-51.png
    :scale: 50 %

    The screenshot of "Build Steps" section in the
    pipeline configuration with pointers to "Apply" and
    "Save" buttons

Finally, you should
click **“Apply”** and **“Save”** buttons to finish the
integration of Apache Maven with the pipeline.

.. rubric:: **Step 7: Test Apache Maven integrated
   into the pipeline**
   :name: h-step-7-test-apache-maven-integrated-into-the-pipeline

Now you can use your updated pipeline to build your
Github project. To do that you need to click
the **“Build Now”**button. As a result, you will see a
successful job result in the build history.

If you open your AWS EC2 terminal. You can check that
the pipeline works well.

Just use this command.

.. code:: bash

   cd /var/lib/jenkins/workspace/{your pipeline name}/target

This way you can see the JAR artifact, indicating the
successful build of your project from GitHub.

.. rubric:: **[Module 5]: Docker**
   :name: h-module-5-docker

Now let’s create a new EC2 instance with the name
"Ansible Server" where you are going to install Docker
and Ansible.

.. rubric:: **Step 1: Launch an AWS EC2 Virtual Server
   instance**
   :name: h-step-1-launch-an-aws-ec-2-virtual-server-instance

Use instructions from “\ **Launch an AWS EC2 Virtual
Server instance”** section of this tutorial to finish
this step. Do not forget to add a security group
setup. It allows Docker and SSH to work on ports 8080
and 22 respectively.

.. rubric:: **Step 2: Connect to an AWS EC2 Virtual
   Server instance**
   :name: h-step-2-connect-to-an-aws-ec-2-virtual-server-instance

Click the “Connect” button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-52.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Connect" button

Now you can see the EC2 Virtual Server instance online
terminal.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-53.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    online terminal

.. code:: bash

   sudo chown ansible-admin:ansible-admin /opt/docker

.. rubric:: **Step 3: Install Docker on the Ansible
   EC2 virtual server.**
   :name: h-step-3-install-docker-on-the-ansible-ec-2-virtual-server

Now you need to install docker on your Ansible EC2
instance. To do that you need to create a new docker
folder.

.. code:: bash

   sudo mkdir /opt/docker

Then, install docker by executing the next command.

.. code:: bash

   sudo yum install docker -y

.. rubric:: **Step 4: Add current user to Docker group
   on Ansible EC2 virtual server**
   :name: h-step-4-add-current-user-to-docker-group-on-ansible-ec-2-virtual-server

You need to add the current
user **“ansible-admin”** to the Docker group on the
**“AnsibleServer”** EC2 virtual server to give Docker
admin privileges.

.. code:: bash

   sudo usermod -a -G docker ansible-admin

You will need to logout and log back in for these
changes to take effect.

Then you can execute the next command

.. code:: bash

   id ansible-admin

to see that the new docker user exists.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-54.png
    :scale: 50 %

    The screenshot of Ansible EC2 instance with the
    pointer to the docker user

.. rubric:: **Step 5: Launch Docker**
   :name: h-step-5-launch-docker

Now as Docker is installed on the Ansible EC2 instance
you can launch it by executing the next command.

.. code:: bash

   sudo systemctl start docker

As Docker is started you can execute the next command

.. code:: bash

   sudo systemctl status docker

to see that docker is active and running now.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-55.png
    :scale: 50 %

    The screenshot of Ansible EC2 instance with the
    active docker status

.. rubric:: **Step 6: Create Dockerfile**
   :name: h-step-6-create-dockerfile

In the final version of the pipeline, the process will
involve creating a new Docker image from your GitHub
project and pushing it to Docker Hub. To accomplish
this, your GitHub project should contain a Dockerfile.

If you used the project **“Hello”** which was offered
in “\ **[Module 3]: Git and Github”** module, then you
don’t need to create a new Dockerfile as this project
repository has already contained Dockerfile.

.. code:: bash

   FROM eclipse-temurin:17-jre-jammy
   ENV HOME=/opt/app
   WORKDIR $HOME
   ADD hello-0.0.1-SNAPSHOT.jar $HOME
   ENTRYPOINT ["java", "-jar", "/opt/app/hello-0.0.1-SNAPSHOT.jar" ]

If you used your own project repository and it didn't
contain a Dockerfile, you will need to create a new
Dockerfile.

To create a new Dockerfile, execute the following
command, which will create the new file.

.. code:: bash

   sudo touch Dockerfile

Then you can fill this file with a sequence of
commands that describe how to build a containerized
application environment. These commands include
actions like copying files into the image, installing
software, setting environment variables, and
configuring the container.

To fill the Dockerfile with these commands, execute
the following command.

.. code:: bash

   vim Dockerfile

The Dockerfile is ready to use.

.. rubric:: **Step 7: Login Docker**
   :name: h-step-7-login-docker

Now that your Dockerfile is prepared for use, proceed
by copying your project's JAR artifact from
the **"JenkinsServer"**EC2 instance and pasting it
onto the **"AnsibleServer"** EC2 instance. It is
important to note that this transfer will be automated
through the pipeline further.

By completing this step, you'll be ready to test your
Dockerfile along with the Docker environment you've
set up.

Before you begin testing, make sure to authenticate
yourself on Dockerhub. Execute the following command.

.. code:: bash

   docker login

This command will prompt you to provide your Dockerhub
login credentials, including your username and
password.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-56.png
    :scale: 50 %

    The screenshot of successful docker login in
    "AnsibleServer" EC2 instance

With this, you have completed the process of logging
into
`Docker <https://hackernoon.com/306-stories-to-learn-about-docker>`__
and are now ready to proceed with testing.

.. rubric:: **Step 8:** Testing the Docker environment
   and Dockerfile
   :name: h-step-8-testing-the-docker-environment-and-dockerfile

With your successful login to Dockerhub completed, you
are now ready to begin testing the Dockerfile you have
prepared.

Execute this command to create a docker image.

.. code:: bash

   docker build -t hello:latest .

Next, execute the subsequent command to establish a
tag that will facilitate the image's upload to
Dockerhub:

.. code:: bash

   docker tag hello:latest zufarexplainedit/hello:latest

Finally, proceed to push the Docker image to Dockerhub
through the execution of this command.

.. code:: bash

   docker push zufarexplainedit/hello:latest

Following these steps, navigate to your Dockerhub
account to verify whether you can see a new image or
not.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-57.png
    :scale: 50 %

    The screenshot of Dockerhub account with the new
    image added

You should now observe that the image has been
effectively added. This outcome confirms the
successful installation of the Docker environment and
that your Dockerfile is correct.

.. rubric:: **[Module 6]: Ansible**
   :name: h-module-6-ansible

Now let us configure the Ansible Server on the EC2
Virtual Server instance.

.. rubric:: **Step 1: Create an AWS EC2 Virtual Server
   instance**
   :name: h-step-1-create-an-aws-ec-2-virtual-server-instance

You need a virtual server to run Ansible.

Follow instructions from **[Module 1]: AWS EC2 Virtual
Server** section of this tutorial to finish this step
and create an EC2 virtual server instance for Ansible.

.. warning::

   Do not forget to add a security group setup. It
   allows **Ansible** and **SSH** to work on
   port **8080** and **22** respectively.

.. note::

   Use the name **“AnsibleServer”** to distinguish
   your EC2 Virtual Server instance.

.. note::

   You can reuse **“CI_CD_Pipeline”** security group
   and **“CI_CD_Pipeline_Key_Pair“** for a
   new **“AnsibleServer”** EC2 instance.

.. rubric:: **Step 2: Connect to an AWS EC2 Virtual
   Server instance**
   :name: h-step-2-connect-to-an-aws-ec-2-virtual-server-instance

Go to AWS Console home page → EC2 Management Console
Dashboard → Instances → AnsibleServer.

Then click the **“Connect”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-58.png
    :scale: 50 %

    The screenshot of AWS web page with the pointer to
    "Connect" button

Then you will see this web page. You should again
click the **“Connect”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-59.png
    :scale: 50 %

    The screenshot of AWS "Connect to Instance" web
    page with the pointer to "Connect" button

Now you can see the EC2 virtual server instance online
terminal.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-60.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    online terminal

Now let’s configure Ansible Server on EC2 virtual
server instance.

.. rubric:: **Step 3: Change the hostname of
   “AnsibleServer” AWS EC2 Virtual Server instance**
   :name: h-step-3-change-the-hostname-of-ansible-server-aws-ec-2-virtual-server-instance

The first thing you need to do when you want to
configure AnsibleServer on EC2 virtual server instance
is changing its hostname.

Let’s do it. Execute this command to open hostname
file:

.. code:: bash

   sudo vi /etc/hostname

You should see something like this:

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-61.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    with hostname file

Replace this hostname with **“ansible-server”.** Then,
reboot it.

.. code:: bash

   sudo init 6

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-62.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the pointer to hostname

.. rubric:: **Step 4: Add and configure a new user in
   “AnsibleServer” AWS EC2 Virtual Server instance**
   :name: h-step-4-add-and-configure-a-new-user-in-ansible-server-aws-ec-2-virtual-server-instance

Now let’s add a new **ansible-admin** user to the AWS
EC2 Virtual Server instance.

To do that use this command:

.. code:: bash

   sudo useradd ansible-admin

Then, set the password for **ansible-admin** user.

.. code:: bash

   sudo passwd ansible-admin

Also, you need to configure user privileges by editing
the **sudoers** file.

.. code:: bash

   sudo visudo

Add **“ansible-admin ALL=(ALL) ALL”** to
this **sudoers** file.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-63.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the pointer to admin privileges

Also, you need to edit **/etc/ssh/sshd_config** file
to enable PasswordAuthentication.

.. code:: bash

   sudo vi /etc/ssh/sshd_config

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-64.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the pointer to admin settings

Then you need to reload the service to confirm these
changes.

.. code:: bash

   sudo service sshd reload

As a result of executing this command, you will see:

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-65.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the pointer to sshd reload result

.. note::

   Now you can use this command to avoid adding sudo
   for all further commands.

   .. code:: bash

      sudo su - ansible-admin

.. rubric:: **Step 5: Generate key in an AWS EC2
   Virtual Server instance**
   :name: h-step-5-generate-key-in-an-aws-ec-2-virtual-server-instance

You are planning to manage remote servers such as K8s
EC2 virtual server instances further in this article.
That is why you need to set up SSH keys.

.. code:: bash

   ssh-keygen

As a result of executing this command, you will see:

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-66.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the pointer to ssh-keygen result

Now SSH keys are generated and ready to use.

.. rubric:: **Step 6: Install Ansible**
   :name: h-step-6-install-ansible

Now you can install Ansible on
your **“AnsibleServer”** EC2 virtual server instance.

Let’s do it.

Execute this command to install Ansible.

.. code:: bash

   sudo amazon-linux-extras install ansible2

To verify Ansible, use this command:

.. code:: bash

   ansible --version

As a result of executing this command, you will see:

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-67.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the pointer to sudo yum install
    ansible result

.. rubric:: **Step 7: Install Jenkins “Publish over
   SSH“ plugin on JenkinsServer EC2 instance**
   :name: h-step-7-install-jenkins-publish-over-ssh-plugin-on-jenkins-server-ec-2-instance

As Ansible is installed on
your **“AnsibleServer”** EC2 virtual server instance,
you can configure Jenkins to integrate it with
Ansible. You need to install the **“Publish over
SSH”** plugin to integrate Jenkins with the EC2
Virtual Server instance where Ansible is installed and
with other EC2 Virtual Server instances where
`Kubernetes <https://hackernoon.com/419-stories-to-learn-about-kubernetes>`__
is installed.

Go to **“Dashboard”** → “\ **Manage
Jenkins”** → **“Configure System”** → **“Available
plugins”**.

Then enter **“Publish over SSH“** in the search box.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-68.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to "Available
    plugins" web page

Click the button **“Install without restart”**. Wait
for the end of the downloading process.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-69.png
    :scale: 50 %

    The screenshot of Jenkins installed on AWS EC2
    Virtual Server with the pointer to "Download
    progress" web page

Now the “Publish over SSH” plugin is installed on the
Jenkins EC2 Virtual Server instance.

.. rubric:: **Step 8: Configure Jenkins “Publish over
   SSH“ plugin**
   :name: h-step-8-configure-jenkins-publish-over-ssh-plugin

With the successful installation of the Apache Maven
Jenkins plugin, you are now able to utilize this
plugin within the pipeline which you created and
updated in modules 2 and 3.

**To do so, follow these steps:**

Go to **“Dashboard“** → **“Manage
Jenkins”** → **“Configure System”** → **“Publish over
SSH”**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-70.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the "Publish over SSH" plugin

Enter all required data as it is on the screenshot,
including hostname, username, and private key (or
password if applicable).

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-71.png
    :scale: 50 %

    The screenshot of AWS EC2 Virtual Server instance
    terminal with the "Publish over SSH" plugin

Then click the **“Apply”** and **“Save”** buttons.

Here you have finished configuring the **“Publish over
SSH“** Jenkins plugin.

Next, click “Test Configuration” to validate that the
plugin is working correctly.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-72.png
    :scale: 50 %

    The screenshot of the "Publish over SSH" plugin
    with the button "Test Configuration"

On the left side you can see that the test plugin
configuration status is “Success”. It means the plugin
configuration is correct.

.. rubric:: **Step 9: Create new Docker directory in
   AnsibleServer**
   :name: h-step-9-create-new-docker-directory-in-ansible-server

You need to make a new folder on the AnsibleServer EC2
instance where the project JAR will be stored. This
jar will be used for creating a Docker image later.

Let’s start.

Go to **“/opt”** folder in AnsibleServer EC2 instance.

.. code:: bash

   cd /opt

Create a new folder **“docker”** there.

.. code:: bash

   sudo mkdir docker

Give privileges to this **“docker”** folder.

.. code:: bash

   sudo chown ansible-admin:ansible-admin docker

Now, check the **“docker”** folder privileges by
executing this command.

.. code:: bash

   ll

You can see that the **“docker”** folder is accessible
with the **“ansible-admin”** user.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-73.png
    :scale: 50 %

    The screenshot of "docker" folder in
    "AnsibleServer" EC2 instance

.. rubric:: **Step 10: Integrate “Publish over
   SSH“** Github plugin into **the pipeline**
   :name: h-step-10-integrate-publish-over-ssh-github-plugin-into-the-pipeline

Now as **“Publish over SSH“** Github plugin is
installed and configured, you're now able to integrate
it into the pipeline which you created in the “[module
2]: Jenkins Server” to transfer a project jar artifact
from “\ **JenkinsServer”** to **“AnsibleServer”**.

Well, to integrate **“Publish over SSH“** Github
plugin into the pipeline you need to follow these
steps:

#. Navigate to **“Dashboard“** **→ “CI_CD_Pipeline“ →
   “Configure“ → “Post-build Actions”.**
#. Click **“Add post-build action”** button.
#. Choose **“Send build artifacts over SSH”** option.
#. Add **“AnsibleServer”** into **“Name”** input
   in **“SSH Server”** section**.*\*
#. Add  **“target/*.jar”** into **“Source
   files”** input in **“Transfer Set”** section**.*\*
#. Add  **“target/”** into **“Remove prefix”** input
   in **“Transfer Set”** section**.*\*
#. Add  **“//opt/docker/”** into **“Remote
   directory”** input in **“Transfer
   Set”** section**.*\*
#. For now, simply put an empty string in the 'Exec
   command' input under the 'Transfer Set' section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-74.png
    :scale: 50 %

    The screenshot of "Send build artifact over SSH"
    section in the pipeline configuration

Finally, you should
click **“Apply”** and **“Save”** buttons to finish the
integration **“Publish over SSH“** plugin with the
pipeline.

.. rubric:: **Step 11: Test “Publish over
   SSH“** Github plugin **integrated into the
   pipeline**
   :name: h-step-11-test-publish-over-ssh-github-plugin-integrated-into-the-pipeline

Now you can use your updated pipeline to transfer a
project jar artifact from
“\ **JenkinsServer”** to **“AnsibleServer”**. To do
that you need to click the **“Build Now”** button. As
a result you will see a successful job result in the
build history.

If you open your **“AnsibleServer”** AWS EC2 terminal.
You can check that the pipeline works well.

Just use this command.

.. code:: bash

   cd /opt/docker

This way you can see the JAR artifact, indicating the
successful build of your project from GitHub.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-75.png
    :scale: 50 %

    The screenshot of /opt/docker directory with the
    project jar artifact

.. rubric:: **Step 12: Configure Ansible hosts**
   :name: h-step-12-configure-ansible-hosts

When you run an Ansible playbook, you specify the
hosts it should run on. You can do this in two ways:

#. **Specify hosts directly in the playbook:** In your
   playbook, you can set the ``hosts`` parameter to a
   list of IP addresses or hostnames.
#. **Use an inventory file:** Ansible allows you to
   define a list of hosts in an inventory file and
   reference this file when running your playbook. The
   default inventory file is ``/etc/ansible/hosts``.

By editing ``/etc/ansible/hosts``, you can easily
manage groups of hosts without having to write out
their IP addresses each time you run a playbook.

Let’s find out the AnsibleServer EC2 instance host by
executing the following command.

.. code:: bash

   sudo ifconfig

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-76.png
    :scale: 50 %

    The screenshot of the network interface setting of
    AnsibleServer EC2 instance

After you find out AnsibleServer EC2 instance host,
you can add it to the Ansible hosts file by executing
the following command.

.. code:: bash

   sudo vi /etc/ansible/hosts

You can also add “[ansible]” as a reference

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-77.png
    :scale: 50 %

    The screenshot of Ansible hosts file

.. note::

   If you're managing a cluster of servers and you
   want to apply a playbook to all of them, instead of
   specifying each server's IP address in the
   playbook, you can simply add all the servers to a
   group in the inventory file and then specify the
   group in the playbook.

