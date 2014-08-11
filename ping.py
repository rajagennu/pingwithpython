import httplib

def get_status_code(host, path="/"):
    try:
        connect = httplib.HTTPConnection(host)
        connect.request("HEAD", path)
        return connect.getresponse().status
    except StandardError:
        return None

if __name__ == '__main__':
    print get_status_code("google.com")
