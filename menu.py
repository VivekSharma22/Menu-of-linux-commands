import subprocess as sp
import os
os.system('tput setef 2')
print("-----------Welcome to my menu------------\n\n")
while True:
    print('''            1. GENERAL
           2. FILES/FOLDERS
           3. STORAGE/RAM/CPU
           4. HADOOP
           5. DOCKER
           6. NETWORKING
           7. EXIT''')
    inp=input("Enter your choice--")

    os.system('tput setaf 8')
#general    
    if inp=='1':
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
 #   os.system('tput setaf 2')
        
    elif inp=='2':
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
    #os.system('tput setaf 4')
    elif inp=='3':
        print('''           1. view status of RAM
            2. view main storage folders and where they are mounted
            3. view information about CPU
            4. view all the storage devices
            5. view all working port in our system
            6. see all the processes running on our system
            7. create partition, format and mount it
            
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
 #hadoop
    elif inp=='4':
        

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

    #os.system('tput setaf 3')
    elif inp=='6':
        print('''           1. get the public ip of a URL
            2. ping any ip (4 times) 
            3. see if any process is running in background''')

        i6=input('enter your choise..')
        if i6=='1':
            x= input("Enter the URL..")
            y="nslookup "+x
            print(sp.getoutput(y))
        elif i6=='2':
            x=input("enter the ip or URL you like to ping..")
            y="ping -c 4 "+ x
            print(sp.getoutput(y))
        #elif i6=='3':
            
    elif inp=='7':
        exit()
    
    else:
        print("Invalid choice..........")

        


