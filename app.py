import requests


def get_sov():
    r = requests.get("https://api.adviceslip.com/advice", timeout=5)
    r.raise_for_status()
    data = r.json()
    print(data["slip"]["advice"])

def get_soviets():
    with Session() as s:
        advices = []
        for _ in range(3):
            r = s.get("https://api.adviceslip.com/advice", timeout=5)
            r.raise_for_status()
            advices.append(r.json()["slip"]["advice"]["status_code"])
        print("\n".join(advices))

if __name__ == "__main__":
    #1
    get_sov()

    #2
    get_soviets()

