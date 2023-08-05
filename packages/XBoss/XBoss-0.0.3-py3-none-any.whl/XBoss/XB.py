# coding:utf-8
'''
Author: F.w
Date: 2021-03-18 08:57:52
LastEditors: F.w 164175317@qq.com
LastEditTime: 2021-12-01 11:01:20
'''
import os
import re
import json
import time
import requests
import datetime
import smtplib
import pandas as pd
import concurrent.futures
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# URL请求
class R_url():
    def __init__(self, url='', header='', data='', R_type='GET', R_url_type='json', B_tpye='json', P_file=''):
        self.url = url
        self.header = header
        self.data = data
        self.R_type = R_type
        self.R_url_type = R_url_type
        self.B_tpye = B_tpye
        self.P_file = P_file

    def d(self):
        if self.R_type == 'GET':
            requests.adapters.DEFAULT_RETRIES = 5
            s = requests.session()
            s.keep_alive = False
            try:
                r = s.get(self.url, headers=self.header, params=self.data, timeout=6000)
            except (Exception):
                try:
                    r = s.get(self.url, headers=self.header, params=self.data, timeout=6000)
                except (Exception):
                    r = None
            if r is not None:
                if self.B_tpye == 'content':
                    data = r.content
                else:
                    r.encoding = r.apparent_encoding
                    if self.B_tpye == 'json':
                        data = json.loads(r.text)
                    elif self.B_tpye == 'text':
                        data = r.text
                    else:
                        exit('-1')
                return data
            else:
                return None
        elif self.R_type == 'POST':
            if self.R_url_type == 'json':
                data_encode = json.dumps(self.data)
            else:
                data_encode = self.data
            try:
                s = requests.Session()
                r = s.post(url=self.url, headers=self.header, data=data_encode, files=self.P_file)
                if self.B_tpye == 'Cookie':
                    r.encoding = r.apparent_encoding
                    r = r.request.headers['Cookie']
                elif self.B_tpye == 'content':
                    r = r.content
                else:
                    try:
                        r.encoding = r.apparent_encoding
                        r = json.loads(r.text)
                    except (Exception):
                        r = r.text
                return r
            except Exception as e:
                return e
        elif self.R_type == 'PUT':
            if self.R_url_type == 'json':
                data_encode = json.dumps(self.data)
            else:
                data_encode = self.data
            try:
                s = requests.Session()
                r = s.put(url=self.url, headers=self.header, data=data_encode, files=self.P_file)
                if self.B_tpye == 'Cookie':
                    r.encoding = r.apparent_encoding
                    r = r.request.headers['Cookie']
                elif self.B_tpye == 'content':
                    r = r.content
                else:
                    try:
                        r.encoding = r.apparent_encoding
                        r = json.loads(r.text)
                    except (Exception):
                        r = r.text
                return r
            except Exception as e:
                return e
        else:
            return None

# 学邦API接口
class Xb_Api():
    __url = 'http://api.xuebangsoft.net/token/'
    __url_data = 'http://api.xuebangsoft.net/'
    def __init__(self, token, id):
        self.token = token
        self.id = id

    def xb_api_header(self):
        url = self.__url + str(self.id)
        header = {'X-XB-CLIENT-PASS': self.token}
        token = R_url(url, header).d()
        token = token['token']
        header = {'X-XB-JWT': token, 'Content-Type': 'application/json'}
        return header

    def get_data(self, url, parm='',method='GET'):
        try:
            data = R_url(self.__url_data + url, self.xb_api_header(), parm, method).d()
            if data['data'] is not None:
                return data['data']
            else:
                return None
        except (Exception):
            return None

