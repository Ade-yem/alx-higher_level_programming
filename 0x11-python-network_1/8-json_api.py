#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    r = requests.post(url, data={'q': letter})
    try:
        data = r.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
