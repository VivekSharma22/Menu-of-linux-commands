import subprocess as sp
import os
os.system('tput setaf 2')
print("-----------Welcome to my menu------------\n\n")
while True:
    os.system("tput setef 3")
    print('''         1. GENERAL
           2. FILES/FOLDERS
           3. STORAGE/RAM/CPU
           4. HADOOP
           5. DOCKER
           6. NETWORKING
           7. EXIT''')
    inp=input("Enter your choice--")

    
#general    
    if inp=='1':
        os.system("tput setaf 4")
        print("""               1. run date command
                 2. run cal command
                 3. run ifconfig command
                 4. view current user of this os
                 5. know your present working directory
                 6. know your terminal name
                 7. know your type of shell
                 8. view text on clipboard
                 9. Query regarding a software
                 10. know which software provides you a particular command
                 11. see if any process is running in background
                 12. locate the executable files of a command
                 13. Stop a process 
                 14. find the time took by a command to execute
                 15. run history command
                 16. download a file from internet
                 17. make alias of a command\n""")
                 
        inp1=input("Enter your choice--")
        if inp1=='1':
            print(sp.getoutput("date"))
        elif inp1=='2':
            print(sp.getoutput("cal"))
        elif inp1=='3':
            print(sp.getoutput("ifconfig"))
        elif inp1=='4':
            print(sp.getoutput("whoami"))
        elif inp1=='5':
            print(sp.getoutput("pwd"))
        elif inp1=='6':
            print(sp.getoutput("tty"))
        elif inp1=='7':
            print(sp.getoutput("echo $SHELL"))
        elif inp1=='8':
            print(sp.getoutput("xclip -o"))
        elif inp1=='9':
            x=input('Enter the name of software.. ')
            y="rpm -q "+ x
            print(sp.getoutput(y))
        elif inp1=='10':
            x=input('Enter the command..')
            y="yum whatprovides "+ x
            print(sp.getoutput(y))
        elif inp1=='11':
            print(sp.getoutput("jobs"))
        elif inp1=="12":
            x=input("enter the command..")
            y="which " + x
            print(sp.getoutput(y))
        elif inp1=='13':
            x=input("Enter the id of process you want to stop..")
            y="kill "+x
            print(sp.getoutput(y))
        elif inp1=="14":
            x=input('Enter the command..')
            y='time '+x
            print(sp.getoutput(y))
        elif inp1=='15':
            print(sp.getoutput("history"))
        elif inp1=='16':
            x=input("Enter the URL to download file..")
            y='wget ' +x
            print(sp.getoutput(y))
        elif inp1=='17':
            x=input('Enter command of which you like alias..')
            a=input('Enter the short name..')
            y='alias ' +a+'='+"'"+x+"'"
            
            print(sp.getoutput(y))
        else:
            print("invalid choice")

#file/folder    

        
    elif inp=='2':
        os.system("tput setaf 5")
        print('''           1. List all files and folder in present directoy
            2. check present working directory
            3. view size of a file
            4. make a folder in current directory
            5. make a file in current directory
            6. delete a file
            7. delete a folder''')
        i2=input("Enter your choice--")
        if i2=='1':
            print(sp.getoutput('ls'))
    
        elif i2=='2':
            print(sp.getoutput('pwd'))

        elif i2=='3':
            x=input('Enter name of file')
            y='ls -lh ' +x
            print(sp.getoutput(y))
        elif i2=='4':
            x=input("Enter name of folder you want to make..")
            y='mkdir ' + x
            print(sp.getoutput(y))
        elif i2=='5':
            x=input('Enter the name of file you want to make..' )
            y='touch ' + x
            print(sp.getoutput(y))
        elif i2=='6':
            x=input('Enter the name of file you want to delete..' )
            y='rm ' + x
            print(sp.getoutput(y))
        elif i2=='7':
            x=input('Enter the name of folder you want to delete..' )
            y='rm -rf ' + x
            print(sp.getoutput(y))

