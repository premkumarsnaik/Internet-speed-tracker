import csv
import datetime
import os
import time
import speedtest

csv_filename = "speedtest_log.csv"
interval_seconds = 30  # Wait 30 seconds between tests
total_duration_seconds = 240 * 60  # Run for exactly 2 minutes total


def log_speed():
    st = speedtest.Speedtest()

    print("\nLocating optimal server...")
    st.get_best_server()

    print("Testing Download Speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    print("Testing Upload Speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    ping = st.results.ping
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_row = [
        timestamp,
        f"{download_speed:.2f}",
        f"{upload_speed:.2f}",
        f"{ping:.2f}",
    ]

    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(
                ["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"]
            )
        writer.writerow(data_row)

    print(
        f"[{timestamp}] Saved: Down: {download_speed:.2f} Mbps | Up: {upload_speed:.2f} Mbps | Ping: {ping:.2f} ms"
    )


# Execution Loop
start_time = time.time()
end_time = start_time + total_duration_seconds

print(
    f"Starting speed test. Data will append to '{csv_filename}' every 30 seconds for 2 minutes."
)

try:
    while time.time() < end_time:
        cycle_start = time.time()

        try:
            log_speed()
        except Exception as e:
            print(f"An error occurred during this test cycle: {e}")

        elapsed_in_cycle = time.time() - cycle_start
        sleep_time = max(0, interval_seconds - elapsed_in_cycle)

        if time.time() + sleep_time < end_time:
            time.sleep(sleep_time)
        else:
            break

    print("\n2-minute testing period completed successfully.")

except KeyboardInterrupt:
    print("\nSpeed test monitoring stopped manually.")
