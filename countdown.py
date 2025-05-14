# countdown.py

import time
from datetime import datetime

# Target date and time
target_time = datetime(2025, 6, 11, 23, 0, 0)

def countdown(target_time):
    while True:
        # Get the current time
        now = datetime.now()
        
        # Calculate the remaining time
        remaining_time = target_time - now
        
        if remaining_time.total_seconds() <= 0:
            print("\033[91mTime's up! \033[0m")
            break
        
        days = remaining_time.days
        hours, remainder = divmod(remaining_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Print the countdown with a red color (ANSI escape code for red text)
        print(f"\033[91mTime remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds\033[0m")
        
        # Wait for 1 second before updating the countdown
        time.sleep(1)

if __name__ == "__main__":
    countdown(target_time)