#storage/ram/cpu
    
    elif inp=='3':
        os.system("tput setaf 9")
        print('''           1. view status of RAM
            2. view main storage folders and where they are mounted
            3. view information about CPU
            4. view all the storage devices
            5. view all working port in our system
            6. see all the processes running on our system
            7. create partition, format if and mount it
            8. start/stop/view status/eanble a service 
            ''')
        i3=input('Enter your choice--')
        if i3=='1':
            print(sp.getoutput('free -m'))
        elif i3=='2':
             print(sp.getoutput('df -h'))
        elif i3=='3':
             print(sp.getoutput('lscpu'))
        elif i3=='4':
             print(sp.getoutput('fdisk -l'))
        elif i3=='5':
             print(sp.getoutput('netstat -tnpl'))
        elif i3=='6':
             print(sp.getoutput('ps -aux'))
        elif i3=='7':
            x=input('Enter the name of drive')
            a=input('Enter hte name of folder on which you like to mount your drive')
            y='echo -e "n\n\n\n\n\nw\n" | fdisk {}'.format(x)
            print(sp.getoutput(y))
            os.system('udevadm settle')
            z='mkfs.ext4 {}1'.format(x)
            print(sp.getoutput(z))
            os.system("mkdir /{}".format(a))
            b='mount /{}1 /{}'.format(x,a)
            os.system(b)
        elif i3=='8':
            x=input('Enter the name of service')
            print(""" What would youlike to do with sevice {}--
        1. See status of service
        2. start the sevice 
        3. stop the service
        4. enable service """.format(x))
            ii3=input("Enter your choice--")
            if ii3=='1':
                print(sp.getoutput('systemctl status {}'.format(x)))
            elif ii3=='2':
                print(sp.getoutput('systemctl start {}'.format(x)))                
            elif ii3=='3':
                print(sp.getoutput('systemctl stop {}'.format(x)))
            elif ii3=='4':

                print(sp.getoutput('systemctl enable {}'.format(x)))   
            else:
                print("OOOppss!! wrong choice")

#hadoop
    elif inp=='4':
	
        os.system("tput setaf 3")
        print("\t\t\t Welcome to my Hadoop Menu!!!")

        os.system("tput setaf 6")
        def hadoop_menu() :
                print("\t\t\t-------------")
                print("\n\t\t\t**************")
                print("press 1: To check the Hadoop is present or not")
                print("press 2: To check the Java  is present or not")
                print("press 3: To install the java")
                print("press 4: To install the Hadoop")	
                print("press 5: To check this system is master | slave | normal system")
                print("press 6: To start namenode")
                print("press 7: To see port numbers")
                print("press 8: To start datanode")
                print("press 9: To check datanode is set up or not")
                print("press 10: To check how many datanodes are connected & how much storage they contributed")
                print("press 11: To check hadoop storage list")
                print("press 12: To upload a file from client")
                print("press 13: To read a file from hadoop cluster")
                print("press 14: To delete a file from hadoop cluster ")
                print("press 15: To change block size of file")
                print("press 16: To stop namenode")
                print("press 17: To stop datanode")
                print("press 0: To exit")
        hadoop_menu()
        ch= int(input("enter your choice:"))
        while ch !=0 :
                if(ch)==1:
                        os.system("rpm -q hadoop")
                elif(ch)==2:
                        os.system("java -version")
                elif(ch)==3:
                        os.system("rpm -i jdk-8u171-linux-x64.rpm")
                elif(ch)==4:
                        os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
                elif(ch)==5:
                        os.system("jps")
                elif(ch)==6:
                        os.system("hadoop-daemon.sh start namenode")
                elif(ch)==7:
                        os.system("netstat -tnlp")
                elif(ch)==8:
                        dnip=input("enter your datanode ip:")
                        os.system("ssh {} hadoop-daemon.sh start datanode".format(dnip))
                elif(ch)==9:
                        dnip=input("enter your datanode ip:")
                        os.system("ssh {} jps".format(dnip))
                elif(ch)==10:
                        os.system("hadoop dfsadmin -report")	
                elif(ch)==11:
                        os.system("hadoop fs -ls /")
                elif(ch)==12:
                        ip=input("enter your client ip:")
                        fn=input("enter your file name:")
                        os.system("ssh {} hadoop fs -put {} /".format(ip,fn))	
                elif(ch)==13:
                        fn1=input("enter your file name:")
                        os.system("hadoop fs -cat /{}".format(fn1))
                elif(ch)==14:
                        fn2=input("enter your file name:")
                        os.system("hadoop fs -rm /{}".format(fn2))
                elif(ch)==15:
                        ip=input("enter your client ip:")
                        fn3=input("enter your file name:")
                        bs=int(input("enter your block size:"))
                        os.system("ssh {} hadoop fs -D dfs.block.size={} -put {} /".format(ip,fn3,bs))
                elif(ch)==16:
                        os.system("hadoop-daemon.sh stop namenode")
                elif(ch)==17:
                        dnip=input("enter your datanode ip:")
                        os.system("ssh {} hadoop-daemon.sh stop datanode".format(dnip))
                elif(ch)==0:
                    exit()
                else:
                        print("invalid option")
		

                print()
                hadoop_menu()
                ch=int(input("enter your choice:"))        






