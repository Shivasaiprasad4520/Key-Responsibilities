amazon Linux default user  -->ec2-user
------------------------
ubuntu default user  -->ubuntu
-------------------
CentOS  -->centos
-----
RHEL  -->ec2-user
----
windows default user  -->Administrator
--------------------


Linux family
============

1) debein family:
1 ubuntu
2 fedora
3 AVlinux
4GRML
{* apt-get --> package manager
   apt-get install java -y}
   _______________________________
2)Redhut family
1RHEL
2CentOS
3Suselinux
4Amazon linux
{* yum --> package manager
   yum install java -y}
   
----------------------------------------------------

Linux: basic commands -:
=====================
 -> user management, swap management, sim link, hard link, dics management, process management, services management, AWS Volume, NFS, file system

cd /opt
df -h
lsblk
lsblk -f
mkfs.ext4 /dev/xvdx
ll
mkdir data
ll
mount /dev/xvdd /opt/data
df -h
cat /etc/fstab



logic volume management-:
==============
LVM  Architecture :
       |
       v 
Physical Hard Disks  (its a volume or Disk of the Server and it is a default one)
       |
       v
 Physical Volume     (in this we create a physical volume from the disk, in this we actually create one or use multiply volume )
       |              cmd: pvcreate
       v
  Volume Group       (in this we sum up the physical volume into a group then we call it as a group volume, we can add multiply volume into one group)
       |              cmd: vgcreate
       v
  Logical Group      (in this we will divide into multiply volume from group volume)
       |               cmd: lvcreate
       v
  File system        (in this we create log file or install software in it )
------------------------------------------------------------------------------

to check the disk in vm we use and it show case that raw disk
cmd: parted -l

listing in block state
cmd: lsblk

to create physical volume 
cmd: pvcreate /dev/sdb or c,d,e,f

to check the physical volume created or not 
cmd: pvs  and cmd: pvdisplay (if we use this command we can see in depth)

to create a volume group
cmd: vgcreate volg_1 /dev/sbd /dev/sdc     [vgcreate+"nameofthevolumegroup"+"/dev/sdc"] if u want to add one more volume then [vgcreate+"nameofthevolumegroup"+"/dev/sdc" "/dev/sdb"]

to check the volume group created or not
cmd: vgs or vgs -v

to create logic volume 
cmd: lvcreate -L 4G -n logvol_1 volg_1     [lvcreate -L +"howmuch-GB-allocate" -n+nameofthelogicalvolume+volumegroupname]

to check the volume group created or not
cmd: lvs

in previous step 1 logical volume created now we want to format that logical volume then mount on a directory for that we make file system
cmd: mkfs.ext4 /dev/vg

cmd: mkfs.ext4 /dev/vlog_1/logvol_1         [mkfs.ext4 /dev/+groupvolume+logicalvolume]

cmd: partprobe      {this cmd is for what thinks are going in system that are to update to kernel:}

to mount logic volume to particular directory named as shiva
cmd: mount /dev/volg_1/logvol_1 /shiva/

to check that is mounted or not
cmd: df -h

to watch directory we use following cmd
cmd: watch df -h /dev/mapper/vlog_1-logvol_1     [df -h + pathnameofdirectory]

now if logical file system is full then we want extend to the existing one
cmd: lvextend -L+5G /dev/vlog-1/logvol-1

to update file system we resize the directory
cmd: resize2fs /dev/mapper/volg-1/logvol-1
------------------------------------
snapshot:
to create a snapshot for a volume or file
cmd: lvcreate -s -n sai_snapshot -L 1G /dev/mapper/vlog_1-logvol_1
     [lvcreate -s for snapshot -n for name sai_snapshot -L 1G how much gb for snapshot + path of the file]

to merge the snapshot to original logical volume
cm: lvconvert --mergesnapshot /dev/vlog-1/sai_snapshot

to reterive the data we should deactivate and activate then the data will update
cmd: umount /shiva/
cmd: lvchange -an /dev/mapper/vlog_1-logvol_1    --> deactivate
cmd: lvchange -ay /dev/mapper/vlog_1-logvol_1    --> activate
cmd: mount /dev/mapper/vlog_1-logvol_1 /shiva/


----------------
*why we use LVM ?
#) in our file system when we make a partition to a volume or disk then the one of the partitioned volume is fulled, then we extend the space in the partitioned through Logical volume and if space is there in other partitioned volume we can use that with the help of  sink . if in case partitioned volume is filled then we create a physical hard disk and allocate that if its root or home or anywhere we can allocate

