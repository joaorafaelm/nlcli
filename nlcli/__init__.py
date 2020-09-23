import os
import random
import sys
from functools import wraps

from padatious import IntentContainer

intents = {}
default_intent = "help"
container = IntentContainer(".data")
linesep = "\n"
tabsep = "\t"


def cmd(samples, default=False):
    def inner_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        if default:
            default_intent = f.__name__
        intents[f.__name__] = f, samples
        return wrapper

    return inner_function


def train():
    for name, intent in intents.items():
        func, samples = intent
        container.add_intent(name, samples)
    container.train(debug=False)


def eval_intent(query, debug=False):
    intent = container.calc_intent(query)
    f, samples = intents[intent.name] if intent.conf else intents[default_intent]
    if debug:
        print(intent)
    return f(**intent.matches) if f.__code__.co_argcount else f()


def interact(query=None, debug=False):
    train()
    cli_args = " ".join(sys.argv[1:])
    query = query or cli_args

    if query:
        intent = eval_intent(query, debug)
        if cli_args:
            print(intent)
        return intent

    while True:
        query_input = input("> ")
        if query_input:
            intent = eval_intent(query_input, debug)
            print(intent)
            if intent == bye():
                os._exit(1)


@cmd(
    ["help (|me) with {skill}", "help {skill}", "{skill} help", "what can you do", "i need help",],
    default=True,
)
def help(skill=None):
    if skill:
        f, samples = intents.get(skill, [None, None])
        if samples:
            return f"here are some examples on how to use {skill}:{linesep+tabsep}{(linesep+tabsep).join(samples)}"
    return f"Heres what I can do:{linesep}{linesep.join([f'{tabsep +k} - usage: {random.sample(v[-1], 1)[0]}' for k, v in intents.items()])}"


@cmd(["See you!", "Goodbye!", "bye", "by", "quit", "exit", "q"])
def bye():
    return "bye"
