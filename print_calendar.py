import calendar
import datetime

# Define variables, year and timestamp for use in filename

year = int(input("Enter year for which you want to generate calendar: "))
# Get the current timestamp and format it to exclude milliseconds
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Replaced ":" with "-"

# What does the calendar generation

with open(f"Calendar for {year} - Generated by Python on {timestamp}.txt", "w") as f:
    f.write(calendar.calendar(year))

print("Calendar for", year, "generated and saved in file.")
