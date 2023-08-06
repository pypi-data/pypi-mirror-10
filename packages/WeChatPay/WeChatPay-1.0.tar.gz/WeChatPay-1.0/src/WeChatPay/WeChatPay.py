# -*- coding: utf-8 -*-
import os
import time
import re
import logging
import datetime

from django.core.cache import cache
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import requests

from llt.utils import random_str, smart_str
from llt.url import sign_url

# Get an instance of a logger
logger = logging.getLogger(__name__)


def get_config(name):
    """
    Get configuration variable from environment variable
    or django setting.py
    """
    config = os.environ.get(name, getattr(settings, name, None))
    if config:
        return config
    else:
        raise ImproperlyConfigured("Can't find config for '%s' either in environment"
                                   "variable or in settings.py" % name)

WC_PAY_APPID = get_config('WC_PAY_APPID')
WC_PAY_MCHID = get_config('WC_PAY_MCHID')
WC_PAY_KEY = get_config('WC_PAY_KEY')
WC_PAY_APPSECRET = get_config('WC_PAY_APPSECRET')
WC_BILLS_PATH = get_config('BILLS_DIR')


def dict_to_xml(params, sign):
    xml = ['<xml>']
    for (k, v) in params.items():
        if v.isdigit():
            xml.append('<%s>%s</%s>' % (k, v, k))
        else:
            xml.append('<%s><![CDATA[%s]]></%s>' % (k, v, k))

    if sign:
        xml.append('<sign><![CDATA[%s]]></sign>' % sign)
    xml.append('</xml>')
    return ''.join(xml)


def xml_to_dict(xml):
    if xml[0:5].upper() != "<XML>" and xml[-6].upper() != "</XML>":
        return None, None

    result = {}
    sign = None
    content = ''.join(xml[5:-6].strip().split('\n'))

    pattern = re.compile(r'<(?P<key>.+)>(?P<value>.+)</(?P=key)>')
    m = pattern.match(content)
    while m:
        key = m.group('key').strip()
        value = m.group('value').strip()
        if value != '<![CDATA[]]>':
            pattern_inner = re.compile(r'<!\[CDATA\[(?P<inner_val>.+)\]\]>')
            inner_m = pattern_inner.match(value)
            if inner_m:
                value = inner_m.group('inner_val').strip()
            if key == 'sign':
                sign = value
            else:
                result[key] = value

        next_index = m.end('value') + len(key) + 3
        if next_index >= len(content):
            break
        content = content[next_index:]
        m = pattern.match(content)

    return sign, result


def get_access_token(app_id=WC_PAY_APPID, app_secret=WC_PAY_APPSECRET):
    """
    获取access_token
    :return: access_token
    """
    key = 'wechat:app_id_%s:access_token' % app_id
    access_token = cache.get(key)
    if access_token:
        # logger.debug('Get access token [%s] from cache, key: [%s]' %
        # (access_token, key))
        return access_token

    params = {'grant_type': 'client_credential',
              'appid': app_id,
              'secret': app_secret}
    response = requests.get(
        'https://api.weixin.qq.com/cgi-bin/token', params=params)
    logger.info('Make request to %s' % response.url)

    json_data = response.json()
    if 'errcode' in json_data:
        raise ValueError('Get access token failed, errcode: [%s], errmsg: [%s]' %
                         (json_data['errcode'], json_data['errmsg']))

    # logger.debug('Put access token [%s] into cache, key: [%s]' %
    # (json_data['access_token'], key))
    cache.set(key, json_data['access_token'], timeout=int(
        json_data['expires_in']) - 60)
    return json_data['access_token']


def get_jsapi_ticket(app_id=WC_PAY_APPID):
    """
    获取jsapi_ticket
    :return: jsapi_ticket
    """
    key = 'wechat:app_id_%s:jsapi_ticket' % app_id
    jsapi_ticket = cache.get(key)
    if jsapi_ticket:
        # logger.debug('Get jsapi ticket [%s] from cache, key: [%s]' %
        # (jsapi_ticket, key))
        return jsapi_ticket

    params = {'access_token': get_access_token(),
              'type': 'jsapi'}
    response = requests.get(
        'https://api.weixin.qq.com/cgi-bin/ticket/getticket', params=params)
    logger.info('Make request to %s' % response.url)

    json_data = response.json()
    if json_data['errcode'] != 0:
        raise ValueError('Get jsapi ticket failed, errcode: [%s], errmsg: [%s]' %
                         (json_data['errcode'], json_data['errmsg']))

    # logger.debug('Put jsapi ticket [%s] into cache, key: [%s]' %
    # (json_data['ticket'], key))
    cache.set(key, json_data['ticket'], timeout=int(
        json_data['expires_in']) - 60)
    return json_data['ticket']


