import netifaces

eth0_interface = "eth0"
fallback = "0.0.0.0"


def get_ip_address() -> str:
    try:
        addresses = netifaces.ifaddresses(eth0_interface)
        if addresses is None or len(addresses) == 0:
            return fallback
        af_inet = addresses[netifaces.AF_INET]
        if af_inet is None or len(af_inet) == 0:
            return fallback
        ip_address = af_inet[0].get('addr')
        if ip_address is None:
            return fallback
        return ip_address
    except ValueError:
        return fallback
