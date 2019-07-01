from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

# this where ip of the device is located in a file called ios_device
with open('ios_device') as f:
    devices_list = f.read().splitlines()
# telling netmiko to where device is located
for devices in devices_list:
    print ("connecting to device " + str(devices))
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



    output = net_connect.send_command('wr')
    print (output)
    output = net_connect.send_command('show ip bgp ipv4 unicast')
    print (output)
    output = net_connect.send_command('show run')
    print (output)