# 学邦网页模拟登录
class Login_Xb_boss():
    def __init__(self, phone, password):
        self.phone = phone
        self.password = password

    def Login(self, organizationId=''):
        url = 'https://www.xuebangsoft.net/eduboss/webLogin'
        header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        data = {'contactOrAccount': self.phone, 'password': self.password}
        xb_cookie = R_url(url, header, data, 'POST', '', 'Cookie').d()
        if xb_cookie:
            header = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': xb_cookie,
                'Host': 'www.xuebangsoft.net',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36,'
            }
            try:
                login_info = R_url('https://www.xuebangsoft.net/eduboss/SystemAction/getLoginUserInfo.do', header).d()
            except(Exception):
                login_info=None
            if login_info:
                on_login_organizationId = login_info['organizationId']
                userid = login_info['userId']
                system_id = login_info['institutionId']
                organizationName = login_info['organizationName']
                if organizationId != '' and organizationId != on_login_organizationId:
                    url_o = 'https://www.xuebangsoft.net/eduboss/OrganizationController/switchManageOrganization.do'
                    data_org = {'organizationId': organizationId}
                    r = R_url(url_o, header, data_org).d()
                    on_login_organizationId = R_url('https://www.xuebangsoft.net/eduboss/SystemAction/getLoginUserInfo.do', header).d()['organizationId']
                    if r and on_login_organizationId:
                        if r['resultMessage'] == '操作成功' and organizationId == int(on_login_organizationId):
                            url = f'https://www.xuebangsoft.net/eduboss/AccessTokenController/accessToken.do?uId={userid}&instId={system_id}'
                            header['X-XB-JWT'] = R_url(url, header).d()['data']['access_token']
                    else:
                        header = None
                else:
                    url = f'https://www.xuebangsoft.net/eduboss/AccessTokenController/accessToken.do?uId={userid}&instId={system_id}'
                    header['X-XB-JWT'] = R_url(url, header).d()['data']['access_token']
            else:
                header = None
        else:
            header = None
        return header,organizationName

    def Manage_Organization_list(self):
        header,organizationName = self.Login()
        url = 'https://mastedu.xuebangsoft.net/eduboss/OrganizationController/listManageOrganization.do'
        try:
            Mlist=R_url(url,header).d()
            Mlist={v['name']:v['id'] for v in Mlist}
        except(Exception):
            Mlist=None
        return Mlist

# 学邦系统各列表页面导出筛选条件下所有内容
class details_list_page(Login_Xb_boss):
    def __init__(self,  phone, password, url, organizationId='', method='GET'):
        self.url = url
        self.phone = phone
        self.password = password
        self.organizationId = organizationId
        self.method = method

    def get_pages_list(self):
        header,organizationName = Login_Xb_boss(self.phone, self.password).Login(self.organizationId)
        if header is not None:
            try:
                row = 1000
                url = re.sub(r'&rows=\d+', '&rows={}'.format(str(row)), self.url)
                url = re.sub(r'&nd=\d+', '', url)
                maxrows = R_url(url, header, R_type=self.method).d()['total']
                print(1000, maxrows, flush=True)
            except (Exception):
                try:
                    row = 200
                    url = re.sub(r'rows=\d+', 'rows={}'.format(str(row)), self.url)
                    url = re.sub(r'&nd=\d+', '', url)
                    maxrows = R_url(url, header, R_type=self.method).d()['total']
                    print(200, maxrows, flush=True)
                except (Exception):
                    maxrows = None
            if maxrows is not None:
                url_list = [re.sub(r'&page=\d+', '&page={}'.format(str(i)), url) for i in range(1, maxrows + 1)]
            else:
                url_list = None
        else:
            print('header获取异常！', flush=True)
            url_list = None
        return url_list

    def get_data(self, url):
        header,organizationName = Login_Xb_boss(self.phone, self.password).Login(self.organizationId)
        if header is not None:
            try:
                rows = R_url(url, header).d()['rows']
            except (Exception):
                time.sleep(1)
                rows = R_url(url, header).d()['rows']
        else:
            rows = None
        return rows

    def get_datas(self):
        lists = self.get_pages_list()
        i = 1
        datas = pd.DataFrame()
        if lists is not None:
            with concurrent.futures.ThreadPoolExecutor() as pool:
                futures = {}
                for url in lists:
                    future = pool.submit(self.get_data, url)
                    futures[future] = url
                    time.sleep(0.5)
                for future in concurrent.futures.as_completed(futures):
                    data = pd.DataFrame(future.result())
                    datas = datas.append(data)
                    time.sleep(0.5)
                    print(i, flush=True)
                    i += 1
        return datas

