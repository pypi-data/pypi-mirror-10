#python-thrift-pool

#base on：
* python2.7
* thrift 0.9.2 thrift lib

#change 2014-12-05 :
* dependency thrift 0.9.2 while using thrift-TMultiplexedProtocol

#usage

##install 
	pip install thriftpl

## using
look at tests/test.py
<pre>
<code>
# -*- coding: utf-8 -*-

import os,sys

from thriftpl.client import ThriftClientPool,ThriftClientConfig,HostAndPort,ThriftPoolConfig
from test import TestService

address = HostAndPort("127.0.0.1",9090)
poolConfig = ThriftPoolConfig(minPoolSize=1,maxPoolSize=10,maxWait=500)
clientConfig = ThriftClientConfig(clientInterface=TestService.Client)
pool = ThriftClientPool(clientConfig,poolConfig,address)

client = pool.getClient()
print client.test("123")
print client.test("1234")
print client.test("1235")

print pool.getClient().test("abc")
print pool.getClient().test("abcd")
print pool.getClient().test("abce")
</code>
</pre>

