#!/usr/bin/python3
""" `4-hbtn_status.py` fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {type(r.text)}")
    print("\t- content: {r.text}")
