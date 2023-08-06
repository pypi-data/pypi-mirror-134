import os,requests,json
import time

from requests import api
#Class Form
def CheckApiKey(api_key):
    try:
        test=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy/get-status?api_key={api_key}').json()
        if test['message']=="API Tồn Tại" and test['code'] == 1:
            type="IPV6"
    except:
        type="0 có"
    if type=="0 có":
        try:
            test2=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy_v4/get-status?api_key={api_key}').json()
            if test2['message']=="API Tồn Tại" and test2['code'] == 1:
                type="IPV4"
        except:
            type="0 cớ"
    return type
def Get_Proxy(api_key):
    loại=CheckApiKey(api_key)
    if loại == "IPV4":
        a=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy_v4/get-current-proxy?api_key={api_key}').json()
        if a['message']=="API Này Không Có Proxy" or a['data']['timeout'] < 300:
            requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy_v4/get-new-proxy?api_key={api_key}').json()
            time.sleep(2)
        lấy=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy_v4/get-current-proxy?api_key={api_key}').json()
        if lấy['message']=="API Tồn Tại":
            ip_port=lấy['data']['http_proxy_ipv4']
            return ip_port
    elif loại=="IPV6":
        a=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy/get-current-proxy?api_key={api_key}').json()
        if a['message']=="API Này Không Có Proxy" or a['data']['timeout'] < 300:
            lấy_proxy=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy/get-new-proxy?api_key={api_key}').json()
            if lấy_proxy['message']=="khong con proxy":
                return "Emtry"
            elif lấy_proxy['message'] != "khong con proxy" and  lấy_proxy['data']['http_proxy'] != '':
                pass
        b=requests.get(f'https://dash.minproxy.vn/api/rotating/v1/proxy/get-current-proxy?api_key={api_key}').json()
        if b['data']['http_proxy']!='':
            return b['data']['http_proxy']