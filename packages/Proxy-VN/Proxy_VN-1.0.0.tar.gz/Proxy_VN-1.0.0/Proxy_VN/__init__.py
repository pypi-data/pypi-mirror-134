
import requests,json,time

from requests import api

class Min:
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
        loại=Min.CheckApiKey(api_key)
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

class TM: 
    def Info(api_key):
        check=requests.post('https://tmproxy.com/api/proxy/stats', json={'api_key': api_key}).json()
        if check['code']==0:
            return True
        else:
            return False
    def Get_Proxy(api_key):
        if TM.Info(api_key) == True:
            requests.post('https://tmproxy.com/api/proxy/get-new-proxy', json={'api_key': api_key, 'sign': 'string', 'id_location':1}).json()
            time.sleep(1)
            lấy_proxy=requests.post('https://tmproxy.com/api/proxy/get-current-proxy', json={'api_key': api_key}).json()
            if lấy_proxy['data']['https'] != '':
                return lấy_proxy['data']['https']
            else:
                return 'Lấy Prox Fail'
        elif TM.Info(api_key) == False:
            return 'API Không Hợp Lệ'