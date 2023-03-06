import argparse

from check import check
from utils import NumberedToken

parser = argparse.ArgumentParser('Scan k8s api')

url_group = parser.add_mutually_exclusive_group(required=True)
url_group.add_argument('--url', help='url to scan')
url_group.add_argument('--url-file', help='urls to scan, one by line, only scheme+host (ex: https://k8s.example.com)')

path_group = parser.add_mutually_exclusive_group()
path_group.add_argument('--path', help='url to scan')
url_group.add_argument('--path-file', help='path to scan, one by line', default='k8s-dico.txt')

port_group = parser.add_mutually_exclusive_group(required=True)
port_group.add_argument('--port', help='url to scan')
port_group.add_argument('--port-file', help='ports to scan, one by line')

token_group = parser.add_mutually_exclusive_group()
token_group.add_argument('--token', help='token to check')
token_group.add_argument('--token-file', help='file with tokens to use, one by line')

parser.add_argument('--proxy', help='Use proxy')

args = parser.parse_args()


if __name__ == '__main__':

    if args.url:
        urls = [args.url]
    else:
        with open(args.url_file) as f:
            urls = f.readlines()

    if args.path:
        pathes = [args.path]
    else:
        with open(args.path_file) as f:
            pathes = list(map(lambda line: line.strip(), f.readlines()))

    if args.port:
        ports = [args.port]
    else:
        with open(args.port_file) as f:
            ports = list(map(lambda line: line.strip(), f.readlines()))

    if args.token:
        tokens = [args.tokens]
    else:
        if args.token_file:
            with open(args.token_file) as f:
                tokens = list(map(lambda line: line.strip(), f.readlines()))
        else:
            tokens = []

    for url in urls:
        for port in ports:
            for path in pathes:
                status = check(url, path, port)
                if status.skip_url:
                    break
                i = 0
                for token in tokens:
                    i += 1
                    status = check(url, path, port, NumberedToken(token, i))
                    if status.skip_url:
                        break
