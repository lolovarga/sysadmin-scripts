import getopt
import sys
import requests

def parse_args(argv):
    try:
        opts, args = getopt.getopt(argv, "u", ["url"])
    except getopt.GetoptError:
        print 'url_redirect -u <url>'
        sys.exit(1)
    if not len(opts) == 1:
        print 'url_redirect -u <url>'
        sys.exit(1)
    return args[0]

def check_redirect(url):
    try:
        r = requests.get(url, allow_redirects=False, timeout=0.5)
        if 300 <= r.status_code < 400:
            return r.headers['location']
        else:
            return '[no redirect]'
    except Exception, ex:
        print ex.message
        sys.exit(1)

if __name__ == '__main__':
    url = parse_args(sys.argv[1:])
    redirect = check_redirect(url)
    print redirect

