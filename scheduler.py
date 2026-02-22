def create_schedule(subjects, hours):
    subjects = subjects.split(",")

    schedule = "📅 Your Study Schedule:\n"

    time_slots = ["Morning", "Afternoon", "Evening", "Night"]

    for i, sub in enumerate(subjects):
        slot = time_slots[i % len(time_slots)]
        schedule += f"{slot}: Study {sub.strip()} for {hours} hour(s)\n"

    return schedule