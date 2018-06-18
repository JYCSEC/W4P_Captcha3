import requests, webbrowser, urllib2, urllib, webbrowser
#This was a pain...

if __name__ == '__main__':
    url = 'http://192.168.159.131/captcha/example3/'
    req = requests.get(url)
    c = req.cookies
    v = c.items()
    opener = urllib2.build_opener()
    for val in v:
        s = str(val)
        string = s[13:-2]
    print string
    url = url + "submit?captcha="+string+"&submit=Submit+Query"
    req = requests.get(url,cookies=c)
    opener.addheaders.append(('Cookie','captcha='+string))
    print req
    print opener.open(url).read()
