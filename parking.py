print("\n\nNOTE: Please be aware that no any vehicles are allowed to stay later than midnight, as it will be automatically be towed aways!")

vehicle = input("Enter 'C' for 'Car', 'B' for 'Bus', and 'T' for truck: ").upper()
if vehicle == "C" or vehicle == "B" or vehicle == "T":
    enterHour = int(input("Enter the hour when you enter (between 0 - 24): "))
    enterMin = int(input("Enter the minute when you enter (between 0 - 60): "))
    leftHour = int(input("Enter the hour when you left  (between 0 - 24): "))
    leftMin = int(input("Enter the minute when you left (between 0 - 60): "))

    calHour = 0
    calMin = 0
    fine = 0.00

    if leftHour >= 24 or enterHour > 24:
        print("\n\nInput only between [0]-[24]!\n")

    if leftHour < enterHour or (leftHour == enterHour and leftMin < enterMin):
        leftHour += 24

    parking_duration = (leftHour - enterHour) * 60 + (leftMin - enterMin)
    rounded_hours = parking_duration // 60 + (1 if parking_duration % 60 > 0 else 0)

    if vehicle == 'C':
        vehicle_type = "Car"
        if parking_duration <= 180:
            fine = 0.00
        else:
            fine = (rounded_hours - 3) * 1.50

    elif vehicle == 'B':
        vehicle_type = "Bus"
        if parking_duration <= 60:
            fine = 2.00
        else:
            fine = rounded_hours * 3.70

    elif vehicle == 'T':
        vehicle_type = "Truck"
        if parking_duration <= 120:
            fine = 1.00
        else:
            fine = (rounded_hours - 2) * 2.30

    print("\n\n\tPARKING LOT CHARGE")
    print("Type of Vehicle:", vehicle_type)
    print(f"TIME-IN: {enterHour:02d}:{enterMin:02d}")
    print(f"TIME-OUT: {leftMin:02d}:{leftMin:02d}")
    print("\t------------")
    print(f"PARKING TIME: {parking_duration // 60} : {parking_duration % 60:02d}")
    print(f"ROUNDED TOTAL: {rounded_hours}")
    print("\t--------------")
    print(f"TOTAL CHARGE: {fine:.2f}\n\n")
else:
    print("Please enter the right key!")
        

    

  

    



