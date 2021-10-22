import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC adress")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC adress")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    if not options.interface:
        parser.error("[-] Please specify a new MAC, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for" + interface + " to " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", ifconfig_result)

        if mac_address_search_result:
            return mac_address_search_result
        else:
            print("[-] Could not read MAC address")

options = get_args()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + current_mac)
#change_mac(options.interface, options.new_mac)




