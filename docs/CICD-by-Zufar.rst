==============================================================================================================
Building a CI/CD Pipeline with AWS, K8S, Docker, Ansible, Git, Github, Apache Maven, and Jenkins \| HackerNoon
==============================================================================================================

.. rubric:: Content Overview
   :name: h-content-overview

-  **Motivation**
-  **[Module 1]: AWS EC2 Virtual Server**
-  **[Module 2]: Jenkins Server**
-  **[Module 3]: Git and Github**
-  **[Module 4]: Apache Maven**
-  **[Module 5]: Docker**
-  **[Module 6]: Ansible**
-  **[Module 7]: Kubernetes**
-  **Conclusion**
-  **About the Author**

| 

| 

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

| 

In this article, we aim to demystify the CI/CD process
through practical application. We'll take you through
a step-by-step tutorial, breaking it down module by
module, where you'll build a CI/CD pipeline manually.
To do this, we'll harness the power of contemporary
DevOps tools like **AWS, Docker, Kubernetes, Ansible,
Git, Apache Maven,** and **Jenkins**. So, let's begin
this journey!

| 

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
    
    The screenshot of AWS main web page with the
    pointer to "Create an AWS Account" button

Follow the instructions on the create account web
page.

.. rubric:: **Step 2: Sign In to your AWS Account**
   :name: h-step-2-sign-in-to-your-aws-account
    
Go to https://console.aws.amazon.com/console/home.
Click the **Sign In** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-2.png

    The screenshot of AWS main web page with the
    pointer to "Sign In" button

Enter all necessary credentials on this web page.

.. rubric:: **Step 3: Find EC2 Virtual Server**
    :name: h-step-3-find-ec-2-virtual-server
    
Find EC2 in the search box.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-3.png

    The screenshot of AWS web page with the pointer to
    the search box

Choose EC2 Virtual Server by clicking **EC2 Service**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-4.png

    The screenshot of AWS web page with the pointer to
    "EC2" AWS service

Click the button **Launch Instance**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-5.png

    The screenshot of AWS web page with the pointer to
    "Launch instance" button


.. rubric:: **Step 4: Configure “Name and tags“
    section**
    :name: h-step-4-configure-name-and-tags-section

Go to the **“Name and tags”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-6.png

    The screenshot of AWS web page with the pointer to
    "Name and tags" section

Provide a name for a new AWS EC2 Virtual Server
instance in the **“Name”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-7.png

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

    The screenshot of AWS web page with the pointer to
    "OS" and "Machine type" buttons in "Application and
    OS Images (Amazon Machine Image)" section


.. rubric:: **Step 6: Configure “Instance type“
    section**
    :name: h-step-6-configure-instance-type-section

Go to the **”Instance type”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-10.png

    The screenshot of AWS web page with the pointer to
    "Instance type" section

To play with the virtual server for **FREE**:

Select a type with the **Free tier eligible
tag** in the **Instance type** section.

For me it is **t2.micro (Family: t2 1cCPU 1 GiB
Memory Current generation:true)**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-11.png

The screenshot of AWS web page with the pointer to
"Instance type" dropdown in "Instance type" section

.. rubric:: **Step 7: Configure “Configure storage“
    section**
    :name: h-step-7-configure-configure-storage-section

Go to the **”Configure storage”** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-12.png

The screenshot of AWS web page with the pointer to
"Configure storage" section

.. note::
    To play with the virtual server for **FREE**:
    Do not change default settings. Free tier eligible
    customers can get **30 GB of EBS General Purpose
    (SSD) or Magnetic storage**.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-13.png

    The screenshot of AWS web page with the pointer to
    storage possible configurations in "Configure
    storage" section

.. rubric:: **Step 8: Configure “Network settings“
    section**
    :name: h-step-8-configure-network-settings-section

Go to the **“Network settings“** section.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-14.png

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

The screenshot of AWS web page with the pointer to
"Launch Instance" button

After the completion of the EC2 Virtual Server
instance creation process, you will see the following.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-19.png

The screenshot of the AWS web page displaying a
'Success' notification, indicating the successful
completion of the EC2 Virtual Server instance
creation process

Then you should go to the **“Instances“** section by
clicking **“View all instances”** button.

.. figure:: media/CICD-by-Zufar/CICD-by-Zufar-20.png

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


