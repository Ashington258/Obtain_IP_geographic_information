import requests
import time

def get_ip_location(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        return data
    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    while True:
        # 获取当前IP地址
        response = requests.get("https://api64.ipify.org?format=json")
        ip_data = response.json()
        ip_address = ip_data["ip"]

        # 获取IP地址所在的位置信息
        location_data = get_ip_location(ip_address)

        if location_data:
            print("Location information for IP address:", ip_address)
            print("IP:", location_data.get("ip"))
            print("Hostname:", location_data.get("hostname", "N/A"))
            print("City:", location_data.get("city", "N/A"))
            print("Region:", location_data.get("region", "N/A"))
            print("Country:", location_data.get("country", "N/A"))
            print("Location:", location_data.get("loc", "N/A"))
            print("Organization:", location_data.get("org", "N/A"))
        else:
            print("Unable to retrieve location information.")
        
        # 等待1秒
        time.sleep(1)
