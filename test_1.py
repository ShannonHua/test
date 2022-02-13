# -*- coding: utf-8 -*-
# author: 华测-长风老师
from requests import request


def api(protocol, host, port, method, path=None, **kwargs):
    """
    api 是用来在真正开始用例之前输出测试用例的执行数据
    :return: 返回一个能被request 接受的数据体（可以是一个dict）
    """
    """
    1.请求协议
    2.请求方式
    3.请求host
    4.请求的端口
    5.请求的路径
    6.请求的url地址
    7.请求的数据（json、data、params）
    """

    print(f"协议是：{protocol}")
    print(f"主机是：{host}")
    print(f"端口是：{port}")
    kwargs.update(
        {
            "url": f"{protocol}://{host}:{port}/{path}",
            "method": method
        }
    )
    for key in kwargs.keys():
        print(f"请求中的{key}是:{kwargs[f'{key}']}")
    # print(f"路径是：{kwargs['url']}")
    # if "params" in kwargs.keys():
    #     print(f"请求参数有params：{kwargs['params']}")
    # if "json" in kwargs.keys():
    #     print(f"请求参数有json：{kwargs['json']}")
    # if "data" in kwargs.keys():
    #     print(f"请求参数有data：{kwargs['data']}")

    return kwargs  # 这个字典需要被 request 接受


# def test():
#     """函数内部就是我们的测试用例我们只需要运行这个测试用例就好了；"""
#     """
#     我们需要将这个用例的构建方式变简单；
#
#     假设，我们的日志就是（print）
#
#     """
#
#     data = {'data': {'pwd': 'changfeng', 'type': 'username', 'accounts': 'test_changfeng'},
#             'url': 'http://shop-xo.hctestedu.com:80/index.php?s=/api/user/login&application=app', 'method': 'post'}
#     print("请求数据是：", data["data"])
#     print("请求方法是：", data["method"])
#     print("请求路径是：", data["url"])
#     # 接口测试的日志（输入，输出）
#     # 接口日志应该记录请求数据的情况，响应数据的情况
#     req = request(**data)  # request  它固定就是那么些内容
#     print("响应结果是：", req.json())
#
#     print(req)


def test01():
    """第二次构建接口请求"""

    req = request(**api(
        protocol="http",
        host="shop-xo.hctestedu.com",
        port=80,
        method="post",
        path="index.php",
        params={
            "s": "/api/user/login",
            "application": "app"
        },
        data={
            'pwd': 'changfeng',
            'type': 'username',
            'accounts': 'test_changfeng'
        }
    ))

    print("测试结果是：", req.json())


if __name__ == '__main__':
    import pytest

    pytest.main(["--html=report/report.html"])  # 可以转化成命令行运行
