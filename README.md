# Key-Responsibilities

Showcasing and Leveraging the Skill-Set i have with Handson Practices in Various DevOps Tool and as Well in Platform's 
======================================================================================================================
* Platforms as Services :
   ======================

1) AWS  -:
   ======
   1.EC2 Instance
   --------------
   2.IAM User Role
   ----------------
   AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. With IAM, you can centrally manage permissions that control which AWS resources users can 
   access. You use IAM to control who is authenticated (sign in) and authorized (has permissions) to use resources.
   Way to Create IAM and Accessing and Adding MFA :
----------------------------------------------

1) To create IAM account login to the Root account and search IAM  in search bar then click on the IAM
  ![IAM](https://github.com/user-attachments/assets/b81f4be6-8ee2-4e67-a5cd-83de1807da4f)
2) Now in IAM go to the users then create  user
3) Step 1 --> Specify user details -->give user name --> then check-in "Provide user access to the AWS Management Console" --> give custom password --> then uncheck "users must create a new password at sign-in" ---> save it
 ![created iam](https://github.com/user-attachments/assets/e52c1a15-9f3b-45a4-b387-45c0826a0d31)

4) step 2 --> set permissions --> keep all defualt -> save it
5) step 3 --> review and create --> keep all defualt --> give tag --> create user 
6) Copy the Console sign-in url past it in the other browser and login with user name and password
   
 ![IAM account](https://github.com/user-attachments/assets/33d4504e-53f0-4cff-8bd3-cbaed50c80fc)
7) Premission are not assigned to IAM account for that we go back to root account and give access to IAM for that click on the user in Root -> IAM and apply permission to the user
8) Add Permission -->click on attach policies directly -->click on that permission do you want to give --> then next --> add permission

Multi-factor Authentication
      ![WhatsApp Image 2024-08-14 at 16 55 03_0da24c9f](https://github.com/user-attachments/assets/9c602a56-891b-45c5-a35f-f68763ec6cd7)

   3.VPC
   ---------
   4.S3 Bucket
   -----------
   5.Elastic File System
   ------------------------
   6.Elastic Load Balancer
   ------------------------
   7.Elastic Bean stack
   ------------------------
   8.Auto Scaling
   ------------------------
   9.lambda Function
   ------------------------
   10.Route 53
   ------------------------
   11.Cloud Formation
   ------------------------
   12.SNS
   ------------------------
   13.SQS
    ------------------------   
   14.Cloud Watch
   ------------------------
   
3) Azure  -:
   =======
   1.Virtual Machine
   ------------------------
   2.Azure Storage Services
   ------------------------
   3.Virtual Network
   ------------------------
   4.Bill and Management
   ------------------------
   5.Recovery Services Vault
   ------------------------
   6.Azure Monitoring
   ------------------------
   7.Azure Traffic Manager (Load Balancer)
   ------------------------

5) GCP -:
   ======
   
 ------------------------------------------------------------------------------------------------   
* DevOps Tools -:
  ============
1) Jenkins - CI/CD Implementation -:
   =================================
   1.Jenkins Integration
   ------------------------
   2.Jenkins User management
   ------------------------
   3.Role Based Authorization Strategy
   ------------------------
   4.Jenkins Pipeline
   ------------------------
   5.Jenkins Thin Backup
   ------------------------
   6.Multi - Branching Pipeline
   ------------------------
   ------------------------------------------------------------------------------------------------------------------------------------------------------------
   7.Jenkins - Slave Model
   -----------------------
   
 1) Create a ubuntu server Instance with port number 8080 and T2 medium For Jenkins Master 
    ![jenkins-master](https://github.com/user-attachments/assets/782b5ba5-2b43-4096-a4ac-ed689202d475)
    
 2) Connect Instance to mobaXterm and install Jenkins on the server 
  {
sudo apt-get update -y

sudo apt-get install openjdk-17-jdk -y

sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian/jenkins.io-2023.key

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt-get update

sudo apt-get install jenkins -y

sudo systemctl status jenkins
} 
3)after install Jenkins connect to browser with Jenkins (IP address:8080) then login 
  ![install jenkins](https://github.com/user-attachments/assets/16ad9c07-e4a0-455a-8cd7-4dea92c3c910)

4)After login Jenkins then create a agent server connect to server in mobaXterm go to root account 
  ![agent](https://github.com/user-attachments/assets/812e8cd6-fb58-4b33-bb63-c2286848d5d3)

5) In root account check present working  directory (cmd:pwd) then make a directory (cmd:mkdir jenkins-slave)

6) In that directory generate a SSH key (cmd:ssh-keygen) it generate three keys those are authoried key, private key, public key
   follow this cmd : ~ cd
                     cd /.ssh
                      ls or ll (u will see key)
  ![agent-install](https://github.com/user-attachments/assets/25a51545-223e-4cd1-88b3-5ef205afe0b3)

7) open public key and copy that key then open authorized key and paste the public key 

8) open private key copy that key then go to Jenkins master GUI following this steps
 jenkins-master -->Dashboard --> manage Jenkins -->click on credentials --> click on global --> add credential -->kind [SSH Username with private key] -->give ID, description, username
 --> enable enter directly then paste private key and create
   ![cred](https://github.com/user-attachments/assets/5373b7ad-ead4-4e03-9312-b9a53fe46adf)


9)install java latest version on agent server
  

10)integrate agent with master by using user based authentication
   in Jenkins master login -> Dashboard -> manage Jenkins -> nodes -> create new node -> node name(slave1) -> select permanent agent -> keep some default and give some following steps 
