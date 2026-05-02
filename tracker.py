import csv
import datetime
import os
import random
import time
import speedtest

# Configuration
csv_filename = "speedtest_log.csv"
interval_seconds = 30  # Wait exactly 30 seconds between cycles
total_duration_seconds = 0.04 * 60 * 60  # Run for 4 hours total (14,400 seconds)


def log_speed(st):
    try:
        # Step 1: Fetch the closest servers
        print("\nFetching nearby servers...")
        servers = st.get_servers()

        # Flatten the dictionary into a list of available test servers
        server_list = [
            server for sublist in servers.values() for server in sublist
        ]

        # Select randomly from the top 5 closest servers to avoid hammering the same one
        chosen_server = random.choice(server_list[:5])
        print(
            f"Testing against server: {chosen_server['sponsor']} in {chosen_server['name']}"
        )

        # Assign the selected server to the client
        st.get_best_server([chosen_server])

        print("Testing Download Speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps

        print("Testing Upload Speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps

        ping = st.results.ping
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Format data for CSV
        data_row = [
            timestamp,
            f"{download_speed:.2f}",
            f"{upload_speed:.2f}",
            f"{ping:.2f}",
        ]

        # Step 2: Check if CSV file exists and append the new results
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

    except Exception as e:
        # Gracefully handle server-side errors or temporary timeouts without stopping the loop
        print(f"An error occurred during this test cycle: {e}")


# --- Execution Flow ---

# Initialize the persistent client once before entering the loop
print("Initializing persistent Speedtest client...")
try:
    st_client = speedtest.Speedtest(secure=True)
except Exception as e:
    print(
        f"Failed to initialize client. Please check your internet connection: {e}"
    )
    exit(1)

start_time = time.time()
end_time = start_time + total_duration_seconds

print(
    f"\nStarting speed test automation. Data will append to '{csv_filename}' every 30 seconds for 4 hours."
)
print("Press Ctrl + C in the terminal to terminate early.")

try:
    while time.time() < end_time:
        cycle_start = time.time()

        # Run the test using the persistent client
        log_speed(st_client)

        # Calculate time taken by the test and dynamically adjust sleep
        elapsed_in_cycle = time.time() - cycle_start
        sleep_time = max(0, interval_seconds - elapsed_in_cycle)

        # Ensure we only sleep if the next interval falls within our 4-hour window
        if time.time() + sleep_time < end_time:
            time.sleep(sleep_time)
        else:
            break

    print("\n4-hour testing period completed successfully.")

except KeyboardInterrupt:
    print("\nSpeed test monitoring stopped manually by user.")
