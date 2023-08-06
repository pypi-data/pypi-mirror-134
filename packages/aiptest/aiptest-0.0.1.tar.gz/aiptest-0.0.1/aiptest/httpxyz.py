import logging
import requests
import requests.auth


class HttpXyz(object):

    def __init__(self):
        """
        在第一次实例Requester模块时，先进行session的实例化以及请求方法的实例
        """
        logging.getLogger("requests").setLevel(logging.ERROR)  # 用于去除requests的多余log
        self.HttpSessions = None
        self._sessions()

    def _sessions(self):
        self.HttpSessions = requests.Session()
        self.METHODS = {'GET': self.HttpSessions.get,
                        'POST': self.HttpSessions.post,
                        'PUT': self.HttpSessions.put,
                        'DELETE': self.HttpSessions.delete,
                        'HEAD': self.HttpSessions.head,
                        'PATCH': self.HttpSessions.patch}

    # TO--DO 完成请求封装，后续需要在解析case的时候限制可选参数的key值，保证程序不会报TypeError
    def request(self, method, url, new=False, data=None, json=None, **kwargs):
        """
            封装request 请求，使所有请求都在session中进行，当有新的session页时只需要传入new=True即可刷新session页面，
        刷新之后之前的session页面保存的cookie等信息也将被刷新。没有保存session功能，请不要随意调用该方法
        :param method: 请求方法，get post put 等这些，规定是大写
        :param url: 请求地址
        :param new: 是否为新页面 刷新session(可选) 默认为false
        :param data: data数据，(可选) 默认为空值
        :param json: json数据，（可选） 默认为空值
        :param kwargs:缺省参数 ，（可选） 包含
                params, headers, cookies, files,auth,timeout,
                allow_redirects, proxies,hooks, stream, verify, cert
                超过以上列出来的参数会提示 TYPEERROR
        :return: response 将response值返回出来
        """
        method = method.upper()
        # 三元表达式
        self._sessions() if new else None
        if method in ('GET', 'DELETE', 'HEAD'):
            return self.METHODS[method](url, **kwargs)
        elif method == 'POST':
            return self.METHODS['POST'](url, data, json, **kwargs)
        else:
            return self.METHODS[method](url, data, **kwargs)

    def authentication(self, username, password, url, data):
        auth = requests.auth.HTTPBasicAuth(username, password)
        auth_response = requests.post(url, auth=auth, data=data)
        return auth_response
