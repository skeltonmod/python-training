from datetime import datetime

d = str(datetime.now().strftime("%H:%M:%S %P"))

morning = "Morning" if d.split(" ")[1] == "am" else "Afternoon"

print(f"Good {morning}, The time is {d}")