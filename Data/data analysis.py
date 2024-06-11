import csv
import os.path

userhome = os.path.expanduser('~')
csvfile = os.path.join(userhome, 'Desktop', 'car-crashes-nyc', 'Cleaned-Vehicle-Crashes-NYC.csv')
txt_file = os.path.join(userhome, 'Desktop', 'car-crashes-nyc', 'Cleaned-Vehicle-Crashes-NYC.txt')

# Initialize dictionaries to store injuries, fatalities, and causes per year
injuries_per_year = {}
fatalities_per_year = {}
causes_count = {}

# Function to extract year from 'CRASH DATETIME' string
def extract_year(datetime_str):
    try:
        # Extract the year from the format 'YYYY-MM-DD'
        return datetime_str.split('-')[0]
    except IndexError:
        return None

# Function to convert float strings to integers
def convert_to_int(float_str):
    try:
        return int(float(float_str))
    except ValueError:
        return 0

# Read the csv file and parse it
with open(csvfile, newline='') as file:
    reader = csv.DictReader(file)
    
    # Print column names for debugging
    print("Column names:", reader.fieldnames)
    
    # Read and process the rows
    for row in reader:
        crash_datetime = row['CRASH DATETIME']
        year = extract_year(crash_datetime)
        
        # Print the CRASH DATETIME and extracted year for debugging
        print(f"CRASH DATETIME: {crash_datetime}, Extracted Year: {year}")
        
        if year:
            # Update injuries and fatalities per year
            if year not in injuries_per_year:
                injuries_per_year[year] = 0
            if year not in fatalities_per_year:
                fatalities_per_year[year] = 0

            injuries = convert_to_int(row['NUMBER OF PERSONS INJURED'])
            fatalities = convert_to_int(row['NUMBER OF PERSONS KILLED'])

            injuries_per_year[year] += injuries
            fatalities_per_year[year] += fatalities

            # Update causes count
            cause = row['CONTRIBUTING FACTOR VEHICLE 1']
            if cause not in causes_count:
                causes_count[cause] = 0
            causes_count[cause] += 1
            
            # Print the cause for debugging
            print(f"Cause: {cause}, Current Count: {causes_count[cause]}")

# Find the most common cause of accidents
if causes_count:
    most_common_cause = max(causes_count, key=causes_count.get)
else:
    most_common_cause = 'Unknown'

# Print results
print("Injuries per year:")
for year, injuries in injuries_per_year.items():
    print(f"{year}: {injuries}")

print("\nFatalities per year:")
for year, fatalities in fatalities_per_year.items():
    print(f"{year}: {fatalities}")

print("\nMost common cause of accidents:")
print(f"{most_common_cause}: {causes_count.get(most_common_cause, 0)}")

# Save the analysis results to a text file
with open(txt_file, "w") as txt_file:
    txt_file.write("Crash Analysis Results\n")
    txt_file.write("-" * 30 + "\n")
    
    # Write injuries per year
    txt_file.write("Injuries per year:\n")
    for year, injuries in injuries_per_year.items():
        txt_file.write(f"{year}: {injuries}\n")
    txt_file.write("-" * 30 + "\n")
    
    # Write fatalities per year
    txt_file.write("Fatalities per year:\n")
    for year, fatalities in fatalities_per_year.items():
        txt_file.write(f"{year}: {fatalities}\n")
    txt_file.write("-" * 30 + "\n")
    
    # Write most common cause of accidents
    txt_file.write("Most common cause of accidents:\n")
    txt_file.write(f"{most_common_cause}: {causes_count.get(most_common_cause, 0)}\n")
    txt_file.write("-" * 30 + "\n")

print("Analysis results have been saved to:", txt_file)