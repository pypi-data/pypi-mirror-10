# -*- coding: UTF-8 -*-
# lvjiyong on 2015/6/7.

"""
封装Http Request，结果以Response输出
"""
__all__ = ['Request']

import chardet
from ghttp import http, utils
from ghttp.response import Response
from ghttp.parameter import Parameter


class Request(Parameter):
    """
    封装http请求，输出response等
    >>> page = Request('https://www.baidu.com/')
    >>> 'baidu' in page.response.body
    True
    >>> page.response.encoding
    'utf-8'

    """

    def set_response(self, url, **kwargs):
        self.url = url
        params = Parameter(kwargs)
        self.headers = params.headers
        self.cookies = params.cookies
        if url and str(url).startswith('http'):
            content, info = http.request_with_header(url, **kwargs)
            self.status = info.getcode()
            params.headers = info.headers
            params.body = content
            params.cookies = info.headers.get('Set-Cookie')
            response = Response(url=url, **params)

            # 获取编码方式并解码
            encoding = self.encoding
            if not encoding:
                encoding = utils.match_encoding(response.body)
                if not encoding:
                    encoding = utils.match_encoding(params.headers.get("Content-Type", ""))
                if not encoding:
                    encoding = 'utf-8'

            if encoding.lower() in ('gbk', 'gb2312'):
                encoding = 'gb18030'
            try:
                response.encoding = encoding
                response._body_as_unicode = response.body.decode(response.encoding, 'ignore')
            except:
                response.encoding = chardet.detect(response.body).get('encoding')
                response._body_as_unicode = response.body.decode(response.encoding, 'ignore')
            self.response = response

    def __init__(self, url, **kwargs):
        super(Request, self).__init__(**kwargs)
        self.url = url
        self.response = None
        self.headers = None
        self.status = 0
        self.cookies = None
        self.set_response(url=url, **kwargs)
        self.encoding = kwargs.get('encoding') or 'utf-8'
        callback = kwargs.get('callback')
        if callback:
            call = callback(self.response)
            if hasattr(call, 'next'):
                call.next()
                # except Exception as e:
                # if err_callback:
                # err_callback(e)
                # else:
                #         raise e


if __name__ == "__main__":
    import doctest

    doctest.testmod()