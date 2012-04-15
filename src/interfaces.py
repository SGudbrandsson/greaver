# -*- Mode: Python; Coding: utf-8; tab-width: 4 -*-
#
# Greaver
# Copyright (C) Sigurdur Gudbrandsson 2012 <sigurdur@sigginet.info>
#Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name ``Sigurdur Gudbrandsson'' nor the name of any other
#    contributor may be used to endorse or promote products derived
#    from this software without specific prior written permission.
# 
# Greaver IS PROVIDED BY Sigurdur Gudbrandsson ``AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL Sigurdur Gudbrandsson OR ANY OTHER CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import array
import struct
import socket
import fcntl
import string

SIOCGIFCONF = 0x8912  #define SIOCGIFCONF
BYTES = 4096          # Simply define the byte size

# get_iface_list function definition 
# this function will return array of all 'up' interfaces 
def get_iface_list():
    # create the socket object to get the interface list
    sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # prepare the struct variable
    names = array.array('B', '\0' * BYTES)
    
    # the trick is to get the list from ioctl
    bytelen = struct.unpack('iL', fcntl.ioctl(sck.fileno(), SIOCGIFCONF, struct.pack('iL', BYTES, names.buffer_info()[0])))[0]

    # convert it to string
    namestr = names.tostring()

    # return the interfaces as array
    return [namestr[i:i+32].split('\0', 1)[0] for i in range(0, bytelen, 32)]

# get_filtered_iface_list function definition
# This function will return an array of all "filtered" interfaces that are 'up'.
# Useful for getting a current list of WLAN or MON interfaces.
# Also useful for checking that a interface is actually up before assigning work to it.
def get_filtered_iface_list(ifacename = "wlan"):
    # Get the interfaces
    interfaces = get_iface_list()

    # Filter the iface interfaces
    for interface in interfaces:
        if interface.find(ifacename) != -1:
            filtinterfaces = [interface]

    # Return the list if there are any, -1 if there are none.
    if len(filtinterfaces) > 0:
        return filtinterfaces
    else:
        return -1