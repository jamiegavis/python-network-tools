#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 08:46:38 2020

@author: jg
"""

import socket
import sys

def connect(host,port,data,sock_type=socket.SOCK_STREAM):
    '''
    Sends packets (TCP/UDP) and returns response from server.
    
    Does not handle bad connection attempts or slow response times.
    
    Inputs
        sock_type: Type of socket. (defaults to socket.SOCK_STREAM)
        host: the host server (127.0.0.1, www.cnn.com etc)
        port: target port
        data: data to be sent (if None: TCP will connect but not send data)        
            
    Returns
        data from server or 0 if TCP error
    
    '''
    client = socket.socket(socket.AF_INET,sock_type) #default paramaters for tcp
    if sock_type == socket.SOCK_STREAM:
        try:
            client.connect((host,port))
            if data:
                client.send(data)
            resp_len,response = 1,""
            while resp_len:
                client_data = client.recv(4096)
                resp_len = len(client_data)
                response += client_data
                if resp_len < 4096:
                    break    
            return response
        except Exception as e:
            print("Exception: ",e ,"-- Exiting.")
            client.close()
            return 0
    
    elif sock_type == socket.SOCK_DGRAM:
        client.sendto(data,(host,port))
        received,_ = client.recvfrom(4096) #resp size limited to 4096
        return received
    
    
if __name__ == "__main__":
    if len(sys.argv) != 5 or sys.argv[1] not in ("-t","-u"):
        print("Usage: {} <-t or -u> <host> <port> <data>".format(sys.argv[0]))
        sys.exit(1)    
    
    host,port,data=sys.argv[2:]
    port = int(port)
    data = data.encode('utf_8')
    if sys.argv[1] == "-t":
        sock = socket.SOCK_STREAM
    elif sys.argv[1] == "-u":
        sock = socket.SOCK_DGRAM
    
    connect(host,port,data,sock_type=socket.SOCK_STREAM)
