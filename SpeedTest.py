import speedtest

def test_speed():
    st = speedtest.Speedtest()
    
    print("正在选择最佳服务器...")
    st.get_best_server()
    
    print("正在测试下载速度...")
    download_speed = st.download() / 10**6  # Convert to Mbps
    print(f"下载速度: {download_speed:.2f} Mbps")
    
    print("正在测试上传速度...")
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    print(f"上传速度: {upload_speed:.2f} Mbps")
    
    print("正在测试延迟...")
    ping = st.results.ping
    print(f"延迟: {ping} ms")
    
    print("正在进行网络详细测试...")
    st.get_best_server()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    ping = st.results.ping
    jitter = st.results.jitter
    packet_loss = st.results.packet_loss
    
    print("测试结果：")
    print(f"下载速度: {download_speed:.2f} Mbps")
    print(f"上传速度: {upload_speed:.2f} Mbps")
    print(f"延迟: {ping} ms")
    print(f"抖动（Jitter）: {jitter} ms")
    print(f"丢包率: {packet_loss}%")

if __name__ == "__main__":
    test_speed()

##国内使用Clash链接时似乎无法进行测试，无法连接到speedtest.net服务，原因未知