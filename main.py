
def compare_time_ranges(range1, range2):
    """Return if range 2 it is in range 1"""
    range1_value = range1.split("-")
    range1_start = int(range1_value[0].replace(":", ""))
    range1_end = int(range1_value[1].replace(":", ""))

    range2_value = range2.split("-")
    range2_start = int(range2_value[0].replace(":", ""))
    range2_end = int(range2_value[1].replace(":", ""))

    comparison1 = range1_start <= range2_start <= range1_end
    comparison2 = range1_start <= range2_end <= range1_end

    return comparison1 or comparison2


def schedule_coincidence(range1, range2):
    """Return if range 2 it is in range 1 and range 1 it is range 2"""
    comparison = compare_time_ranges(range1, range2) or compare_time_ranges(range2, range1)
    return comparison


def load_employee_data(name, data):
    """Return a dictionary that contains the name and the schedule of an employee"""
    employee = {"name": name, "schedule": {}}
    for schedule_day in data:
        day = schedule_day[0:2]
        schedule = schedule_day[2:]
        employee["schedule"][day] = schedule
    return employee


file_name = input("Employee schedule file: ")
file = open(file_name)
schedules = []

for line in file:
    data = line.strip().split("=")
    name = data[0]
    schedule_data = data[1].split(",")

    employee_data = load_employee_data(name, schedule_data)

    for other_employee in schedules:
        coincidences = 0

        for day in employee_data["schedule"]:
            if day in other_employee["schedule"]:
                this_employee_schedule = employee_data["schedule"][day]
                other_employee_schedule = other_employee["schedule"][day]

                if schedule_coincidence(this_employee_schedule, other_employee_schedule):
                    coincidences += 1

        print(other_employee["name"], employee_data["name"], coincidences)
    schedules.append(employee_data)
file.close()
