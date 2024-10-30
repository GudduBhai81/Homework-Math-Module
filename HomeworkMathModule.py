import math

# Function to calculate sin, cos, and tan of an angle in degrees
def calculate_trig_functions(angle_degrees):
    # Convert the angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sin, cos, and tan
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    
    # Print the results
    print(f"Sin({angle_degrees}°) = {sin_value}")
    print(f"Cos({angle_degrees}°) = {cos_value}")
    print(f"Tan({angle_degrees}°) = {tan_value}")

# Example usage
angle = float(input("Enter the angle in degrees: "))
calculate_trig_functions(angle)