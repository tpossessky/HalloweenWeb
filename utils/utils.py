def get_error_message(idea) -> str:

    if "Fentanyl".lower() in idea.lower() or "Fent".lower() in idea.lower():
        return "Go outside and get some fent for yourself"
    else:
        return ""