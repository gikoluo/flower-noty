###################
# Celery Settings #
###################




#basic_auth=username:passworrd,user2:pwd2

# address 通过给定的地址运行http服务
# auth 使谷歌的OpenID认证。
# auto_refresh 自动刷新控制面板(默认，auto_refresh=True)
# basic_auth 使用HTTP基础认证，basic_auth是`:分隔的值`username:passworrd,更多信息查看:ref:basic-auth.
# broker_api Flower使用 RabbitMQ Managment Plugin 获取队列信息. 默认managment plugin不可用
# certfile SSL证书文件的路径
# conf
# db 数据库文件的使用，如果持久模式开启的话(by default, db=flower)
# debug 使用调试模式 (by default, debug=False)
debug = True
# enable_events 定期启用 Celery events通过`enable_events`命令（默认,`enable_event=True`）
# format_task 修改默认的task格式
# inspect_timeout 设置worker检查超时（默认，inspect_timeout=10000 毫米）
# keyfile SSL key文件路径
# max_tasks 内存中保留最大的task数目（默认，max_tasks=10000）
# natural_time 显示相对于时间的刷新时间，（默认`natural_time=True`）
# persistent 启用持久模式，
# port 设置HTTP服务端口，默认`port=5555`
port = 5555
# xheaders 启用X-Real-Ip 和 X-Scheme headers，（默认，xheaders=False）
# tasks_columns 指定用逗号分隔的列清单在/tasks/页面