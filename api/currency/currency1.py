import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=34119a0aaa3d3af1b32259d9c6ec1b15&base=EUR&symbols=JPY")

    data = res.json()

    if data["success"] != True:
        raise Exception("Error: API request unsuccessful")

    rate = data["rates"]["JPY"]
    print(f"1 EUR is equal to {rate} JPY")

if __name__ == "__main__":
    main()