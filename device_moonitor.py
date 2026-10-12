def get_initial_readings():
    """Return the initial readings."""
    return [28, 31, 35, 37, 29]


def display_readings(readings):
    """Display all readings."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def is_whole_number(text):
    """Check if input is a whole number."""
    if len(text) == 0:
        return False

    start = 0

    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True


def add_reading(readings, lowest, highest):
    """Validate and add a reading."""
    text = input("Enter new reading: ")

    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
    elif int(text) < lowest or int(text) > highest:
        print("\nInvalid reading. Enter a value from 0 to 100.")
    else:
        readings.append(int(text))
        print("\nReading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the reading classification."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings, warning_limit, critical_limit):
    """Display all classifications."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(
            reading, warning_limit, critical_limit
        )
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Calculate the total using a loop."""
    total = 0

    for reading in readings:
        total = total + reading

    return total


def compute_average(readings):
    """Calculate the average temperature."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Find the smallest reading."""
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    """Find the largest reading."""
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Count readings in a category."""
    count = 0

    for reading in readings:
        result = classify_reading(
            reading, warning_limit, critical_limit
        )

        if result == category:
            count = count + 1

    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings, warning_limit, critical_limit):
    """Display the monitoring summary."""
    number = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(
        readings, warning_limit, critical_limit, "NORMAL"
    )
    warning_count = count_category(
        readings, warning_limit, critical_limit, "WARNING"
    )
    critical_count = count_category(
        readings, warning_limit, critical_limit, "CRITICAL"
    )

    normal_percent = normal_count / number * 100
    warning_percent = warning_count / number * 100
    critical_percent = critical_count / number * 100

    status = determine_overall_status(
        warning_count, critical_count
    )

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {number}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")

    print()
    print(f"NORMAL   : {normal_count} ({normal_percent:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percent:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percent:.2f}%)")

    print()
    print(f"Overall Status: {status}")


def display_menu():
    """Display the main menu."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    """Run the monitoring system."""
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("\nEnter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            display_classifications(
                readings, warning_limit, critical_limit
            )
        elif choice == "4":
            display_summary(
                readings, warning_limit, critical_limit
            )
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print(
                "\nInvalid choice. Please enter a number from 1 to 5."
            )


main()
