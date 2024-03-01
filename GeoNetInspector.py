import requests
import time
import logging

# 初始化日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# 内嵌配置
API_ENDPOINTS = {
    "IP_INFO": "https://ipinfo.io",
    "CURRENT_IP": "https://api64.ipify.org?format=json",
    "PING_ENDPOINT": "http://www.google.com"
}

def get_ip_location(ip_address):
    """获取IP地址的地理位置信息"""
    try:
        response = requests.get(f"{API_ENDPOINTS['IP_INFO']}/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        return {k: data.get(k, 'N/A') for k in ['ip', 'hostname', 'city', 'region', 'country', 'loc', 'org']}
    except requests.RequestException as e:
        logging.error(f"获取IP位置信息时出错: {e}")
        return None

def check_ip_security(ip_address):
    """检查IP地址的安全性"""
    return "Safe" if ip_address.startswith("192.") else "Unsafe"

def test_network_latency():
    """
    Tests the network latency by making an HTTP GET request to a known endpoint and measuring the time it takes to receive a response.

    Returns:
        The network latency, or None if the test failed.
    """
    try:
        start_time = time.time()
        requests.get(API_ENDPOINTS['PING_ENDPOINT'])
        return time.time() - start_time
    except requests.RequestException as e:
        logging.error(f"Network latency test failed: {e}")
        return None

def get_current_ip() -> str:
    """
    This function uses the requests library to make an HTTP GET request to the
    API endpoint 'https://api64.ipify.org?format=json' and returns the IP address
    as a string. If the request fails, the function logs the error using the
    logging module and returns None.
    """
    try:
        response = requests.get(API_ENDPOINTS['CURRENT_IP'])
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        logging.error(f"Error getting current IP: {e}")
        return None

def print_location_data(location_data: dict):
    """
    This function prints the location data in a readable format.

    Args:
        location_data (dict): The location data to be printed.

    Returns:
        None

    """
    for key, value in location_data.items():
        logging.info(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    while True:
        ip_address = get_current_ip()
        if ip_address:
            logging.info("当前IP地址信息:")
            logging.info(f"IP地址: {ip_address}")
            print()

            location_data = get_ip_location(ip_address)
            if location_data:
                logging.info("IP地址位置信息:")
                print_location_data(location_data)
                print()

            security_status = check_ip_security(ip_address)
            logging.info(f"IP地址安全检查: {security_status}")
            print()

            latency = test_network_latency()
            if latency is not None:
                logging.info(f"网络延迟: {latency:.2f}秒")
                print()
        else:
            logging.error("无法获取当前IP地址。")

        print('----------------------------------------------------------------')
        time.sleep(2)
