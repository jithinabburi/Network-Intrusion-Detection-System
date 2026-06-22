from collections import defaultdict

ip_counter = defaultdict(int)

PACKET_THRESHOLD = 50

def check_packet(src_ip):

    alerts = []

    ip_counter[src_ip] += 1

    if ip_counter[src_ip] > PACKET_THRESHOLD:

        alerts.append(
            f"⚠ High Traffic From {src_ip}"
        )

    return alerts