# probe_request.py

from scapy.all import RadioTap, Dot11, Dot11ProbeReq, sendp

def send_probe_request(interface, ssid=""):
    """
    Sends a probe request to discover available networks.
    :param interface: The network interface in monitor mode.
    :param ssid: SSID to probe (optional, empty for broadcast).
    """
    try:
        # Constructing a probe request
        dot11 = Dot11(type=0, subtype=4, addr1="ff:ff:ff:ff:ff:ff", addr2="00:11:22:33:44:55", addr3="ff:ff:ff:ff:ff:ff")
        probe_req = RadioTap() / dot11 / Dot11ProbeReq() / (ssid.encode() if ssid else b"")
        
        # Sending the probe request
        sendp(probe_req, iface=interface, verbose=False)
        print(f"Probe request sent on interface {interface} for SSID '{ssid or 'broadcast'}'")
    except Exception as e:
        print(f"Error sending probe request: {e}")
