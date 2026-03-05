def validate_task_data(data):

    required_fields = ["title", "description", "assigned_to"]

    for field in required_fields:

        if field not in data or not data[field]:

            return False, f"{field} is required"

    return True, "Valid task data"
