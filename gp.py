import requests
import threading

url = 'https://gmpay.top/site/card-submit'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '325',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'aff1135=aea4063f91adadaa4fea56a7189c7cf5527339467bd5fa74d1e69271b41bf7e1a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22aff1135%22%3Bi%3A1%3Bs%3A13%3A%226022bea3a77ca%22%3B%7D; userHash=d1c4be35194c32e93da072725ce274781c2978ebfbebcfbff0d7f4077e106317a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22userHash%22%3Bi%3A1%3Bs%3A32%3A%22bce8e75ce66cc00c8203ddf07a7c4a03%22%3B%7D; _csrf-frontend=a437a64b22b3079dd930b703305eff72a6edbb79ae70af12f72f00b527703e88a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22SEUAFvA6Gr3a_1exzJYUWSYJh2pxJAxN%22%3B%7D',
    'Host': 'gmpay.top',
    'Origin': 'https://gmpay.top',
    'Referer': 'https://gmpay.top/600050dc7ccd2/pp/4488f6072b31a?codePartner=6022bea3a77ca&uniqueCode=152951f4a2c41057dee077d0bd6e0d96',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'X-CSRF-Token': '8PWvtzM3JCLpokQfVbq6dT4E2xDHSPien3QBLtGOPVCjsPr2dUFlFK7Qd34Ki98NRE6CRZAbodT3RnFWm89FHg==',
    'X-Requested-With': 'XMLHttpRequest',
}

data ={
    '_csrf-frontend': 'kRoIHR4McAj5CScAaziQeUelcpAmRV7b9t1WfOago07CVx1cWHoxPr57FGE0CfUBPe8rxXEWB5Ge7yYErOHbAA==',
    'id': '5520819',
    'name': 'Ivan ivanov',
    'number': '4074 6527 2172 1471',
    'month': '09',
    'year': '21',
    'cvv': '234',
}
#def do_request():
 #   while True:
response = requests.post(url, data=data, headers=headers).text
print(response)
'''        
threads = []

for i in range(50):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()
    
for i in range(50):
    threads[i].join()
'''
