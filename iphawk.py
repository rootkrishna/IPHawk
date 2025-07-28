# iphawk.py

import requests
import argparse
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(f"""
{Fore.RED}██████╗ ██╗██████╗ ██████╗ ██╗  ██╗ █████╗ ██╗  ██╗
{Fore.RED}██╔══██╗██║██╔══██╗██╔══██╗██║  ██║██╔══██╗██║ ██╔╝
{Fore.YELLOW}██████╔╝██║██████╔╝██████╔╝███████║███████║█████╔╝ 
{Fore.YELLOW}██╔═══╝ ██║██╔═══╝ ██╔═══╝ ██╔══██║██╔══██║██╔═██╗ 
{Fore.GREEN}██║     ██║██║     ██║     ██║  ██║██║  ██║██║  ██╗
{Fore.GREEN}╚═╝     ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
{Fore.CYAN}    IPHawk - Advanced IP Geolocation Tool by KRISHNA ⚡
    """)

def ip_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,isp,org,asname,query,timezone,lat,lon"
    try:
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'fail':
            print(f"{Fore.RED}[✘] Error: {data['message']}")
            return

        print(f"{Fore.CYAN}[✓] IP Info for {data['query']}\n")
        print(f"{Fore.GREEN}🌍 Continent   : {data['continent']}")
        print(f"🏳️ Country     : {data['country']}")
        print(f"🗺️ Region      : {data['regionName']}")
        print(f"🏙️ City        : {data['city']}")
        print(f"🌐 ISP         : {data['isp']}")
        print(f"🏢 Organization: {data['org']}")
        print(f"📡 ASN         : {data['asname']}")
        print(f"🕒 Timezone    : {data['timezone']}")
        print(f"📍 Location    : {data['lat']}, {data['lon']}")
    except Exception as e:
        print(f"{Fore.RED}[✘] Exception: {e}")

def main():
    parser = argparse.ArgumentParser(description="IPHawk - Advanced IP Tracker by KRISHNA")
    parser.add_argument("-i", "--ip", required=True, help="Target IP address")
    args = parser.parse_args()

    banner()
    time.sleep(0.5)
    ip_lookup(args.ip)

if __name__ == "__main__":
    main()