# 学邦系统自定义报表生成及导出
class get_custom_reports(Login_Xb_boss):
    def __init__(self,  phone, password, param, report_name, save_path, organizationId=''):
        self.phone = phone
        self.password = password
        self.organizationId = organizationId
        self.param = param
        self.report_name = report_name
        self.save_path = save_path

    def make_reports(self, header):
        create_Time = R_url('https://www.xuebangsoft.net/eduboss/CommonAction/getServerTime.do?format=yyyy-MM-dd HH:mm:ss', header, B_tpye='text').d()
        create_Time = datetime.datetime.strptime(create_Time, '%Y-%m-%d %H:%M:%S')
        oa_mk_url = 'https://www.xuebangsoft.net/eduboss/web/customizedReportTemplate/CustomizedReportTemplateWebController/exportExcel.do'
        url = f'{oa_mk_url}?param={self.param}'
        create_day = datetime.date.today()
        r = R_url(url, header).d()
        if r['resultMessage'] == '操作成功':
            return create_Time, create_day
        else:
            create_Time = R_url('https://www.xuebangsoft.net/eduboss/CommonAction/getServerTime.do?format=yyyy-MM-dd HH:mm:ss', header, B_tpye='text').d()
            create_Time = datetime.datetime.strptime(create_Time, '%Y-%m-%d %H:%M:%S')
            oa_mk_url = 'https://www.xuebangsoft.net/eduboss/web/customizedReportTemplate/CustomizedReportTemplateWebController/exportExcel.do'
            url = f'{oa_mk_url}?param={self.param}'
            r = R_url(url, header).d()
            if r['resultMessage'] == '操作成功':
                return create_Time, create_day
            else:
                return False

    def download_reports(self):
        header,organizationName = Login_Xb_boss(self.phone, self.password).Login(self.organizationId)
        if header is not None:
            r = self.make_reports(header)
            if r:
                create_data = r[1]
                create_Time = r[0]
                print('报表生成时间:{}'.format(create_Time), flush=True)
                print('生成报表成功！', flush=True)
                run_time = 0
                while run_time < 600:
                    url = f'https://www.xuebangsoft.net/eduboss/web/ExportExcelList/ExportExcelListWebController/page.do?fileName={self.report_name}&status=&name=&startDate={create_data}&endDate={create_data}&_search=false&rows=100&page=1&sidx=this_.id&sord=desc'
                    data = R_url(url, header).d()
                    if data['resultCode'] == 0 and data['total'] > 0:
                        d = data['rows'][0]
                        createTime = datetime.datetime.strptime(d['createTime'], '%Y-%m-%d %H:%M:%S')
                        print('报表时间:{}'.format(d['createTime']), flush=True)
                        # print(d, flush=True)
                        if createTime >= create_Time and d['status'] == 'completed':
                            content = R_url(d['aliPath'], B_tpye='content').d()
                            try:
                                f = open('{}/{}'.format(self.save_path, d['fileName']), 'wb')
                                f.write(content)
                                f.close()
                                print('导出{}-{}成功！'.format(d['createTime'], d['fileName']), flush=True)
                                return '{}/{}'.format(self.save_path, d['fileName'])
                            except Exception as e:
                                print(e)
                                print('下载报表失败！', flush=True)
                                return None
                        else:
                            print('数据还在生成中,5秒后再次执行.........', flush=True)
                            run_time = run_time + 5
                            time.sleep(5)
                    else:
                        print('未查找到数据,5秒后再次执行.........', flush=True)
                        time.sleep(5)
                        run_time = run_time + 5
        else:
            print('头部信息错误,检查帐号密码及系统接口配置是否正确!', flush=True)
            return None

