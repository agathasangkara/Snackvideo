import requests, sys, os, json, re
import random, string
from datetime import datetime, time

def claim_snack(serial, os_version, token, url):
    headers = {}
    headers['Accept'] = 'application/json, text/plain, /'
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 Yoda/2.8.5 ISDR/0 Kwai_Pro/7.1.30.529405 NetScore/43 NST/F deviceScore/-1 webviewPreloaded/false WebViewPreAlloc/0 StatusHT/29 TitleHT/50 preload_api/1 NetType/LTE ISLP/0 ISDM/0 ISLB/0 locale/in-id evaSupported/false'
    headers['Accept-Encoding'] = 'gzip, deflate'
    headers['Accept-Language'] = 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'
    headers['Cookie'] = 'did=ANDROID_{0};c=GOOGLE_PLAY;ver=6.1;appver=6.1.30.529405;language=in-id;countryCode=ID;sys=KWAI_BULLDOG_ANDROID_{1};token={2}'.format(serial, os_version, token)
    
	#remove from preview
    
    response = requests.post(url, headers = headers, data = data)
    return json.loads(response.text)

def generate_serial(length=16):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


while True:
	cookies = input(" > Data cookies : ").strip()
	os.system('cls' if os.name == 'nt' else 'clear')
	print("░█▀▀░█▀█░█▀█░█▀▀░█░█\n░▀▀█░█░█░█▀█░█░░░█▀▄\n░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀")
	if "token" in cookies:
		serial = generate_serial()
		os_version = random.randint(4, 13)
		
		#remove from preview
		
		print ("\n > Grabber account succesfully, trying claim")
		break
	else:
		sys.exit(" > Data cookies wrong\n")

now = datetime.now()
date = now.strftime('%H:%M')
while True:
    #remove from preview
        break
    else:
        continue

url = ""
result = claim_snack(serial, os_version, token, url)
#remove from preview


