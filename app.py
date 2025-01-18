import requests
import json
import time
import datetime
import smtp
import os
from dotenv import load_dotenv

load_dotenv()
authorization_token = os.getenv("AUTHORIZATION_TOKEN")
departureStationId = os.getenv("departureStationId")
departureStationName = os.getenv("departureStationName")
arrivalStationId = os.getenv("arrivalStationId")
arrivalStationName = os.getenv("arrivalStationName")
departureDate = os.getenv("departureDate")
url = "https://web-api-prod-ytp.tcddtasimacilik.gov.tr/tms/train/train-availability?environment=dev&userId=1"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "tr",
    "Authorization": f"Bearer {authorization_token}",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ebilet.tcddtasimacilik.gov.tr",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "unit-id": "3895",
}

payload = {
    "searchRoutes": [
        {
            "departureStationId": departureStationId, 
            "departureStationName": departureStationName, 
            "arrivalStationId": arrivalStationId, 
            "arrivalStationName": arrivalStationName,
            "departureDate": departureDate,
        }
    ],
    "passengerTypeCounts": [{"id": 0, "count": 1}],
    "searchReservation": False,
}

train_id_str = os.getenv("train_id")
env_train_id = list(map(int, train_id_str.split(',')))
env_cabin_name = os.getenv("cabin_name")
while True:
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            trains = [
                train
                for leg in response_data.get('trainLegs', [])
                for availability in leg.get('trainAvailabilities', [])
                for train in availability.get('trains', [])
                if train.get('id') in env_train_id 
            ]
            for train in trains:
                cabin_classes = train.get('cabinClassAvailabilities', [])
                if cabin_classes:
                    for cabin_class in cabin_classes:
                        cabin_name = cabin_class.get('cabinClass', {}).get('name')
                        availability_count = cabin_class.get('availabilityCount', 0)
                        print(train.get('id'),cabin_name, availability_count)
                        if cabin_name == env_cabin_name:
                            smtp.send_mail()
                            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            entry = {
                                "train_id": train.get('id'),
                                "cabin_name": cabin_name,
                                "datetime": current_time,
                                "availability_count": availability_count
                            }
                            print(entry)
                            with open("train_availability.json", "a", encoding='utf-8') as file:
                                file.write(json.dumps(entry, ensure_ascii=False) + "\n")
                else:
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    entry = {
                        "train_id": train.get('id'),
                        "cabin_name": None,
                        "datetime": current_time,
                        "availability_count": 0
                    }
                    print(entry)
                    with open("train_availability.json", "a", encoding='utf-8') as file:
                        file.write(json.dumps(entry, ensure_ascii=False) + "\n")
        else:
            print(f"Received status code: {response.status_code}")
        time.sleep(20)
    except requests.exceptions.RequestException as e:
        print(f"Request failed with error: {e}")
        time.sleep(20)