#docker
    elif inp=='5':
        os.system("tput setaf 3")
        print("\t\t\t Welcome to my Docker Menu!!!")

        os.system("tput setaf 6")
        print("\t\t\t-------------")

        print("\n\t\t\t**************")

        def docker_menu():
            print("""\tPress 1: To check Docker installed or not\n\tpress 2: To start Docker service\n\tpress 3: To Show all the Info about Docker\n\tpress 4: Pull OS Images\n\tpress 5: Delete/stop/start a container\n\tpress 6: Configure httpd server inside a container""")
        docker_menu()
        ch = input("Enter your choice:")
        if int(ch) == 1:
    	    os.system("rpm -q docker-ce")

        elif int(ch) == 2:
            os.system("systemctl start docker")

        elif int(ch) == 3:
            os.system("docker info")
        elif int(ch) == 4:
            osname= input("Which os Image you want to pull:")
            print(osname)
            os.system("docker pull {}".format(osname))
        elif int(ch) == 5:
            choice = input("""Enter your choice 
    press 1- To start container 
    press 2- To stop  container 
    press 3- To Delete container
    press 4- To Delete all containers""")
            if int(choice) ==1:
                container = input("Enter container Name/ID:")
                imagename =  input("Enter Image name:")
                os.system("docker run --name {} {}".format(container,imagename))
            elif int(choice) ==2:
                container = input("Enter container Name/ID:")
                os.system("docker stop {}".format(container))
            elif int(choice) ==3:
                container = input("Enter container Name/ID:")
                os.system("docker rm {}".format(container))
            elif int(choice) ==4:
                os.system("docker rm 'docker ps -a -q'")
            else:
                print("Invalid choice")         
        elif int(ch) == 6:
            osname = input("Enter the container name in which you want to configure webserver:")
            os.system("docker exec {} yum install httpd -y".format(osname))
            os.system("tput setaf 2")
            os.system("docker exec {} /usr/sbin/httpd".format(osname))

    
#networking

    
    elif inp=='6':
        os.system("tput setaf 8")
        print('''           1. get the public ip of a URL
            2. ping any ip (4 times) 
            3. view router and their gateway ''')

        i6=input('enter your choise..')
        if i6=='1':
            x= input("Enter the URL..")
            y="nslookup "+x
            print(sp.getoutput(y))
        elif i6=='2':
            x=input("enter the ip or URL you like to ping..")
            y="ping -c 4 "+ x
            print(sp.getoutput(y))
        elif i6=='3':
            print(sp.getoutput('route -n'))

    elif inp=='7':
        exit()
        
            
    
    else:
        print("Invalid choice..........")

        