# 企业微信推送信息
class Qw_msg(R_url):
    def __init__(self, userid, msgtype='text', content='', corpid='', corpsecret='', agentid=''):
        self.corpid = corpid
        self.agentid = agentid
        self.corpsecret = corpsecret
        self.msgtype = msgtype
        self.content = content
        self.userid = userid

    def get_token(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={str(self.corpid)}&corpsecret={str(self.corpsecret)}'
        r = R_url(url).d()
        try:
            if r['errmsg'] == 'ok':
                return r['access_token']
            else:
                print(r)
                return None
        except (Exception):
            print(r.text)
            return None

    def up_file(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={str(self.get_token())}&type={str(self.msgtype)}'
        files = {self.msgtype: open(self.content, 'rb')}
        r = R_url(url, R_url_type='dict', R_type='POST', P_file=files).d()
        try:
            if r['errmsg'] == 'ok':
                return r['media_id']
            else:
                print(r)
                return None
        except (Exception):
            print(r)
            return None

    def send(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={str(self.get_token())}'
        message = {'touser': self.userid, 'agentid': self.agentid, 'safe': 0, 'enable_id_trans': 0, 'enable_duplicate_check': 0, 'duplicate_check_interval': 1800, 'msgtype': self.msgtype}
        if self.msgtype == 'text':
            message[self.msgtype] = {"content": self.content}
        elif self.msgtype in ['image', 'voice', 'file']:
            message[self.msgtype] = {"media_id": self.up_file()}
        else:
            print('{}格式错误,不被允许!只能是:text,image,voice,file'.format(self.msgtype))
            return None
        r = R_url(url, data=message, R_url_type='json', R_type='POST').d()
        try:
            if r['errmsg'] == 'ok':
                return r
            else:
                print(r)
                return None
        except (Exception):
            print(r.text)
            return None

# 微信服务号模版消息
class Wx_msg():
    def __init__(self, APPID, APPSECRET, data):
        self.APPID = APPID
        self.APPSECRET = APPSECRET
        self.data = data

    def get_wx_token(self):
        url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={str(self.APPID)}&secret={str(self.APPSECRET)}'
        data = requests.get(url)
        try:
            r = json.loads(data.text)
            return r['access_token']
        except (Exception):
            print(data.text)
            return None

    def send_template_msg(self):
        wx_token = self.get_wx_token()
        if wx_token is not None:
            try:
                url = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={str(wx_token)}'
                data = json.dumps(self.data)
                d = requests.post(url, data)
                print(d.text)
            except (Exception):
                print('发送失败！')
        else:
            print('access_token获取失败！')

# 邮件发送
class Email_message(R_url):
    def __init__(self, receivers=[''], subject_text='', main_text='', send_file_path='', send_file_names=[''], mail_host='', mail_user='', mail_pass='', sender=''):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender
        self.receivers = receivers
        self.subject_text = subject_text
        self.main_text = main_text
        self.send_file_path = send_file_path
        self.send_file_names = send_file_names

    def send_mail(self):
        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receivers[0]
        message['Subject'] = self.subject_text
        message.attach(MIMEText(self.main_text, 'plain', 'utf-8'))
        if self.send_file_path != '' and self.send_file_names != ['']:
            for send_file_name in self.send_file_names:
                part = MIMEText(open(os.path.join(self.send_file_path, send_file_name), 'rb').read(), 'base64', 'utf_8_sig')
                part['Content-Type'] = 'application/octet-stream'
                part.add_header('Content-Disposition', 'attachment', filename=send_file_name)
                message.attach(part)
        try:
            smtpObj = smtplib.SMTP_SSL(host=self.mail_host)
            smtpObj.connect(self.mail_host, 465)
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print('邮件发送成功！')
            smtpObj.quit()
            return True
        except smtplib.SMTPException as e:
            print('邮件发送失败！', e)
            return False

# 钉钉服务端信息推送到工作通知注意服务器出口IP修改
class Ding_talk_message(R_url):
    def __init__(self, userid='', msgtype='text', content='', appkey='', appsecret='', agent_id=''):
        self.appkey = appkey
        self.appsecret = appsecret
        self.agent_id = agent_id
        self.msgtype = msgtype
        self.content = content
        self.userid = userid

    def get_Ding_token(self):
        url = f'https://oapi.dingtalk.com/gettoken?appkey={str(self.appkey)}&appsecret={str(self.appsecret)}'
        result = R_url(url).d()
        try:
            access_token = result['access_token']
            return access_token
        except (Exception):
            return None

    def send_msg(self):
        access_token = self.get_Ding_token()
        if access_token:
            if self.msgtype == 'text':
                try:
                    url = f'https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token={str(access_token)}'
                    data = {
                        'agent_id': self.agent_id,
                        'userid_list': str(self.userid),
                        'msg': {
                            'msgtype': 'text',
                            'text': {
                                'content': self.content,
                            }
                        }
                    }
                    result = R_url(url, data=data, R_type='POST').d()
                except (Exception):
                    result = ''
            elif self.msgtype == 'action_card':
                try:
                    url = f'https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token={str(access_token)}'
                    data = {
                        'agent_id': self.agent_id,
                        'userid_list': str(self.userid),
                        'msg': {
                            "msgtype": "action_card",
                            "action_card": self.content,
                        }
                    }
                    result = R_url(url, data=data, R_type='POST').d()
                except (Exception):
                    result = ''
            else:
                try:
                    url = f'https://oapi.dingtalk.com/media/upload?access_token={str(access_token)}&type={str(self.msgtype)}'
                    files = {'media': open(self.content, 'rb')}
                    data = {'access_token': access_token, 'type': self.msgtype}
                    response = R_url(url, data=data, R_url_type='dict', R_type='POST', P_file=files).d()
                    media_id = response["media_id"]
                except (Exception):
                    media_id = None
                if media_id:
                    try:
                        msg = {'agent_id': self.agent_id, 'userid_list': str(self.userid), 'msg': {"msgtype": self.msgtype, self.msgtype: {"media_id": media_id}}}
                        url = 'https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2?access_token=' + access_token
                        result = R_url(url, data=msg, R_url_type='json', R_type='POST').d()
                    except (Exception):
                        result = ''
                else:
                    result = ''
        else:
            result = ''
        return result

if __name__=='__main__':
    pass
