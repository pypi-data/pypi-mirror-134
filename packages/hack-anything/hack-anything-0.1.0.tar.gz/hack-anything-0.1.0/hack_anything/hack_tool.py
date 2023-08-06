import time
from tqdm import tqdm
import base64
from colorama import Fore


def hack(info):
    assert isinstance(info, str)
    print(Fore.GREEN + f".....encrypted Name:{base64.b64encode(info.encode('ascii'))}")
    time.sleep(2)
    print(Fore.GREEN + ".....Fetching Info")
    time.sleep(3)
    text_list = ["============>establishing ssh connection","====>Decrypting data",
                 "============>scanning system files", "=======>forwarding request", "========>fetching active port",
                 "==============>Defalut protocol exists"]
    print("........termination protection disabled")
    print(Fore.GREEN + "Private IP DNS name"+" ---->***********")
    for i in text_list:
        print(Fore.GREEN + "======="+i)
        time.sleep(2)
    print(Fore.GREEN + "================>Deactivating Firewall")
    for _ in tqdm(range(20)):
        time.sleep(1)
    time.sleep(3)
    print(Fore.LIGHTGREEN_EX + f"'{info.upper()}' hacked successfully")


if __name__ == "__main__":
    hack(info="NASA")
