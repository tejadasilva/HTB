---
description: HTB Getting Started documentation
cover: >-
  https://images.unsplash.com/photo-1528605248644-14dd04022da1?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwxOTcwMjR8MHwxfHNlYXJjaHwxMHx8dGVhbSUyMG9mJTIwcGVvcGxlfGVufDB8fHx8MTY2MDMxNzQzNg&ixlib=rb-1.2.1&q=80
coverY: 0
---

# 👣 Nibbles - Web Footprinting



## Directory Enumeration

{% code fullWidth="false" %}
```
┌─[user@parrot]─[~/Downloads]
└──╼ $gobuster dir -u http://10.129.164.113/nibbleblog/ --wordlist /home/user/Tools/SecLists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.164.113/nibbleblog/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/user/Tools/SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 309]
/.hta                 (Status: 403) [Size: 304]
/.htpasswd            (Status: 403) [Size: 309]
/README               (Status: 200) [Size: 4628]
/admin                (Status: 301) [Size: 327] [--> http://10.129.164.113/nibbleblog/admin/]
/admin.php            (Status: 200) [Size: 1401]
/content              (Status: 301) [Size: 329] [--> http://10.129.164.113/nibbleblog/content/]
/index.php            (Status: 200) [Size: 2987]
/languages            (Status: 301) [Size: 331] [--> http://10.129.164.113/nibbleblog/languages/]
/plugins              (Status: 301) [Size: 329] [--> http://10.129.164.113/nibbleblog/plugins/]
/themes               (Status: 301) [Size: 328] [--> http://10.129.164.113/nibbleblog/themes/]
Progress: 4734 / 4735 (99.98%)
===============================================================
Finished
===============================================================

```
{% endcode %}

## Checking README page

```
┌─[user@parrot]─[~/Downloads]
└──╼ $curl http://10.129.128.122/nibbleblog/README
====== Nibbleblog ======
Version: v4.0.3
Codename: Coffee
Release date: 2014-04-01

Site: http://www.nibbleblog.com
Blog: http://blog.nibbleblog.com
Help & Support: http://forum.nibbleblog.com
Documentation: http://docs.nibbleblog.com

===== Social =====
* Twitter: http://twitter.com/nibbleblog
* Facebook: http://www.facebook.com/nibbleblog
* Google+: http://google.com/+nibbleblog

===== System Requirements =====
* PHP v5.2 or higher
* PHP module - DOM
* PHP module - SimpleXML
* PHP module - GD
* Directory “content” writable by Apache/PHP

Optionals requirements

* PHP module - Mcrypt

===== Installation guide =====
1- Download the last version from http://nibbleblog.com
2- Unzip the downloaded file
3- Upload all files to your hosting or local server via FTP, Shell, Cpanel, others.
4- With your browser, go to the URL of your web. Example: www.domain-name.com
```

<figure><img src=".gitbook/assets/2024-11-06 21_24_27-Parrot OS Security Edition [Running] - Oracle VirtualBox.png" alt=""><figcaption><p>Browsing content</p></figcaption></figure>

## Checking users.xml file

```
┌─[✗]─[user@parrot]─[~/Downloads]
└──╼ $curl -s http://10.129.128.122/nibbleblog/content/private/users.xml | xmllint --format -
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<users>
  <user username="admin">
    <id type="integer">0</id>
    <session_fail_count type="integer">1</session_fail_count>
    <session_date type="integer">1730949749</session_date>
  </user>
  <blacklist type="string" ip="10.10.10.1">
    <date type="integer">1512964659</date>
    <fail_count type="integer">1</fail_count>
  </blacklist>
  <blacklist type="string" ip="10.10.14.225">
    <date type="integer">1730949749</date>
    <fail_count type="integer">1</fail_count>
  </blacklist>
</users>

```

## Cheking config file

```
┌─[user@parrot]─[~/Downloads]
└──╼ $curl -s http://10.129.128.122/nibbleblog/content/private/config.xml | xmllint --format -
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<config>
  <name type="string">Nibbles</name>
  <slogan type="string">Yum yum</slogan>
  <footer type="string">Powered by Nibbleblog</footer>
  <advanced_post_options type="integer">0</advanced_post_options>
  <url type="string">http://10.10.10.134/nibbleblog/</url>
  <path type="string">/nibbleblog/</path>
  <items_rss type="integer">4</items_rss>
  <items_page type="integer">6</items_page>
  <language type="string">en_US</language>
  <timezone type="string">UTC</timezone>
  <timestamp_format type="string">%d %B, %Y</timestamp_format>
  <locale type="string">en_US</locale>
  <img_resize type="integer">1</img_resize>
  <img_resize_width type="integer">1000</img_resize_width>
  <img_resize_height type="integer">600</img_resize_height>
  <img_resize_quality type="integer">100</img_resize_quality>
  <img_resize_option type="string">auto</img_resize_option>
  <img_thumbnail type="integer">1</img_thumbnail>
  <img_thumbnail_width type="integer">190</img_thumbnail_width>
  <img_thumbnail_height type="integer">190</img_thumbnail_height>
  <img_thumbnail_quality type="integer">100</img_thumbnail_quality>
  <img_thumbnail_option type="string">landscape</img_thumbnail_option>
  <theme type="string">simpler</theme>
  <notification_comments type="integer">1</notification_comments>
  <notification_session_fail type="integer">0</notification_session_fail>
  <notification_session_start type="integer">0</notification_session_start>
  <notification_email_to type="string">admin@nibbles.com</notification_email_to>
  <notification_email_from type="string">noreply@10.10.10.134</notification_email_from>
  <seo_site_title type="string">Nibbles - Yum yum</seo_site_title>
  <seo_site_description type="string"/>
  <seo_keywords type="string"/>
  <seo_robots type="string"/>
  <seo_google_code type="string"/>
  <seo_bing_code type="string"/>
  <seo_author type="string"/>
  <friendly_urls type="integer">0</friendly_urls>
  <default_homepage type="integer">0</default_homepage>
</config>


```

## Directory brute-forcing against root of the web application

```
┌─[user@parrot]─[~/Downloads]
└──╼ $gobuster dir -u http://10.129.128.122/ --wordlist /home/user/Tools/SecLists/Discovery/Web-Content/common.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.128.122/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/user/Tools/SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 293]
/.htaccess            (Status: 403) [Size: 298]
/.htpasswd            (Status: 403) [Size: 298]
/index.html           (Status: 200) [Size: 93]
/server-status        (Status: 403) [Size: 302]
Progress: 4734 / 4735 (99.98%)
===============================================================
Finished
===============================================================

```

We see "nibbles" word on configuration files, so we tried with valid user name "admin", so we have a successful login attempt using nibbles as password:

<figure><img src=".gitbook/assets/2024-11-06 21_59_30-Parrot OS Security Edition [Running] - Oracle VirtualBox.png" alt=""><figcaption></figcaption></figure>