physical volume  --cmd pvcreate /dev/xvdd
volume group     --cmd vgcreate gem /dev/xvdd
logical volume   --cmd lvcreate -n jam -l gam 

cmd: pvcreate /dev/xvdd
cmd:   

==============================
utilization (monitoring)
df -h (human readable)

free -m ()
cd /etc/systemd/system

Here are ten essential troubleshooting commands for Linux systems, often used by DevOps and Site Reliability Engineers (SREs):

1.top
 - Displays real-time system information, including running processes, CPU usage, memory usage, and more.
 top
 
2. htop
 - An improved version of `top` with a more user-friendly interface and additional features.
 htop
 
3. ps
 - Displays information about active processes. Commonly used with options to filter or format output.
 ps aux 

4. netstat
 - Displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
 netstat -tuln

5. ss
 - Provides detailed information about socket connections, similar to `netstat`, but with more modern features and better performance.
 ss -tuln

6. df
 - Displays the amount of disk space used and available on mounted file systems.
 df -h
 
7. du
 - Estimates file space usage, often used to find large files and directories.
 du -sh 
 
8. dmesg
 - Prints the kernel ring buffer messages, useful for diagnosing hardware and driver issues.
 dmesg | less

9. journalctl
 - Queries and displays logs from `systemd` journal, which captures logs from various system services and applications.
 journalctl -xe
 

10.ping
 - Tests the reachability of a host on an IP network and measures the round-trip time for messages sent to the destination
 ping google.com

11.traceroute
 - Displays the route packets take to a network host, useful for diagnosing network path issues.
 traceroute google.com

12.curl
 - Transfers data from or to a server using various protocols, often used for testing API endpoints and network services.
 curl -I http://example.com
 
13.nslookup:-
 - Queries Internet name servers interactively to find DNS details, such as IP addresses associated with a domain.
 nslookup example.com

14.lsof:- 
 - Lists open files and the processes that opened them, helpful for diagnosing issues related to file locks and network ports.
 lsof -i ;8080

15.Free:-
 - Displays the amount of free and used memory in the system.
 free -h
------------------------------------------------------------------------------
Certainly! Here's a list of commands related to each of the specified categories in Linux:

### User Management
1. `adduser` or `useradd` - Add a new user
2. `passwd` - Change user password
3. `deluser` or `userdel` - Delete a user
4. `usermod` - Modify a user account
5. `chown` - Change file owner and group
6. `groups` - Show user’s groups
7. `id` - Display user identity

### Swap Management
1. `swapon` - Enable swap space
2. `swapoff` - Disable swap space
3. `mkswap` - Set up a Linux swap area
4. `free` - Display amount of free and used memory in the system, including swap
5. `top` or `htop` - Display system summary information, including swap usage
6. `fallocate` - Create a swap file
7. `dd` - Create a swap file (e.g., `dd if=/dev/zero of=/swapfile bs=1M count=1024`)

### Symbolic Link (Sim Link)
1. `ln -s target link_name` - Create a symbolic link

### Hard Link
1. `ln target link_name` - Create a hard link

### Disk Management
1. `fdisk` - Partition table manipulator for Linux
2. `parted` - A partition manipulation program
3. `lsblk` - List information about block devices
4. `blkid` - Locate/print block device attributes
5. `mount` - Mount a file system
6. `umount` - Unmount file systems
7. `df` - Report file system disk space usage
8. `du` - Estimate file space usage
9. `mkfs` - Build a Linux file system
10. `fsck` - File system consistency check and repair

### Process Management
1. `ps` - Report a snapshot of current processes
2. `top` or `htop` - Display Linux tasks
3. `kill` - Send a signal to a process
4. `killall` - Kill processes by name
5. `pkill` - Look up or signal processes based on name and other attributes
6. `nice` - Run a program with modified scheduling priority
7. `renice` - Alter priority of running processes
8. `bg` - Resume a stopped job in the background
9. `fg` - Bring a background job to the foreground

### Services Management
1. `systemctl` - Control the systemd system and service manager
2. `service` - Run a System V init script
3. `chkconfig` - System V init script management
4. `update-rc.d` - Install and remove System-V style init script links

### AWS Volume Management
1. `aws ec2 describe-volumes` - Describe Amazon EBS volumes
2. `aws ec2 create-volume` - Create an Amazon EBS volume
3. `aws ec2 delete-volume` - Delete an Amazon EBS volume
4. `aws ec2 attach-volume` - Attach an Amazon EBS volume to an instance
5. `aws ec2 detach-volume` - Detach an Amazon EBS volume from an instance

