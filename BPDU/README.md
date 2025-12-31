Scapy STP – BPDU Injection Lab

Overview

This project demonstrates how Spanning Tree Protocol (STP) behaves under normal conditions and how it can be manipulated by injecting crafted BPDUs using Scapy.
The goal of this lab is to understand:
STP root bridge election
Port roles and states
How malicious or rogue BPDUs can influence topology decisions
This is a learning-focused lab, built to explore protocol behavior rather than exploit real networks.

Topology

The lab consists of multiple switches connected in a Layer 2 topology.
Normal STP Operation
Root bridge is elected based on Bridge ID (BID)
Port roles (Root, Designated, Blocking) are stable
Traffic flows as expected

📷 Image:
images/topology_normal.png
(Shows BIDs and port roles under normal STP operation)
STP Under BPDU Injection
In this scenario, crafted BPDUs are sent from a host using Scapy.

Effects observed:
Root bridge election changes
Port roles are recalculated
Previously forwarding ports may move to blocking state

📷 Image:
images/topology_attack.png
(Shows changed port roles after BPDU injection)
BPDU Generation with Scapy
A Python script is used to manually construct and send STP BPDUs.
This helps in understanding:
BPDU structure
How switches trust received BPDUs
Why features like BPDU Guard and Root Guard are important

📷 Image:
images/bpdu_sender.png
(Terminal showing BPDU transmission using Scapy)

Tools Used
Scapy (Python)
Linux
Virtual / Lab-based switches
Wireshark (for verification)

Author

Built as part of hands-on networking and protocol analysis practice.This is a read me file
