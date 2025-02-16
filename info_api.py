# API & CODED BY SHAH MAKHDUM SHAJON
# GitHub : github.com/SHAJON-404
# TELEGRAM : t.me/SHAJON404_OFFICIAL
# FIXED BANGLA PROFILE NAME PROBLEM
# FIXED JAVASCRIPT ERROR PROBLEM

import requests
import json

cookies = {
    '__test': '76788fa900c30f7f1bdd40b0f032cfbf',
    'Lda_aKUr6BGRn': 'hipodi.com/r/v2?',
    'Lda_aKUr6BGRr': '0',
    'Fm_kZf8ZQvmX': '1',
    'Ac_aqK8DtrDS': '6',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ru;q=0.6,ar;q=0.5,bn;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

xd_url = 'https://www.facebook.com/profile.php?id=100075702605787'

response = requests.get(
    f'http://shajon404.rf.gd/info_api.php?api_key=trial&fb_url={xd_url}',
    cookies=cookies,
    headers=headers,
    verify=False,
).text

data = json.loads(response)

decoded_response = json.dumps(data, ensure_ascii=False, indent=4)

print(decoded_response)
