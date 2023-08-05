#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 3:42 下午
# @Author  : lijiarui
# @Email   : lijiarui15@jd.com
# @Site    : 
# @File    : adapter_server.py
# @Software: PyCharm
import os
import yaml
from net_utils import get_host_ip
from py_nacos_client.logger import logger
# 当前文件路径
pro_dir = os.path.split(os.path.realpath(__file__))[0]


father_path=os.path.abspath(os.path.dirname(pro_dir)+os.path.sep+".")
NacosLibYamlPath = os.path.realpath(os.path.join(pro_dir, "microservice.yaml"))

DEFAULT_GROUP = "DEFAULT_GROUP"
NAMESPACE = "PUBLIC"


class Adapter:
      def __init__(self, obj, adapted_methods):
          self.obj = obj
          self.__dict__.update(adapted_methods)
      def __str__(self):
          return str(self.obj)



class Instance:
    """
    服务实例
    """
    def __init__(self, name, ip = get_host_ip(), port = "8000", group_name = DEFAULT_GROUP, name_space = NAMESPACE, **kwargs):
        self.service_name = name
        self.ip = ip
        self.port = port
        self.group_name = group_name
        self.name_space = name_space
        self.port_list = []
        if kwargs.get("port_list"):
            self.port_list.extend(kwargs["port_list"])

    @property
    def has_more_port(self):
        return len(self.port_list) > 1

    def __call__(self, *args, **kwargs):
        return self.service_name


def load_active_content(path=''):
    """
    加载yaml文件内容
    :return:
    """
    with open(NacosLibYamlPath if not path else path) as f:
        server_config = yaml.load(f.read(), Loader=yaml.FullLoader)
    #kwargs can be use to customsize what you want
    SERVER_NAME = server_config.pop("SERVER_NAME")
    IP = server_config.pop("IP") if server_config.pop("IP") else get_host_ip()
    PORT = server_config.pop("PORT")
    if server_config:
        for k in server_config:
            server_config[k.lower()] = server_config.pop(k)
    new_instance = Instance(SERVER_NAME, IP, PORT, **server_config)
    return new_instance
