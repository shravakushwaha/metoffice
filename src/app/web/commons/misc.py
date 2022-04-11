def error_message_extractor(error: str):
    error_pos = str(error).find("DETAIL: ")
    # error = str(error)[int(error_pos + 9) :]
    # error_pos = str(error).find(".")
    # error = str(error)[:error_pos]
    # return error
    # return error_pos
    return error
