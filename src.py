import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def gmail_username_is_valid(username):
    headers = {
        'Host': 'accounts.google.com',
        'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
        'X-Same-Domain': '1',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Google-Accounts-Xsrf': '1',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://accounts.google.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    params = (('hl', 'en'))
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowEntry=SignUp&flowName=GlifWebSignIn&service=mail&f.req=%5B%22AEThLlz0ie2eUdQidITxZNPKyWo9F5CHezhV4m5iJFb6Y0fXxhEeIqcqkJyzi9iLnqqM_5nbXYCjdPivsYu8GjCs3AntdmSWeazb070mWDXAAP0AxacM6X2yIOwSMsEUZ6VvUFvUJGndaMrFyvXa98xb3KEfhEQnd3JQHN0Yxqg0KKeClozPPEEh5vCwwSglfu7kDtYqZ04Zk_enDoXgzgDx_8P9fSvBkw%22%2C%22%22%2C%22%22%2C%22{username}%22%2Ctrue%2C%22S1158501710%3A1634620721349897%22%2C1%5D&azt=AFoagUX07RTYvixRfsvPo1DuUMXJvEl4bw%3A1634620721364&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%5D'.format(username = username)
    response = requests.post('https://accounts.google.com/_/signup/webusernameavailability', headers=headers, params=params, data=data, verify=False)
    response_text = response.text.splitlines()[-1]
    response_text = "".join(response_text.split())
    parsed_res = json.loads(response_text)
    isValid = True if parsed_res[0][1] == 1 else False
    sugestions = parsed_res[0][2]
    return isValid, sugestions


username = 'alifalehh8'

isValid, sugestions = gmail_username_is_valid(username)

print("user is valid : ", isValid)
if not isValid:
    print("sugestions : ", sugestions)

# using proxy :

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

r = requests.get(url, headers=headers, proxies=proxyDict)






import requests
from bs4 import BeautifulSoup
import json


def is_valid_apple_id(email):
    headers = {
        'Host': 'appleid.apple.com',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://appleid.apple.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }
    response = requests.get('https://appleid.apple.com/', headers=headers, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    bot_keys = soup.find_all("script", {"id": "boot_args"})[0].get_text()
    aidsp = response.headers['Set-Cookie'].split(';')[-5].split('=')[1]
    scnt = json.loads(bot_keys)["direct"]["scnt"]
    api_key = json.loads(bot_keys)["direct"]["apiKey"]
    sessionId = json.loads(bot_keys)["direct"]["sessionId"]
    headers = {
        'Host': 'appleid.apple.com',
        'X-Apple-I-Fd-Client-Info': '{"U":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36","L":"en-US","Z":"GMT+03:00","V":"1.1","F":".ta44j1e3NlY5BNlY5BSs5uQ084akJ1FmkxOHxcKB8i.uJtHoqvynx9MsFyxY25BCw0Tf50FL1kb9WDK1civyfw8btTrl7klY5BNleBBNlYCa1nkBMfs.7Sh"}',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Apple-Request-Context': 'create',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Apple-I-Timezone': 'Asia/Baghdad',
        'Sec-Ch-Ua': '";Not A Brand";v="99", "Chromium";v="94"',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://appleid.apple.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://appleid.apple.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close',
    }
    headers["X-Apple-Id-Session-Id"] = sessionId
    headers["Scnt"] = scnt
    headers["X-Apple-Api-Key"] = api_key
    cookies = {
        'idclient': 'web',
        'dslang': 'US-EN',
        'site': 'USA',
        'aidsp': aidsp,
        'geo': 'IQ',
    }
    data = '{"emailAddress":"'+email+'"}'
    response = requests.post('https://appleid.apple.com/account/validation/appleid', headers=headers, cookies=cookies, data=data, verify=False)
    return json.loads(response.text)['used']



print(is_valid_apple_id("alifalih783783333@gmail.com"))