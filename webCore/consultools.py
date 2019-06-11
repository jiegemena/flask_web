import config
import consul

def register():
    server_name = config.CONSUL_CLIENT_NAME
    ip = config.CONSUL_CLIENT_HOST
    port= config.CONSUL_CLIENT_PORT
    c = consul.Consul(host=config.CONSUL_HOST,port=config.CONSUL_PORT) # 连接consul 服务器，默认是127.0.0.1，可用host参数指定host
    print(f"开始注册服务{server_name}")
    check = consul.Check.tcp(ip, port, "10s") # 健康检查的ip，端口，检查时间
    c.agent.service.register(server_name, f"{server_name}-{ip}-{port}",address=ip, port=port, check=check) # 注册服务部分
    print(f"注册服务{server_name}成功")

def unregister():
    server_name = config.CONSUL_CLIENT_NAME
    ip = config.CONSUL_CLIENT_HOST
    port= config.CONSUL_CLIENT_PORT
    c = consul.Consul(host=config.CONSUL_HOST,port=config.CONSUL_PORT)
    print(f"开始退出服务{server_name}")
    c.agent.service.deregister(f'{server_name}-{ip}-{port}')