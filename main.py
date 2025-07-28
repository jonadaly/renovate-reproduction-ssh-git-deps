import httpx
import requests

def main():
    print("Hello from renovate-reproduction-ssh-git-deps!")
    print(httpx.__version__)
    print(requests.__version__)


if __name__ == "__main__":
    main()
