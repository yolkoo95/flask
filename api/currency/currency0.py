import requests

def main():
    # due to our privileges, the base can be only EUR
    res = requests.get("http://data.fixer.io/api/latest?access_key=34119a0aaa3d3af1b32259d9c6ec1b15&base=JPY&symbols=USD")

    data = res.json()
    
    if data["success"] != True:
        raise Exception("Error: API request unsuccessful")

    print(data)

if __name__ == "__main__":
    main()