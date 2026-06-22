from scapy.all import sniff, IP
from collections import Counter
from alerts import check_packet

def capture_features(packet_limit=100):

    packet_count = 0
    total_size = 0

    protocol_counter = Counter()
    destination_ips = set()

    alerts_found = []

    def process_packet(packet):

        nonlocal packet_count
        nonlocal total_size

        if IP in packet:

            src_ip = packet[IP].src

            packet_count += 1
            total_size += len(packet)

            protocol_counter[packet[IP].proto] += 1

            destination_ips.add(
                packet[IP].dst
            )

            alerts_found.extend(
                check_packet(src_ip)
            )

    sniff(
        prn=process_packet,
        count=packet_limit,
        store=False
    )

    avg_packet_size = (
        total_size / packet_count
        if packet_count > 0
        else 0
    )

    features = [
        packet_count,
        avg_packet_size,
        protocol_counter[6],   # TCP
        protocol_counter[17],  # UDP
        len(destination_ips)
    ]

    return features, list(set(alerts_found))