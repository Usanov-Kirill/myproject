import requests

def get_sov():
    r = requests.get("https://api.adviceslip.com/advice", timeout=5)
    r.raise_for_status()
    data = r.json()
    print(data["slip"]["advice"])


if __name__ == "__main__":
    # 1
    get_sov()
