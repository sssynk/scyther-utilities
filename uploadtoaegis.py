from time import sleep
import requests
import json

def process_file_and_send_requests(source_file_path, url):
    try:
        with open(source_file_path, 'r') as source_file:
            lines = source_file.readlines()

        for index, line in enumerate(lines):
            if len(line) >= 16:
                username = line[:15].strip()
                password = line[16:].strip()
            else:
                print(f"Line {index + 1} is too short to process.")
                continue

            payload = {
                "accounts": [
                {
                    "password": password,
                    "username": username,
                }
                ],
                "default_level": 0
            }

            #response = requests.post(url, json=payload) with header
            response = requests.post(url, json=payload)


            print("user: "+ username)
            print("pass: "+ password)

            if response.status_code == 202:
                print(f"Successfully processed line {index + 1}.")
            else:
                print(f"Failed to process line {index + 1}. HTTP Status Code: {response.status_code}")

    except FileNotFoundError:
        print("File not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file_path = 'accounts.txt'
url = 'http://192.168.1.150:6010/accounts/'

process_file_and_send_requests(source_file_path, url)
