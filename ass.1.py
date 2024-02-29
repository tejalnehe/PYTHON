def richter_scale_result(magnitude):
    if magnitude < 4.0:
        return "Little or no damage"
    elif 4.0 <= magnitude < 6.0:
        return "Minor damage"
    elif 6.0 <= magnitude < 7.0:
        return "Moderate damage"
    elif 7.0 <= magnitude < 8.0:
        return "Severe damage"
    elif 8.0 <= magnitude:
        return "Very severe damage"
    else:
        return "Invalid magnitude value"
try:
    magnitude = float(input("Enter the Richter magnitude value: "))
    result = richter_scale_result(magnitude)
    print(f"For Richter magnitude {magnitude}: {result}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value for Richter magnitude.")