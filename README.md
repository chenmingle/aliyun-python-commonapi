# aliyun-python-commonapi



## 下面主要实现一个简单的阿里云解析操作功能


### 首先在主机上安装aliyun sdk库

```
pip install aliyun-python-sdk-alidns
```

### 在阿里云上申请AccessKey
* 建议使用子用户AccessKey
* 然后按步骤走会生成AccessKeyId与AccessKeySecret（请自己保管好！）

### 脚本的执行
```
python aliyun-python-commonapi.py
```
### 使用例子：
* 查询有哪些二级域名
	###### list_domain()
* 查询二级域名有哪些解析
	###### list_dns_record('test.xin')
* 修改域名解析
	###### edit_dns_record('test.xin', 'test', 'test_ok', 'A', '121.20.122.103')
* 增加域名解析
	###### add_dns_record('test.xin', 'test', 'A', '121.20.122.103')
* 删除域名解析
	###### delete_dns_record('test.xin','test_ok')
* 暂停或启动域名解析
	###### set_dns_record('test.xin', 'test_ok', 'DISABLE'/'ENABLE')



