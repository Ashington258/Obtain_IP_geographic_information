import requests
import time
import logging
from configparser import ConfigParser

# 初始化日志记录器
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 读取配置文件
config = ConfigParser()
config.read('config.ini')

def get_ip_location(ip_address):
    """获取IP地址的地理位置信息"""
    try:
        response = requests.get(f"{config['API']['IP_INFO']}/{ip_address}/json")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"获取IP位置信息时出错: {e}")
        return None

def check_ip_security(ip_address):
    """检查IP地址的安全性"""
    # 示例功能，可以扩展为实际的安全检查
    return "Safe" if ip_address.startswith("192.") else "Unsafe"

def test_network_latency():
    """测试网络延迟"""
    try:
        start_time = time.time()
        requests.get(config['API']['PING_ENDPOINT'])
        return time.time() - start_time
    except requests.RequestException as e:
        logging.error(f"网络延迟测试失败: {e}")
        return None

def get_current_ip():
    """获取当前IP地址"""
    try:
        response = requests.get(config['API']['CURRENT_IP'])
        response.raise_for_status()
        return response.json().get("ip")
    except requests.RequestException as e:
        logging.error(f"获取当前IP地址时出错: {e}")
        return None

if __name__ == "__main__":
    while True:  # 添加无限循环
        ip_address = get_current_ip()
        if ip_address:
            logging.info(f"当前IP地址: {ip_address}")

            location_data = get_ip_location(ip_address)
            if location_data:
                logging.info(f"IP地址位置信息: {location_data}")

            security_status = check_ip_security(ip_address)
            logging.info(f"IP地址安全检查: {security_status}")

            latency = test_network_latency()
            if latency is not None:
                logging.info(f"网络延迟: {latency:.2f}秒")
        else:
            logging.error("无法获取当前IP地址。")
        print('----------------------------------------------------------------')
        time.sleep(2)  # 每60秒循环一次
