import time
import matplotlib.pyplot as plt
import random


def measure_throughput(duration_seconds):
    """Measures throughput (packets/second or bits/second)."""

    start_time = time.time()
    packets_sent = 0  # Replace with your actual packet sending logic
    bytes_sent = 0 # keep track of the amount of data sent
    while time.time() - start_time < duration_seconds:
        # Simulate sending packets (REPLACE THIS WITH YOUR ACTUAL SENDING CODE)
        packet_size = random.randint(64, 1500)  # Example packet size, replace with RFC2544
        bytes_sent += packet_size
        packets_sent += 1
        time.sleep(0.001) # simulate some processing time

    elapsed_time = time.time() - start_time
    throughput_bps = (bytes_sent * 8) / elapsed_time  # bits per second
    throughput_pps = packets_sent / elapsed_time # packets per second
    return throughput_bps, throughput_pps


def measure_latency(num_packets):
    """Measures latency (round-trip time)."""

    latencies = []
    for _ in range(num_packets):
        # Simulate sending and receiving a packet (REPLACE WITH YOUR ACTUAL CODE)
        start_time = time.time()

        # Simulate packet send/receive (replace with your actual send/receive)
        time.sleep(0.01)  # Simulate some network delay

        end_time = time.time()
        latency = (end_time - start_time) * 1000  # in milliseconds
        latencies.append(latency)

    average_latency = sum(latencies) / len(latencies) if latencies else 0
    return average_latency, latencies



# --- Main Script ---
test_duration = 10  # seconds
throughput_bps_values = []
throughput_pps_values = []
latency_values = []
time_points = []

for i in range(1,6):  # Example: Run tests in 10-second intervals for 5 times.
    print(f"Running test {i}...")

    throughput_bps, throughput_pps = measure_throughput(test_duration)
    average_latency, latencies = measure_latency(100)  # Send 100 packets for latency test

    throughput_bps_values.append(throughput_bps)
    throughput_pps_values.append(throughput_pps)
    latency_values.append(average_latency)
    time_points.append(i * test_duration) # record the time in seconds


    print(f"  Throughput (bps): {throughput_bps:.2f}")
    print(f"  Throughput (pps): {throughput_pps:.2f}")
    print(f"  Average Latency: {average_latency:.2f} ms")
    print("-" * 20)

# --- Plotting ---
plt.figure(figsize=(12, 6))

# Throughput (bps)
plt.subplot(2, 1, 1)
plt.plot(time_points, throughput_bps_values, marker='o')
plt.xlabel("Time (seconds)")
plt.ylabel("Throughput (bps)")
plt.title("Throughput")
plt.grid(True)

# Latency
plt.subplot(2, 1, 2)
plt.plot(time_points, latency_values, marker='o', color='orange')
plt.xlabel("Time (seconds)")
plt.ylabel("Average Latency (ms)")
plt.title("Latency")
plt.grid(True)

plt.tight_layout()
plt.show()


# Example of plotting individual latency values.
# plt.figure()
# plt.plot(range(len(latencies)), latencies, marker='o')
# plt.xlabel("Packet")
# plt.ylabel("Latency (ms)")
# plt.title("Individual Latency Values")
# plt.grid(True)
# plt.show()
