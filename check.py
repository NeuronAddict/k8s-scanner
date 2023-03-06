from utils import NumberedToken, ReturnStatus
import requests
import urllib3
from requests.exceptions import SSLError
from urllib3.exceptions import InsecureRequestWarning


def check(url: str, path: str, port: str, token: NumberedToken = None) -> ReturnStatus:

    headers = {'Authorization': f'Bearer {token.token}'} if token else {}

    url_ = f'{url.strip("/")}:{port}/{path.strip("/")}'

    try:
        urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.get(url_, headers=headers, verify=False)

        if r.status_code < 400:
            print(f'[+] Find url: {url_} with token {token.number if token else "None"}')
    except SSLError as e:
        print(f'[-] SSLError with url {url_}, is the port/scheme correct and the port serving http ? (ex: ssh ports '
              f'not supported)\n[*] skip this url')
        print(e)
        return ReturnStatus(success=False, skip_url=True)
    except Exception as e:
        print(f'[-] Error with url {url_}: {str(e)}')

    return ReturnStatus()