def get_js_config_params(url, nonce_str, time_stamp):
    """
    获取js_config初始化参数
    """
    params = {'noncestr': nonce_str,
              'jsapi_ticket': get_jsapi_ticket(),
              'timestamp': '%d' % time_stamp,
              'url': url}

    # params['signature'] = calculate_sign(params, sign_type='sha1',
    # upper_case=False)
    params['signature'] = sign_url(params, '', sign_type='sha1')
    return params


class WeChatPay(object):

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        self.app_id = app_id
        self.mch_id = mch_id
        self.api_key = api_key
        self.common_params = {'appid': self.app_id,
                              'mch_id': self.mch_id}
        self.params = {}
        self.url = ''

    def set_params(self, **kwargs):
        self.params = {}
        for (k, v) in kwargs.items():
            self.params[k] = smart_str(v)

        self.params['nonce_str'] = random_str(length=32)
        self.params.update(self.common_params)

    def post_xml(self):
        xml = self.dict2xml(self.params)

        response = requests.post(self.url, data=xml)
        logger.info('Make post request to %s' % response.url)
        logger.debug('Request XML: %s' % xml)
        logger.debug('Response encoding: %s' % response.encoding)
        logger.debug('Response XML: %s' % ''.join(response.text.splitlines()))

        return self.xml2dict(response.text.encode(response.encoding)) if response.encoding else response.text

    def post_xml_ssl(self):
        xml = self.dict2xml(self.params)

        cert_file = os.sep.join(
            [settings.ROOT_DIR, 'config/wechat/apiclient_cert.pem'])
        key_file = os.sep.join(
            [settings.ROOT_DIR, 'config/wechat/apiclient_key.pem'])
        logger.debug('Cert file: %s' % cert_file)
        logger.debug('Key file: %s' % key_file)
        response = requests.post(
            self.url, data=xml, verify=True, cert=(cert_file, key_file))
        logger.info('Make SSL post request to %s' % response.url)
        logger.debug('Request XML: %s' % xml)
        logger.debug('Response encoding: %s' % response.encoding)
        logger.debug('Response XML: %s' % ''.join(response.text.splitlines()))

        return self.xml2dict(response.text.encode(response.encoding)) if response.encoding else response.text

    def dict2xml(self, params, with_sign=True):
        sign = sign_url(
            params, self.api_key, key_name='key', upper_case=True) if with_sign else None
        return dict_to_xml(params, sign)

    def xml2dict(self, xml):
        sign, params = xml_to_dict(xml)
        if not sign or not params:
            raise ValueError('Convert xml to dict failed, xml: [%s]' % xml)

        if params['appid'] != self.app_id or params['mch_id'] != self.mch_id:
            raise ValueError('Invalid appid or mch_id, appid: [%s], mch_id: [%s]' % (params['appid'],
                                                                                     params['mch_id']))

        if params['return_code'] != 'SUCCESS':
            raise ValueError('WeChat proccess request failed, return code: [%s], return msg: [%s]' %
                             (params['return_code'], params.get('return_msg', '')))

        calc_sign = sign_url(
            params, self.api_key, key_name='key', upper_case=True)
        if calc_sign != sign:
            raise ValueError(
                'Invalid sign, calculate sign: [%s], sign: [%s]' % (calc_sign, sign))

        if params['result_code'] != 'SUCCESS':
            logger.error('WeChat process request failed, result_code: [%s], err_code: [%s], err_code_des: [%s]' %
                         (params['result_code'], params.get('err_code', ''), params.get('err_code_des', '')))

        return params