### NFS (Network File System)
1. `showmount` - Show mount information for an NFS server
2. `mount -t nfs` - Mount an NFS share
3. `exportfs` - Maintain the table of exported NFS file systems
4. `nfsstat` - Print NFS statistics
5. `rpcinfo` - Report RPC information
6. `systemctl start/stop/restart nfs-server` - Manage NFS server service

### File System Management
1. `mkfs.ext4` - Create an ext4 file system
2. `tune2fs` - Adjust tunable file system parameters on ext2/ext3/ext4 file systems
3. `mount` - Mount a file system
4. `umount` - Unmount file systems
5. `df` - Report file system disk space usage
6. `du` - Estimate file space usage
7. `fsck` - File system consistency check and repair
8. `e2fsck` - Check a Linux ext2/ext3/ext4 file system
9. `resize2fs` - Resize ext2/ext3/ext4 file systems

These commands cover the basic and commonly used functionalities within each category for Linux systems.
--------------------------------------------
Linux Basic Commands: 1st set of Commands
##########################################
$  Prompt  --> user prompt

# prompt(root)  --> Administrator 

sudo -i  --> to switch root user

hostname Linux-Server  --> to change the server name

exec bash  --> Changes will be reflected

pwd --> present working directory

cal --> to check current month calendar 

cal 03 2020 --> to old calendar

date --> to check date & time

users --> to check the list of users

figlet L V M --> figlet command represent the in Big what we given like L V M or Name or anythink

who/whoami --> to check the present user

clear --> to clear the screen

1st set of Commands:
---------------------
Creating, removing, copying, moving files & directorys

cat > filename --> to create a file
ex: cat > file1 
    Hello-World
    ctrl+d

ls --> list files & directorys

cat >> file1 --> to append lines in the file
Linux Session
Multi-Cloud with Devops Batch
ctrl+d

cat file1 --> to read content in the file

touch file2 file3 file4 file5  ---> to create multiple files

touch xyz{1..100} --> to create multiple files

mkdir git --> to create directory

mkdir jenkins{1..100}  --> to create multiple directorys

cp file1 git --> to copy file in to directory

cd git --> to switch directory

cd .. --> to exit from the directory

mv file2 git  --> move file in to directory

rm file1 --> to delete the file

rmdir jenkins --> to delete the directory

rm -rf file2 --> to delete the file forcefully 

rm -rf git  --> to delete the directory forcefully

mv sourcedirectory destinationdirectory --> to rename directory

File editors:
-------------
1)vi --> visual display editor
2)vim --> visual display editor improved
  
vi is having 3 modes
--------------------

1)command mode: move cursor top to buttom and left to right:
----------------------------------------------------------
delete line                   dd
undo line                     u
copy                          yy
paste                          p
mv cursor word by word         w
mv cursor back word by word    b

2)insert/edit/append mode:
-------------------------
         i  -->to switch insert mode modify the content
         
3)extended command mode:
-----------------------
esc
:w --> to save the file
:q --> to quit the file without save

find (search)
---------------
1) find / -name filename
2) find / -name foldername
3) find / -name username
4) find / -name groupname

user management:
---------------

useradd/adduser --> to add/create user
passwd username --> to add passwd to user
vi /etc/sudoers --> to give primission to the user
su username   --> to switch user
exit  --> to exit from user

file permissions:
----------------
permissions are applied on 3 levels
1) Owner/user level
2) Group level
3)Other level
Access Modes are 3 types:

1) r  read
2) w  write
3) x excute

The permission string - ---(u) ---(g) ---(o) can be interpreted as follows: 
 
The first character (-) indicates that file is a regular file (not a directory or 
special file). 
The next three characters (---) represent the permissions for the user owner 
(user). Since all permissions are set to ---, the user owner has no permissions. 
The next three characters (---) represent the permissions for the group owner 
(user group). Similarly, all permissions are set to ---, meaning the group owner 
has no permissions. 
The last three characters (---) represent the permissions for other users. Once 
again, all permissions are set to ---, indicating that other users have no 
permissions.

-->ls
-->ls -l filename (it showcase the file with default permission)
-->chmod u=w,g=w,o=w filename (it will changes from default permission to write premission)

2 Absolute method:we use nubers in place of rwx

1) 4  read
2) 2  write
3) 1 execute
    421(u)421(g)421(o)
-->chmod 666(u+g+o) filename (it will changes from default permission to read&write premission)
