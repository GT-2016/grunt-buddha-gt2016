# coding:utf-8
'''
Created on 2018年5月23日

@author: Administrator
'''
import logging,time,os
from logging.handlers import RotatingFileHandler

class LogPrint(object):
    '''
    # 1. 控制台打印log
    # 2. 可控制日志文件显示大小和个数
    # 3. 通过JSON或YAML文件配置logging模块 import json/yaml
    '''

    def __init__(self, tilte_name):
        '''
        Constructor
        '''
        title = u'日志输出测试'
        day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
        filepath = os.getcwd()
        file = os.path.join(filepath, day+'.log')
#         file = os.path.join(filepath, "logging.log")
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.Logger(tilte_name)      # title
        # 不限制文件保存
#         self.logfile = logging.FileHandler(file)
#         self.logfile.setLevel(logging.INFO)
#         self.logfile.setFormatter(self.formater)
#         self.logger.addHandler(self.logfile)
        # control输出到屏幕
        self.control = logging.StreamHandler()      
        self.control.setLevel(logging.INFO)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.control)
        #定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
        self.rHandler = RotatingFileHandler(file,maxBytes = 512*1024,backupCount = 3)
        self.rHandler.setLevel(logging.INFO)
        self.rHandler.setFormatter(self.formater)
        self.logger.addHandler(self.rHandler)
        
    def debug_log(self, msg):
        print 'debug'
        records = {'john': 55, 'tom': 66}
        self.logger.debug('Records: %s', records)
        self.logger.debug(msg)
    
    def info_log(self, msg):
        self.logger.info(msg)
        
    def warn_log(self, msg):
        self.logger.warn(msg)
        
    def error_log(self, msg):
        self.logger.error(msg)
        
if __name__ == "__main__":
    log = LogPrint('logger.py')
# #     log.warn_log("input:name:%s password:%s,passwordque:%s,shoujihao:%s,youxiang:%s ,assert:%s"%(i,"1234556","self.passwordque","eeewr","self.youxiang","self.assert_vale"))
    log.debug_log("msg1111111111111111")
    
    print 'logging'