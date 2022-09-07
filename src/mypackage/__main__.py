import mypackage


def main():
    """Entry point of the package"""
    print(f"Hello world from {mypackage.__name__} ({mypackage.__doc__})")


if __name__ == "__main__":
    main()
