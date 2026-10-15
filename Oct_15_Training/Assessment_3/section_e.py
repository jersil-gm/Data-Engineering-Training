# section_e.py

# 47. Write three event-processing messages to event_log.txt using with open()
with open("event_log.txt", "w", encoding="utf-8") as f:
    f.write("Log 1: Event registration portal opened.\n")
    f.write("Log 2: Synced attendee records from database.\n")
    f.write("Log 3: Payment gateway check completed.\n")

# 48. Append two more messages
with open("event_log.txt", "a", encoding="utf-8") as f:
    f.write("Log 4: 10 new confirmations processed.\n")
    f.write("Log 5: Daily batch execution ended.\n")

# 49. Read the complete file
print("--- Complete File Contents (read) ---")
with open("event_log.txt", "r", encoding="utf-8") as f:
    complete_text = f.read()
    print(complete_text.strip())

# 50-52. Read line by line and display without extra blank lines
print("\n--- Reading Line by Line (without extra blank lines) ---")
with open("event_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())