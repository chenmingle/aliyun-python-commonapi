#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'chenmingle'


from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest,DescribeDomainRecordsRequest,UpdateDomainRecordRequest,AddDomainRecordRequest,DeleteDomainRecordRequest,SetDomainRecordStatusRequest
import json,urllib,re
import sys


client = AcsClient(
   "access_ id",
   "access_key",
   "cn-shenzhen"
);


###查看二级域名信息###
def list_domain():
    DomainList = DescribeDomainsRequest.DescribeDomainsRequest()
    DomainList.set_accept_format('json')
    DNSListJson = json.loads(client.do_action_with_exception(DomainList))
    for i in DNSListJson['Domains']['Domain']:
    	print i['DomainName']
    #print DNSListJson


###查看某个域名信息###
def list_dns_record(DomainName):
    AliyunRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest() 
    AliyunRecords.set_accept_format('json')
    AliyunRecords.set_DomainName(DomainName)
    AliyunRecordsJson = json.loads(client.do_action_with_exception(AliyunRecords))
    print DomainName+':'
#    print AliyunRecordsJson
    for x in AliyunRecordsJson['AliyunRecords']['Record']:
         RecordId = x['RecordId']
	 RR = x['RR']
         Type = x['Type']
	 Line = x['Line']
	 Value = x['Value']
	 TTL = x['TTL']
	 Status = x['Status']
	 txt =  RecordId+' '+RR+' '+Type+' '+Line+' '+Value+' '+str(TTL)+' '+Status
	 print txt
    print '\n'


###修改域名配置解析###
def edit_dns_record(DomainName, hostname, hostname_new, Types, IP):
    AliyunRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    AliyunRecords.set_accept_format('json')
    AliyunRecords.set_DomainName(DomainName)
    AliyunRecordsJson = json.loads(client.do_action_with_exception(AliyunRecords))
    for x in AliyunRecordsJson['AliyunRecords']['Record']:
	if hostname == x['RR']:
		RecordId = x['RecordId']
		AliyunUpdateRecord = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
		AliyunUpdateRecord.set_accept_format('json')
		AliyunUpdateRecord.set_RecordId(RecordId)
		AliyunUpdateRecord.set_RR(hostname_new)
		AliyunUpdateRecord.set_Type(Types)
		AliyunUpdateRecord.set_TTL('600')
		AliyunUpdateRecord.set_Value(IP)
		AliyunUpdateRecordJson = json.loads(client.do_action_with_exception(AliyunUpdateRecord))
		print AliyunUpdateRecordJson


###添加域名解析###
def add_dns_record(DomainName, hostname, Types, IP):
    AliyunAddRecord = AddDomainRecordRequest.AddDomainRecordRequest()
    AliyunAddRecord.set_DomainName(DomainName)
    AliyunAddRecord.set_RR(hostname)
    AliyunAddRecord.set_Type(Types)
    AliyunAddRecord.set_TTL('600')
    AliyunAddRecord.set_Value(IP)
    AliyunAddRecordJson = json.loads(client.do_action_with_exception(AliyunAddRecord))
    print AliyunAddRecordJson


###删除域名解析###
def delete_dns_record(DomainName, hostname):
    AliyunRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    AliyunRecords.set_accept_format('json')
    AliyunRecords.set_DomainName(DomainName)
    AliyunRecordsJson = json.loads(client.do_action_with_exception(AliyunRecords))
    for x in AliyunRecordsJson['AliyunRecords']['Record']:
    	if hostname == x['RR']:
		RecordId = x['RecordId']
		AliyunDelRecord = DeleteDomainRecordRequest.DeleteDomainRecordRequest()
		AliyunDelRecord.set_RecordId(RecordId)
		AliyunDelRecordJson = json.loads(client.do_action_with_exception(AliyunDelRecord))
		print AliyunDelRecordJson


###设置域名解析状态###
def set_dns_record(DomainName, hostname, status):
    AliyunRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    AliyunRecords.set_accept_format('json')
    AliyunRecords.set_DomainName(DomainName)
    AliyunRecordsJson = json.loads(client.do_action_with_exception(AliyunRecords))
    for x in AliyunRecordsJson['AliyunRecords']['Record']:
        if hostname == x['RR']:
                RecordId = x['RecordId']
                AliyunSetRecord = SetDomainRecordStatusRequest.SetDomainRecordStatusRequest()
                AliyunSetRecord.set_accept_format('json')
                AliyunSetRecord.set_RecordId(RecordId)
                AliyunSetRecord.set_Status(status)
                AliyunSetRecordJson = json.loads(client.do_action_with_exception(AliyunSetRecord))
                print AliyunSetRecordJson


DomainName = sys.argv
for i in DomainName:
	if i == sys.argv[0]:
		pass
	else:
		list_dns_record(i)

#edit_dns_record('test.xin', 'test', 'test_ok', 'A', '121.20.122.103')
#add_dns_record('test.xin', 'test', 'A', '121.20.122.103')
#delete_dns_record('test.xin','test_ok')
#set_dns_record('test.xin', 'test_ok', 'DISABLE')
#set_dns_record('test.xin', 'test_ok', 'ENABLE')
list_domain()
