#!/usr/bin/python
 
from itertools import product
from pwn import *
import string, pdb, signal, sys, time, requests, urllib3, re
 
def def_handler(sig, frame):
    print("\n\n[!] Saliendo... \n")
    sys.exit(1)
 
# Ctrl+C
signal.signal(signal.SIGINT, def_handler)
 
 
# Calculate G3
def calc_g3():
 
    p1 = product(string.ascii_uppercase, repeat=2)
    p1 = [ "".join(i) for i in p1]
 
    uniques = {}
 
    for i in p1:
        for j in range (0,10):
            cadena = f'XP{i}{j}'
            value = sum(bytearray(cadena.encode()))
 
            uniques[value]= cadena
 
    return uniques.values()
 
# Checksum
 
def calc_cs(key) -> int:
    gs = key.split('-')[:-1]
    return sum([sum(bytearray(g.encode())) for g in gs])
 
def keyGen():
 
    values = calc_g3()
 
    total_keys = []
 
    for key in values:
        key = f"KEY67-AYBZ0-{key}-GAMC7-"
        cs=calc_cs(key)
 
        final_key = key + str(cs)
        total_keys.append(final_key)
    
    return total_keys
 
def tryKey(keys):
 
    login_url = "https://earlyaccess.htb/login"
    key_url = "https://earlyaccess.htb/key"
    key_add_url = "https://earlyaccess.htb/key/add"
 
    urllib3.disable_warnings()
    s = requests.session()
    s.verify =  False
 
    r = s.get(login_url)
 
    token = re.findall(r'name="_token" value="(.*?)"', r.text)[0]
 
    data_post = {
        '_token': token,
        'email': 'miguel@gmail.com',
        'password': 'usuario123'
    }
 
    r = s.post(login_url, data=data_post)
    r = s.get(key_url)
 
    p1= log.progress("Fuerza bruta")
    p1.status("Iniciando proceso de fuerza bruta")
 
    time.sleep(2)
 
    counter = 1
 
    for key in keys:
 
        p1.status("Probando con la key %s [%d/60]" %(key, counter))
 
        token = re.findall(r'name="_token" value="(.*?)"', r.text)[0]
 
        post_data = {
            '_token': token,
            'key': key
        }
 
        r = s.post(key_add_url, data=post_data)
 
        if "Game-key is invalid!" not in r.text:
            p1.success("La KEY %s es valida y ha sido registrada" %key)
            sys.exit(0)
        
        time.sleep(2)
 
        counter += 1
 
if __name__ == '__main__':
 
    keys = keyGen()
 
    tryKey(keys)
