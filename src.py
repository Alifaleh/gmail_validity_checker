import requests
import json

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
    response = requests.post('https://accounts.google.com/_/signup/webusernameavailability', headers=headers, params=params, data=data)
    response_text = response.text.splitlines()[-1]
    response_text = "".join(response_text.split())
    parsed_res = json.loads(response_text)
    isValid = True if parsed_res[0][1] == 1 else False
    sugestions = parsed_res[0][2]
    return isValid, sugestions


# Example of Use:
username = 'alifaleh'
isValid, sugestions = gmail_username_is_valid(username)
print("user is valid : ", isValid)
if not isValid:
    print("sugestions : ", sugestions)