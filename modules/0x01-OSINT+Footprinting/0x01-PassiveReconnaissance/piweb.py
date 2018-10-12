#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework

from __future__ import print_function
import requests
import time
from time import sleep
from core.Core.colors import *

def piweb(web):

    web = web.split('//')
    print(R+'\n   =====================')
    print(R+'    P I N G   C H E C K ')
    print(R+'   =====================\n')
    time.sleep(0.4)
    print('' + GR + color.BOLD + ' [!] Pinging website using external APi...')
    time.sleep(0.4)
    print(""+ GR + color.BOLD + " [~] Result: "+ color.END)
    domains = [web]
    for dom in domains:
        text = requests.get('http://api.hackertarget.com/nping/?q=' + dom).text
        nping = str(text)
        if 'error' not in nping:
            print(G+ nping)
        else:
            print(R+' [-] Outbound Query Exception!')
            sleep(0.8)
