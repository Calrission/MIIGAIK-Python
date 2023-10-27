import platform


def slash() -> str:
    system = platform.system()
    if "Windows" in system:
        return "\\"
    return "/"
