import requests
import soup

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' 
    }

for page in range(1):
    try:
        response = requests.get('https://www.qgsydw.com/qgsydwzp/ksbm/zwsearch.dox', 
            params={'keywords' : '', 'selectgws' : '1', 'p': page}, headers = headers)
        response.encoding = "GB2312"
        response.raise_for_status()
        soup.handleResponse(response.text)
    except requests.RequestException as ex:
        print('response status_code not as expected: ' + response.url, sep='\n')