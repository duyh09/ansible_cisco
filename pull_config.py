import datetime
import os
import re
import threading

import netmiko
import yaml

with open('inter_config') as f:
    line = f.read().splitlines()


def pull_configs(dev):
    '''
    write running config to file named {hostname}
    '''
    dev_ssh = netmiko.ConnectHandler(**dev)
    dev_ssh.enable()
    hostname = dev_ssh.find_prompt()
    dev_conf = dev_ssh.send_command('show run')
    output= net_connect.send_config_set(lines)




    device_dicts = []
    for dev in TOPOLOGY['device_list'].values():
        dd = {
            'device_type': 'cisco_ios',
            'username': TOPOLOGY['credentials']['username'],
            'password': TOPOLOGY['credentials']['password'],
            'ip': dev,
	    
            }
        device_dicts.append(dd)

    thread_list = [threading.Thread(target=pull_configs, args=(dev,))
                   for dev in device_dicts]

    for dt in thread_list:
        dt.start()
    for dt in thread_list:
        dt.join()