class UnifiedOrderPay(WeChatPay):

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(UnifiedOrderPay, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'
        self.trade_type = ''

    def _post(self, body, out_trade_no, total_fee, spbill_create_ip, notify_url, **kwargs):
        params = {'body': body,
                  'out_trade_no': out_trade_no,
                  'total_fee': total_fee,
                  'spbill_create_ip': spbill_create_ip,
                  'notify_url': notify_url,
                  'trade_type': self.trade_type}
        params.update(**kwargs)

        self.set_params(**params)
        return self.post_xml()


class NativeOrderPay(UnifiedOrderPay):

    """
    Native 统一支付类
    """

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(NativeOrderPay, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.trade_type = 'NATIVE'

    def post(self, body, out_trade_no, total_fee, spbill_create_ip, notify_url):
        return super(NativeOrderPay, self)._post(body, out_trade_no, total_fee, spbill_create_ip, notify_url)


class JsAPIOrderPay(UnifiedOrderPay):

    """
    H5页面的js调用类
    """

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(JsAPIOrderPay, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.trade_type = 'JSAPI'

    def post(self, body, out_trade_no, total_fee, spbill_create_ip, notify_url, open_id, url):
        # 直接调用基类的post方法查询prepay_id，如果成功，返回一个字典
        unified_order = super(JsAPIOrderPay, self)._post(body, out_trade_no, total_fee, spbill_create_ip,
                                                         notify_url, open_id=open_id)
        nonce_str = random_str(length=32)
        time_stamp = time.time()

        pay_params = {'appId': self.app_id,
                      'timeStamp': '%d' % time_stamp,
                      'nonceStr': nonce_str,
                      'package': 'prepay_id=%s' % unified_order.get('prepay_id'),
                      'signType': 'MD5'}
        pay_params['paySign'] = sign_url(
            pay_params, self.api_key, key_name='key', upper_case=True)

        unified_order.update({'pay_params': pay_params,
                              'config_params': get_js_config_params(url, nonce_str, time_stamp)})

        return unified_order


class OrderQuery(WeChatPay):

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(OrderQuery, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.url = 'https://api.mch.weixin.qq.com/pay/orderquery'

    def post(self, out_trade_no):
        params = {'out_trade_no': out_trade_no}
        self.set_params(**params)
        return self.post_xml()


class Notify(WeChatPay):
    pass


class Refund(WeChatPay):

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(Refund, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.url = 'https://api.mch.weixin.qq.com/secapi/pay/refund'

    def post(self, out_trade_no, out_refund_no, total_fee, refund_fee):
        params = {'out_trade_no': out_trade_no,
                  'out_refund_no': out_refund_no,
                  'total_fee': total_fee,
                  'refund_fee': refund_fee,
                  'op_user_id': self.mch_id}
        self.set_params(**params)
        return self.post_xml_ssl()


class RefundQuery(WeChatPay):

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(RefundQuery, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.url = 'https://api.mch.weixin.qq.com/pay/refundquery'

    def post(self, out_refund_no):
        params = {'out_refund_no': out_refund_no}
        self.set_params(**params)
        return self.post_xml_ssl()


class DownloadBill(WeChatPay):

    def __init__(self, app_id=WC_PAY_APPID, mch_id=WC_PAY_MCHID, api_key=WC_PAY_KEY):
        super(DownloadBill, self).__init__(
            app_id=app_id, mch_id=mch_id, api_key=api_key)
        self.url = 'https://api.mch.weixin.qq.com/pay/downloadbill'

    def post(self, bill_date=None, bill_type='ALL'):
        params = {}
        if bill_date:
            params = {'bill_date': bill_date,
                      'bill_type': bill_type}
        else:
            today = datetime.date.today()
            t = datetime.timedelta(days=1)
            yesterday = str(today - t).replace('-', '')
            params['bill_date'] = yesterday
            params['bill_type'] = bill_type

        self.set_params(**params)
        res = self.post_xml().replace('`', '')

        month_dir = '%s' % params['bill_date'][:6]

        if not os.path.exists(os.path.join(WC_BILLS_PATH, month_dir)):
            os.makedirs(os.path.join(WC_BILLS_PATH, month_dir))

        with open(os.path.join(WC_BILLS_PATH, month_dir) + "/WeChat_%s.csv" % (params['bill_date']), "wb") as f:
            f.write(res.encode("UTF-8"))
            f.close()
