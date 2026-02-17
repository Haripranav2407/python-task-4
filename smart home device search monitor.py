device_logs = {
    "D1": ["ON", "ON", "OFF", "ON"],
    "D2": ["ON", "ON", "ON"],
    "D3": ["OFF", "OFF"],
    "D4": ["ON"]
}
went_off = []
always_on = []
for device, statuses in device_logs.items():
    if "OFF" in statuses:
        went_off.append(device)
    else:
        always_on.append(device)
print("Devices that ever went OFF:")
print(went_off)
print("\nDevices that were always ON:")
print(always_on)
