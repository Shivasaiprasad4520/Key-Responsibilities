1. Login AWS Console and then go to EC2 Dashboard Lunch Instance
   -
![Screenshot 2024-08-22 233554](https://github.com/user-attachments/assets/a7033252-98d0-4ee5-b5a4-df4bf8e70c0a)

_______________________________________________________________
2. Connect to the Instance Server by using Powershell or Mobaxterm with Keypair
   -
_______
3. After login into server update the server
   -
  sudo apt-get update -y
_______
4. Install AWS CLI in server following command is linux
   -
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  unzip awscliv2.zip
  sudo ./aws/install
______
5. Configure AWS CLI in server using Access Key and Secert Key
   -
6. Create shell scripting file in server
   -
   vi aws_resource_project.sh

 _______
7. Execute that file and see the Output 
   -
