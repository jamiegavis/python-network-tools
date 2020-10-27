#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 20:47:09 2020

@author: ejg
"""

import socket
import sys
import threading
import subprocess

import tcp_server
import udp_tcp_client

def main(listen = True, target ="0.0.0.0", port=9999):
    '''
    '''
    if listen:
        tcp_server.run_server(target,port,run_cmd)
        
    elif not listen and target and port:
        buffer = sys.stdin.read() #blocks -- Ctrl+D bypasses
        client_sender(target,port,buffer)
    
    
def run_console_cmd():
    return ""


def client_sender(target,port,content):
    '''
    '''
    initial = True
    while content or initial:   
        initial = False
        response = udp_tcp_client.connect(target,port,content,socket.SOCK_STREAM)
        if not response: 
            print("No response from ",target)
            break #
        print(response)
        content = input("Reply: ").strip()
        if content: 
            content += "\n"


if __name__ == "__main__":
    #Parse Console Commands
    main()