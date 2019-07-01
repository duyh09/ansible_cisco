from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
# config file for prefix-list or any kind of config
with open('prelist') as f:
    commands_list = f.read().splitlines()
# device ip file
with open('r5r6') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ("connecting to device" + str(devices))
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'cisco',
        'password': 'cisco'
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ("AUTH FAIL " + ip_address_of_device)
        continue
    except (NetMikoTimeoutException):
        print ("Time out " + ip_address_of_device)
        continue
    except (SSHException):
        print (" SSH ISSUE " + ip_address_of_device)
        continue


    output = net_connect.send_config_set(commands_list)
    print (output)
    output = net_connect.send_command('clear ip bgp * soft')
    print (output)
