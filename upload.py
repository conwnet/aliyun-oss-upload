import requests, os

# the path is described remote server
def upload(path, f):
    data = {
        'OSSAccessKeyId': 'LTAIwasl36taM034',
        'policy': 'eyJleHBpcmF0aW9uIjoiMjExNS0wMS0yN1QxMDo1NjoxOVoiLCJjb25kaXRpb25zIjpbWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDEwNDg1NzZdXX0=',
        'Signature': 'rLe0oddE+s2QYSPn6Ym9c3ZLc9w=',
        'key': os.path.join(path, '${filename}'),
        'success_action_redirect': 'http://conw.net',
        'success_action_status': '201',
        'submit': 'Upload'
    }
    files = {'file': f}
    try:
        res = requests.post('http://netcon.oss-cn-qingdao.aliyuncs.com', data, files=files)
        print(res.status_code)
        return res.ok
    except:
        #raise
        return False

def main(localpath):
    files = [filename for filename in os.listdir(localpath) if os.path.isfile(os.path.join(localpath, filename))]
    for filename in files:
        print(filename)
        with open(os.path.join(localpath, filename), 'rb') as f:
            upload('video', f)


if __name__ == '__main__':
    #main('/root/video')
    main('/var/www/html/video/11000')

