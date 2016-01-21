def verify(user_input, input_type):
    try:
        if input_type == "int":
            for i in user_input:
                int(i)
        elif input_type == "float":
            for i in user_input:
                float(i)
        else:
            return
        return True
    except ValueError:
        return False
