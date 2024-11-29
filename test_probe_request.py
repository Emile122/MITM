# test_probe_request.py

from probe_request import send_probe_request

def test_send_probe_request():
    """
    Test sending a probe request. This assumes a valid monitor mode interface.
    """
    test_interface = "mon1"  # Change this to your monitor mode interface
    test_ssid = "TestSSID"
    
    try:
        send_probe_request(test_interface, test_ssid)
        print("Probe request test completed successfully.")
    except Exception as e:
        print(f"Probe request test failed: {e}")
