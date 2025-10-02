def get_error_message(idea) -> str:

    """
    Defined error messages to return to the client when a specific word or phrase is encountered.
    :param idea: text entered by the user
    :return: error message.
    """
    idea_lower = idea.lower()
    anyway = " - we'll take your feedback anyway"
    if "fentanyl" in idea_lower or "fent" in idea_lower:
        return "Go get some fentanyl for yourself. There's plenty to go around" + anyway
    if "spam" in idea_lower or "ads" in idea_lower:
        return "Congratulations, your idea is junk (spam)"+ anyway
    if "kill" in idea_lower or "murder" in idea_lower:
        return "Did you mean to say that we KILLED IT?? Thank you!"+ anyway
    if "drugs" in idea_lower:
        return "Bring more next time!"+ anyway

    return ""