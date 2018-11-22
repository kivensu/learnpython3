import socket


def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host name: " + host_name)
    print("IP address: " + ip_address)


if __name__ == '__main__':
    print_machine_info()


def get_remote_machine_info():
    remote_host = "www.geek-zoo.com"
    try:
        remote_host_ip = socket.gethostbyname(remote_host)
    except socket.error:
        print("remote host error!")
    else:
        print("IP address of " + remote_host + " : " + remote_host_ip)


if __name__ == '__main__':
    get_remote_machine_info()
