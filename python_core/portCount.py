#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''端口扫描器
    TCP端口扫描一般分为以下几种类型：
    TCP connect扫描：也称为全连接扫描，这种方式直接连接到目标端口，完成了TCP三次握手的过程，这种方式扫描结果比较准确，但速度比较慢而且可轻易被目标系统检测到。
    TCP SYN扫描：也称为半开放扫描，这种方式将发送一个SYN包，启动一个TCP会话，并等待目标响应数据包。如果收到的是一个RST包，则表明端口是关闭的，而如果收到的是一个SYN/ACK包，则表示相应的端口是打开的。
    Tcp FIN扫描：这种方式发送一个表示拆除一个活动的TCP连接的FIN包，让对方关闭连接。如果收到了一个RST包，则表明相应的端口是关闭的。
    TCP XMAS扫描：这种方式通过发送PSH、FIN、URG、和TCP标志位被设为1的数据包。如果收到了一个RST包，则表明相应的端口是关闭的。
'''
'''
    问题：统计开放的端口数时是从上一个值开始的
'''
from socket import *
import threading
import argparse

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        # lock.acquire()
        openNum += 1
        print('[+] %d open' % port)
        # lock.release()
        s.close()
    except:
        pass
def main():
    # p = argparse.ArgumentParser(description='Port scanner!.')
    # p.add_argument('-H', dest='hosts', type=str)
    # args = p.parse_args()
    # hostList = args.hosts.split(',')
    # setdefaulttimeout(1)
    hostList = ['192.168.90.177','192.168.90.176']
    for host in hostList:
        print('Scanning the host:%s......' % (host))
        for p in range(1,1024):
            t = threading.Thread(target=portScanner,args=(host,p))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print('[*] The host:%s scan is complete!' % (host))
        print('[*] A total of %d open port ' % (openNum))

if __name__ == '__main__':
    main()