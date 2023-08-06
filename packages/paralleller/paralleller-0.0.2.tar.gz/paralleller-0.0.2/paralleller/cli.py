import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Liquidity provider portfolio stats.")
    parser.add_argument("address", help="Address")
    args = parser.parse_args()
    address = args.address
    data = print(address)
    print(data)
    return data

if __name__ == "__main__":
    main()