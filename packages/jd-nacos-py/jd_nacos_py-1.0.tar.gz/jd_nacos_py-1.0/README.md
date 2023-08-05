# python-nacos-client
- nacosclient 包放置项目目录下
- 可按照microservice.yaml文件进行注册服务配置, 文件路径与包同级
- 当前包内microservice.yaml仅为样例
## 用法
```python
# 可参照init文件内入口使用
# ----logger 用法
# 当前为终端输出，项目下指定路径与输出格式即可输出到文件中

import logging
_format =logging.Formatter(
fmt='[%(asctime)s]-[%(name)s]-[line:%(lineno)d] -%(levelname)-4s: %(message)s',
datefmt='%Y-%m_%d %H:%M:%S',
)
_handler = logging.handlers.TimedRotatingFileHandler("/var/..")
_handler.setFormat(_format)
_handler.setLevel("INFO")

```
### 可用方法及api
- nacos 官网api皆可使用（继承式封装）
- nacos_client.init(instance) 传入注册服务实例即可开启注册，心跳
- nacos_client.get_client() 全局获取客户端实例
- nacos_client.get_random_provider(server_name) 权重ip，传参目标服务名
- nacos_client.load_balance_client_avr(server_name) 轮询ip，传参目标服务名
- nacos_client.add_regist(instance) 手动注册指定实例
- nacos_client.remove_ins(instance) 手动注销指定实例
- nacos_client.stop() 手动退出: 注销当前已注册的全部实例（多端口也算一个可用实例）
- 使用adapter_server 中Instance类实例化服务实例
- 可随项目退出自动注销当前实例：atexit模块使用