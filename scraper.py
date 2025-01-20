import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from datetime import datetime
import pytz
import time

def tennis(input_time_wd,input_time_web_wd,input_time_we,input_time_web_we,email_,password_):
    jakarta_tz = pytz.timezone("Asia/Jakarta")
    current_date = datetime.now()
    fd=datetime.now() + timedelta(days=4)
    future_date = (datetime.now() + timedelta(days=4)).strftime("%Y-%m-%d")
     
    if fd.weekday() < 5:   
        input_time=input_time_wd
        input_time_web=input_time_web_wd
    else:
        input_time=input_time_we
        input_time_web=input_time_web_we


    email=email_
    password=password_
    crt='373'
    print(f'starting func {email} {crt}')

    session = requests.Session()
    url='https://eliteclub.saraga.id/'
    resp=session.get(url)
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    url='https://eliteclub.saraga.id/login'
    payload={
        '_token': csrf_token,
        'email': email,
        'password': password
    }
    headers={
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0',
    }
    resp=session.post(url, data=payload, headers=headers )
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']


    payload={
        "input_date": str(future_date),
        "input_time": input_time,
        "duration": 1,
        "_token": xsrf_token,
    }

    url_get=f'https://eliteclub.saraga.id/court?input-date={future_date}&input-time={input_time_web}&input-duration=1&_token={xsrf_token}'
    resp=session.get(url_get, data=payload )
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    ###################################
    stop_flag = False
    while not stop_flag:
        now = datetime.now(jakarta_tz)
        if now.hour == 6 and now.minute == 00:
       

            url = "https://eliteclub.saraga.id/booking/confirmation"
            headers = {
                'authority': 'eliteclub.saraga.id',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-encoding': 'gzip, deflate, br, zstd',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0',
                'origin': 'https://eliteclub.saraga.id',
                'priority': 'u=0, i',
                'referer': url_get,
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',

            }

            # Payload for the POST request
            payload = {
                "_token": csrf_token ,
                "slug": "elite-club-epicentrum",
                "court_id": crt,
                "input_date": future_date,
                "input_time": input_time,  # JSON array as a string
                "duration": 1
            }

            # Send POST request
            resp = session.post(url, data=payload, headers=headers)
            xsrf_token = resp.cookies.get("XSRF-TOKEN")
            saraga_session = resp.cookies.get("saraga_indonesia_v2_session")

            url='https://eliteclub.saraga.id/booking/process_booking'
            headers={
                'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0'
            }
            payload={
                '_token': csrf_token,
                'voucher_code':'',
                'total': 1,
                'grand_total': 1,
                'promo_discount': 0,
                'agreements': 'confirm'
            }
            resp = session.post(url, data=payload, headers=headers, allow_redirects=False)
            endmessage=(f'{email} is done court {crt}')
            print(endmessage)
            stop_flag = True
        else:
            time.sleep(0.3)

    crt='372'
    print(f'starting func {email}  {crt}')
    session = requests.Session()
    url='https://eliteclub.saraga.id/'
    resp=session.get(url)
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    url='https://eliteclub.saraga.id/login'
    payload={
        '_token': csrf_token,
        'email': email,
        'password': password
    }
    headers={
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0',
    }
    resp=session.post(url, data=payload, headers=headers )
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    payload={
        "input_date": str(future_date),
        "input_time": input_time,
        "duration": 1,
        "_token": xsrf_token,
    }

    url_get=f'https://eliteclub.saraga.id/court?input-date={future_date}&input-time={input_time_web}&input-duration=1&_token={xsrf_token}'
    resp=session.get(url_get, data=payload )
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    url = "https://eliteclub.saraga.id/booking/confirmation"
    headers = {
        'authority': 'eliteclub.saraga.id',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0',
        'origin': 'https://eliteclub.saraga.id',
        'priority': 'u=0, i',
        'referer': url_get,
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',

    }

    # Payload for the POST request
    payload = {
        "_token": csrf_token ,
        "slug": "elite-club-epicentrum",
        "court_id": crt,
        "input_date": future_date,
        "input_time": input_time,  # JSON array as a string
        "duration": 1
    }

    # Send POST request
    resp = session.post(url, data=payload, headers=headers)
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")

    url='https://eliteclub.saraga.id/booking/process_booking'
    headers={
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0'
    }
    payload={
        '_token': csrf_token,
        'voucher_code':'',
        'total': 1,
        'grand_total': 1,
        'promo_discount': 0,
        'agreements': 'confirm'
    }
    resp = session.post(url, data=payload, headers=headers, allow_redirects=False)
    endmessage=(f'{email} is done court {crt}')
    print(endmessage)

    crt='371'
    print(f'starting func {email}  {crt}')
    session = requests.Session()
    url='https://eliteclub.saraga.id/'
    resp=session.get(url)
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    url='https://eliteclub.saraga.id/login'
    payload={
        '_token': csrf_token,
        'email': email,
        'password': password
    }
    headers={
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0',
    }
    resp=session.post(url, data=payload, headers=headers )
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    payload={
        "input_date": str(future_date),
        "input_time": input_time,
        "duration": 1,
        "_token": xsrf_token,
    }

    url_get=f'https://eliteclub.saraga.id/court?input-date={future_date}&input-time={input_time_web}&input-duration=1&_token={xsrf_token}'
    resp=session.get(url_get, data=payload )
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

    url = "https://eliteclub.saraga.id/booking/confirmation"
    headers = {
        'authority': 'eliteclub.saraga.id',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0',
        'origin': 'https://eliteclub.saraga.id',
        'priority': 'u=0, i',
        'referer': url_get,
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',

    }

    # Payload for the POST request
    payload = {
        "_token": csrf_token ,
        "slug": "elite-club-epicentrum",
        "court_id": crt,
        "input_date": future_date,
        "input_time": input_time,  # JSON array as a string
        "duration": 1
    }

    # Send POST request
    resp = session.post(url, data=payload, headers=headers)
    xsrf_token = resp.cookies.get("XSRF-TOKEN")
    saraga_session = resp.cookies.get("saraga_indonesia_v2_session")

    url='https://eliteclub.saraga.id/booking/process_booking'
    headers={
        'cookie':f'_ga=GA1.1.1130634456.1733094184; _ga_6XEBMB0P4T=GS1.1.1733094189.1.1.1733094232.0.0.0; XSRF-TOKEN={xsrf_token}; saraga_indonesia_v2_session={saraga_session}; _ga_D58QK6QGM7=GS1.1.1733094184.1.1.1733098679.0.0.0'
    }
    payload={
        '_token': csrf_token,
        'voucher_code':'',
        'total': 1,
        'grand_total': 1,
        'promo_discount': 0,
        'agreements': 'confirm'
    }
    resp = session.post(url, data=payload, headers=headers, allow_redirects=False)
    endmessage=(f'{email} is done court {crt}')
    print(endmessage)

 
