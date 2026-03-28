# 🕵️ Threat Hunting Simulation

# Simulated logs
logs = [
    "LOGIN SUCCESS - user - 192.168.1.10",
    "FILE ACCESS - public.txt",
    "LOGIN SUCCESS - admin - 45.33.32.1",
    "FILE ACCESS - confidential.docx"
]

# Suspicious indicators
alerts = []

# Process logs
for log in logs:

    # Detect admin login from external IP
    if "LOGIN SUCCESS - admin" in log and "192.168" not in log:
        alerts.append("[HUNT] Suspicious admin login from external IP")

    # Detect access to sensitive file
    if "confidential" in log:
        alerts.append("[HUNT] Sensitive file accessed")

# Output results
print("=== Threat Hunting Report ===\n")

for alert in alerts:
    print(alert)

# Final conclusion
if len(alerts) >= 2:
    print("\n[WARNING] Potential security incident detected")
