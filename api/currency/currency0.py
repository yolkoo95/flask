import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?base=USD&symbols=EUR")

    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful!")

    data = res.json()
    print(data)

if __name__ == "__main__":
    main()