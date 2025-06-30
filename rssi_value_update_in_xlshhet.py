# import subprocess
# from openpyxl import Workbook

# # Run ipconfig and capture output
# result = subprocess.run("ipconfig", capture_output=True, text=True, shell=True)
# output = result.stdout

# # Extract IPv4 address
# ip_address = "Not Found"
# for line in output.splitlines():
#     if "IPv4 Address" in line:
#         ip_address = line.split(":")[-1].strip()
#         break

# # Create Excel file and write IP
# wb = Workbook()
# ws = wb.active
# ws.title = "IP Info"

# ws.append(["Hostname", "IP Address"])
# ws.append(["MyComputer", ip_address])

# wb.save("ip_address.xlsx")
# print("IP Address saved to ip_address.xlsx")

import subprocess
import time
from openpyxl import Workbook
from datetime import datetime

# Function to get current RSSI (in dBm)
def get_rssi():
    result = subprocess.run("netsh wlan show interfaces", capture_output=True, text=True, shell=True)
    for line in result.stdout.splitlines():
        if "Signal" in line:
            try:
                signal_percent = int(line.split(":")[-1].strip().replace('%', ''))
                rssi = (signal_percent / 2) - 100  # Approximate RSSI
                return f"{rssi:.1f} dBm"
            except:
                return "Error"
    return "Not Found"

# Create Excel workbook and worksheet
wb = Workbook()
ws = wb.active
ws.title = "RSSI_Log"

# Write headers
ws.append(["Timestamp", "RSSI"])

# Collect RSSI every 5 seconds for 10 times
for i in range(10):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rssi = get_rssi()
    print(f"[{i+1}/10] {timestamp} | RSSI: {rssi}")
    
    # Write to Excel
    ws.append([timestamp, rssi])
    
    # Wait 5 seconds before next reading
    time.sleep(5)

# Save the Excel file
wb.save("rssi_log.xlsx")
print("✅ RSSI log saved to 'rssi_log.xlsx'")

