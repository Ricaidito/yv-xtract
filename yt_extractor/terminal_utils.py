from termcolor import colored


def print_error(message):
    print(colored(f"[ERROR]: {message}", "red"))


def print_success(message):
    print(colored(f"[SUCCESS]: {message}", "green"))


def print_processing(message):
    print(colored(f"[PROCESSING]: {message}", "yellow"))
