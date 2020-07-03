#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:31:29 2020

@author: ejg
"""

import socket
import threading

def run_server(ip="0.0.0.0", port=9999,response="SERVER TEST"):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip,port))
    
    server.listen(5)
    print("Listening on ", ip, ":", port, sep="")
    while True:
        client, addr = server.accept()
        print("Connection from", addr[0], ":", addr[1], sep="")        
        handler_thread = threading.Thread(target=handle_request,
                                          args=(client,response,))
        handler_thread.start()
    
def handle_request(client, response):
    request = client.recv(1024)
    print("Received:", request)
    client.send(response)
    client.close()
    



if __name__ == "__main__":
    run_server() #defaults