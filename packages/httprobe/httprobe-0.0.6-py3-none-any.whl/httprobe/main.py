import sys
import time
import requests
import re
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import urllib3
import pandas as pd
from tabulate import tabulate
from concurrent.futures import ThreadPoolExecutor, as_completed

argparser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
argparser.add_argument('-H', '--header', nargs='+', action='extend', help='Header to include in the request')
argparser.add_argument('-L', '--follow-redirects', action='store_true', default=False, help='Follow redirections')
argparser.add_argument('-X', '--method', type=str.lower, default='GET', help='HTTP method to use for the requests')
argparser.add_argument('-d', '--data', default=None, help='Body data to include in request')
argparser.add_argument('--connect-timeout', '--ct', type=float, default=15, help='Connection timeout')
argparser.add_argument('--read-timeout', '--rt', type=float, default=15, help='Read timeout')
argparser.add_argument('-c', '-t', '--threads', type=int, default=20, help='Number of concurrent requests')
argparser.add_argument('-p', '-s', '--delay', type=float, default=0, help='Delay in seconds to wait between requests')
argparser.add_argument('-o', '--output-file', help='Write output to file')
argparser.add_argument('-l', '--list', action='store_true', help='Only show urls, do not probe')
args = argparser.parse_args()


def progress(done, total):
    ratio = done / total
    percentage = ratio * 100
    print(f'Request {done} of {total} ( {"%.2f" % percentage} % )', end='\r')
    # bar_length = 80
    # filled = ''.ljust(int(ratio * bar_length))
    # empty = ''.ljust(bar_length - len(filled))
    #
    # bar = f"|{style(filled, bg=colors.WHITE)}{empty}| {'%.2f' % percentage} % | Request {done} of {total}"
    # print(bar, end='\r')
    # print('', end='')


def https(target):
    if re.match('^https?://', target):
        return re.sub('^https?://', 'https://', target)
    else:
        return 'https://' + target


def get_redirects(response):
    if args.follow_redirects and len(response.history) > 0:
        redirects = 'REDIRECTS :\n' + '\n'.join([x.url for x in response.history])
        return redirects
    else:
        if str(response.status_code).startswith('3'):
            for header in response.headers:
                if header.lower() == 'location':
                    redirects = f'LOCATION : {response.headers["location"]}'
                    return redirects
        else:
            return ''


class Requester:
    def __init__(self):
        self.targets = [https(x.strip()) for x in set(sys.stdin.readlines())]
        self.assets = []

        self.REQ = {
            'get': requests.get,
            'post': requests.post,
            'head': requests.head,
            'delete': requests.delete,
            'put': requests.put,
            'options': requests.options
        }

    def probe(self, url):
        try: # HTTPS
            response = self.REQ[args.method.lower()](url,
                                                     allow_redirects=args.follow_redirects,
                                                     headers={x.split(':')[0]: ''.join(x.split(':')[1:]) for x in args.header} if args.header else {},
                                                     data=args.data,
                                                     timeout=(args.connect_timeout, args.read_timeout))
            asset = {
                'url': response.url,
                'status_code': response.status_code,
                'length': len(response.text),
                'redirects': get_redirects(response)
            }

            self.assets.append(asset)
            time.sleep(args.delay)
            return asset

        except:
            try: # HTTP
                response = self.REQ[args.method.lower()](re.sub('^https?://', 'http://', url),
                                                         allow_redirects=args.follow_redirects,
                                                         headers={x.split(':')[0]: ''.join(x.split(':')[1:]) for x in args.header} if args.header else {},
                                                         data=args.data,
                                                         timeout=(args.connect_timeout, args.read_timeout))
                asset = {
                    'url': response.url,
                    'status_code': response.status_code,
                    'length': len(response.text),
                    'redirects': get_redirects(response)
                }
                self.assets.append(asset)
                time.sleep(args.delay)
                return asset

            except Exception as e:
                err = 'timeout' if 'timeout' in str(e).lower() else 'X'
                asset = {
                    'url': url,
                    'status_code': err,
                    'length': err,
                    'redirects': err
                }
                self.assets.append(asset)
                time.sleep(args.delay)
                return asset

    def run(self):
        executor = ThreadPoolExecutor(max_workers=args.threads)
        threads = [executor.submit(self.probe, https(target)) for target in self.targets]

        i = 0
        for thread in as_completed(threads):
            i += 1
            progress(i, len(self.targets))

    def show_results(self):
        columns = [
            'url',
            'status_code',
            'length',
            'redirects',
        ]
        self.assets.sort(
            key=lambda a: (str(a['status_code']) == 'X', str(a['status_code']), str(a['length']))
        )
        results = pd.DataFrame(
                {column: [x[column] for x in self.assets] for column in columns}
        )
        table = tabulate(results, headers='keys', tablefmt='psql')
        if args.output_file:
            of = open(args.output_file, 'w')
            print(table, file=of)
            of.close()
        print(table)


def run():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    if args.list:
        for line in [line.strip() for line in sys.stdin.readlines()]:
            print(https(line))
    else:
        r = Requester()
        r.run()
        r.show_results()

if __name__ == '__main__':
    run()





