def parse_error(errors, with_path=False):
    def get_message(errors, stack=[]):
        message = []
        if isinstance(errors, str):
            if with_path:
                message.append(f"{'.'.join(filter(None, stack))}: {errors}")
            else:
                message.append(f"{errors}")
        elif isinstance(errors, dict):
            for k, v in errors.items():
                stack.append(str(k))
                message += get_message(v, stack)
                stack.pop(-1)
        elif isinstance(errors, list):
            for item in errors:
                message += get_message(item, stack)
        return message
    if '__root__' in errors:
        return ', '.join(get_message(errors['__root__']))
    else:
        return ', '.join(get_message(errors))
