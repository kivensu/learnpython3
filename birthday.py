import sys
import json
import pymysql
from aliyunsdkcore import client
from aliyunsdkslb.request.v20140515 import DescribeLoadBalancersRequest

# 参数获取
AccessKey = sys[0]
AccessSecret = sys[1]
Regin = sys[2]


clt = client.AcsClient(AccessKey, AccessSecret, Regin)
request = DescribeLoadBalancersRequest.DescribeLoadBalancersRequest()
request.set_accept_format('json')
request.set_PageSize(100)
request.set_PageNumber(1)
response = json.loads(clt.do_action_with_exception(request), encoding='UTF-8')

for info in response.get('LoadBalancers').get('LoadBalancer'):
    slb_number = info.get('LoadBalancerId')
    slb_name = info.get('LoadBalancerName')
    slb_status = info.get('LoadBalancerStatus')
    slb_address = info.get('Address')
    address_type = info.get('AddressType')
    region = info.get('Regin_Id')
    network_type = info.get('NetworkType')
    bandwidth = info.get('Bandwidth')
    create_time = info.get('CreateTime')
    masterZone = info.get('MasterZone')
    slaveZone = info.get('SlaveZoneId')
