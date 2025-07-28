# iphawk.py
import requests
import argparse
import time
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.RED}
  ██╗██████╗ ██╗  ██╗ █████╗ ██╗    ██╗
 ██╔╝██╔══██╗██║  ██║██╔══██╗██║    ██║
██╔╝ ██████╔╝███████║███████║██║ █╗ ██║
╚██╗██╔═══╝ ██╔══██║██╔══██║██║███╗██║
 ╚██╗██║     ██║  ██║██║  ██║╚███╔███╔╝
  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝
      {Fore.YELLOW}IP TRACE TOOL BY KRISHNA ⚡
"""

def ip_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,isp,org,asname,query,timezone,lat,lon"
    try:
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'fail':
            print(f"{Fore.RED}[!] Error: {data['message']}")
            return
        print(f"{Fore.CYAN}[✓] Found Data for IP: {ip}\n")
        print(f"{Fore.GREEN}IP: {data['query']}")
        print(f"Continent: {data['continent']}")
        print(f"Country: {data['country']}")
        print(f"Region: {data['regionName']}")
        print(f"City: {data['city']}")
        print(f"Latitude: {data['lat']} | Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"Organization: {data['org']}")
        print(f"ASN Name: {data['asname']}")
    except Exception as e:
        print(f"{Fore.RED}[!] Exception: {e}")

def main():
    parser = argparse.ArgumentParser(description="IPHawk - IP Info & GeoLocation Tool by KRISHNA")
    parser.add_argument('-i', '--ip', required=True, help="IP address to scan")
    args = parser.parse_args()

    print(BANNER)
    time.sleep(0.8)
    ip_lookup(args.ip)

if __name__ == "__main__":
    main()
