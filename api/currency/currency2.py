import requests

def main():
    base = "EUR"
    symbols = input("Second Currency: ")

    res = requests.get("http://data.fixer.io/api/latest?access_key=34119a0aaa3d3af1b32259d9c6ec1b15",
                        params={"base": base, "symbols": symbols})

    data = res.json()

    if data["success"] != True:
        raise Exception("Error: API request unsuccessful")

    rate = data["rates"][symbols]
    print(f"1 {base} is equal to {rate} {symbols}")

if __name__ == "__main__":
    main()