-> remote root directory (/home/ubuntu/jenkins-slave)-> labels (slave1) -> lunch method (lunch agent via ssh) -> host (IP address of the agent server) -> credentials (select the credential which is created in previous step) --> host key verification strategy (non verifying verification strategy) -> save

11)install git latest version on agent server
 
10)create a job on master and run job on agent for that run a job 
-->dashboard --> new item (name of the item)--> free style project -> select git with git repository URL --> build steps --> invoke top-level maven target-->maven version (maven3.6.9) 
--> goals (clean install package) --> save   ==> while run a job it runs in master node we want to run in slave for that -->click on job id go to configure in that general tab tick the restrict where this project can be run --> label expression (master or node id) then save it
   
3) Docker -:
   ======
   1.Docker Image
   ------------------------
   2.Docker File
   ------------------------
   3.Docker Hub
   ------------------------
   4.Docker Network
   ------------------------
   5.Docker Compose
   ------------------------
   6.Docker Volume
   ------------------------
   7.Docker Swarm
   ------------------------
   
5) Kubernets -:
   ============
   
   1.Minikube Setup
   ------------------------
   2.EKS Cluster Management Setup
   ------------------------
   3.Kubernetes Container
   ------------------------
   4.kubernets POD Troubleshooting
   ------------------------
   5.Rolling Update and Roll-Back Update
   ------------------------
   6.Kubernetes Containers
   ------------------------
   7.Kubernetes Network
   ------------------------

7) Ansible -:
   ==========
   1.Ansible Inventory Group with 3 Environment
   ------------------------
   2.Ansible Modules
   ------------------------
   3.Ansible Galaxy
   ------------------------
   4.Ansible roles
   ------------------------
   5.Ansible Tags
   ------------------------
   6.Ansible Vault
   ------------------------

9) Terraform -:
   ============

10) Promotheus -:
    ============

12) Grafana -:
    ==========
    
-------------------------------------------------------------------------------------------------
*  Scripting Languages :
   ===================

1) Python -:
   =========

2) Shell Scripting -:
   ==================
   linux-commands:
   --------------
   linux for shell scripting
1  `hashtag#ls` :List directory contents 📂
2. `hashtag#cd`: Change directory 🔄
3. `hashtag#pwd`: Print working directory 📍
4. `hashtag#mkdir`: Create a directory 📁
5. `hashtag#touch`: Create a file ✏️
6. `hashtag#cp`: Copy files and directories 📋
7. `hashtag#mv`: Move / Rename files and directories 🔄
8. `hashtag#rm`: Remove files and directories ❌
9. `hashtag#find`: Search for files and directories 🔍
10. `hashtag#grep`: Search for patterns in files 🔎
11. `hashtag#cat`: Concatenate and display files 📑
12. `hashtag#less`: View file contents page by page 📄
13. `hashtag#head`: Display the first lines of a file 🗂️
14. `hashtag#tail`: Display the last lines of a file 📜
15. `hashtag#vi/vim`: Text editor 🖋️
16. `hashtag#nano`: Text editor ✏️
17. `hashtag#tar`: Archive and compress files 📦
18. `hashtag#gzip`: Compress files 🗜️
19. `hashtag#gunzip`: Decompress files 🔓
20. `hashtag#wget`: Download files from the web ⬇️
21. `hashtag#curl`: Transfer data to or from a server 🌐
22. `hashtag#ssh`: Secure shell remote login 🔒
23. `hashtag#scp`: Securely copy files between hosts 🔐
24. `hashtag#chmod`: Change file permissions 🛠️
25. `hashtag#chown`: Change file ownership 👤
26. `hashtag#chgrp`: Change group ownership 👥
27. `hashtag#ps`: Display running processes 🖥️
28. `hashtag#top`: Monitor system resources and processes 📊
29. `hashtag#kill`: Terminate processes 🚫
30. `hashtag#df`: Display disk space usage 💾
31. `hashtag#du`: Estimate file and directory space usage 📈
32. `hashtag#free`: Display memory usage 🧠
33. `hashtag#uname`: Print system information ℹ️
34. `hashtag#ifconfig`: Configure network interfaces 🌐
35. `hashtag#ping`: Test network connectivity 📶
36. `hashtag#netstat`: Network statistics 📉
37. `hashtag#iptables`: Firewall administration 🔥
38. `hashtag#systemctl`: Manage system services ⚙️
39. `hashtag#journalctl`: Query the system journal 📜
40. `hashtag#crontab`: Schedule cron jobs ⏲️
------------------------------------------------------------------------------------------------
*  Version Controlling Tool :
   =======================

 1) GitHub -:
    ========
   1.Distributed Version Control
   ------------------------
   2.Git Workflow
   ------------------------

   ![git work flow](https://github.com/user-attachments/assets/9390180d-4b2a-4af4-80a5-53ca0896a116)

   3.Git Brunching Strategy
   ------------------------
  Branches are independent lines of work, stemming from the original codebase. Developers create separate branches for independently working on features so that changes from other developers don’t interfere with an individual’s line of work. Developers can easily pull changes from different branches and also merge their code with the main branch. This allows easier collaboration for developers working on one codebase.
  
The following are the steps for creating a branch
1) To Create a branch with the name you want to specify, here we are naming the branch name as “new-feature”.
   git branch new-feature
2) Now navigate to the new feature branch from the current branch with the following command:
   git checkout  new-feature
3) To Check Current Branch
   git branch
4) To Merge the branch to master
   git merge new-feature
5) Ensure you are present on the branch you want to delete.
   git branch -d

   4.Git Stashing
   ------------------------
   5.Git Conflicts
   ------------------------
   6.Git Tags
   ------------------------
   7.Git Clone
   ------------------------
   8.Git Re-Base
   ------------------------
   9.Cherry-Pick
   ------------------------
   
