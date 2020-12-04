def format_decorator(format_func, *args):
    def format_wrapper(*args):
        formatted_rows = []
        if args:
            for row in args[0]:
                formatted_rows.append(format_func(row))
        return formatted_rows

    return format_wrapper


@format_decorator
def format_task(row):
    item = f"{row[1]}: {row[0]:<4}"
    task = f"{row[2]}"
    date_set = f"Date set: {row[3]}"
    days_to_complete = f"Days to complete: {row[5]}"
    is_complete = f"Completed: {row[6]:<5}"
    date_complete = f"Date complete: {row[4]}"
    is_void = f"Void: {row[7]:<5}"
    return f"{item} [{date_set}, {days_to_complete}, {is_complete}, {date_complete}, {is_void}] {task}"


@format_decorator
def format_note(row):
    item = f"{row[1]}: {row[0]:<4}"
    note = f"{row[2]}"
    date_set = f"Date set: {row[3]}"
    return f"{item} [{date_set}] {note}"
