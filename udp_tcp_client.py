#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:46:38 2020

@author: ejg
"""

import socket
import sys

def main(host,port,data,sock_type=socket.SOCK_STREAM):
    '''
    Sends packets (TCP/UDP) and returns response from server.
    
    Does not handle bad connection attempts, slow response times or 
    servers that send data first and expect response.
    
    Inputs
        sock_type: Type of socket. (defaults to socket.SOCK_STREAM)
        host: the host server (127.0.0.1, www.cnn.com etc)
        port: target port
        data: data to be sent        
            
    Returns
        data from server
    
    '''
    client = socket.socket(socket.AF_INET,sock_type) #default paramaters for tcp
    
    if sock_type == socket.SOCK_STREAM:
        client.connect((host,port))
        client.send(data)
        return client.recv(4096)
    
    elif sock_type == socket.SOCK_DGRAM:
        client.sendto(data,(host,port))
        received,_ = client.recvfrom(4096)
        return received
    
    
if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] not in ("-t","-u"):
        print("Usage: {} <-t or -u> <host> <port> <data>".format(sys.argv[0]))
        sys.exit(1)    
    
    host,port,data=sys.argv[2:]
    port = int(port)
    if sys.argv[1] == "-t":
        sock = socket.SOCK_STREAM
    elif sys.argv[1] == "-u":
        sock = socket.SOCK_DGRAM
    
    main(host,port,data,sock_type=socket.SOCK_STREAM)