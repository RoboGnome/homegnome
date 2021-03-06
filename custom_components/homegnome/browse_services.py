import argparse
import logging
from time import sleep
from typing import cast

from zeroconf import DNSAddress, IPVersion, ServiceBrowser, ServiceStateChange, Zeroconf, ZeroconfServiceTypes


class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info: 
            #print("Service %s added, service info: %s" % (name, info))
            print("Service %s added, IP address: %s" % (name, info.parsed_addresses()[0]))


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_coap._udp.local.", listener)
try:
    sleep(2)
finally:
    zeroconf.close()