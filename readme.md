# nlcli

[![Open In Colab](https://colab.research.google.com/assets/colab-
badge.svg)](https://github.com/joaorafaelm/nlcli/blob/master/readme.ipynb)

Nlcli is a python package that offers a natural language interface for your
programs. It is primarly focused on command line interaction, but it can be used
as a chatbot and even as an interface for HTTP based programs; checkout the
[examples](https://github.com/joaorafaelm/nlcli/tree/master/examples).

Built on top of [mycroftai/padatious](https://github.com/MycroftAI/padatious)
and [libfann/fann](https://github.com/libfann/fann).

# Getting started

*You can run this tutorial interactively on [google
colab]((https://github.com/joaorafaelm/nlcli/blob/master/readme.ipynb).*

### Instalation

Both https://github.com/libfann/fann and https://github.com/swig/swig are
required in order to install nlcli.

*On macos you might have to compile FANN from source, swig can be instaled via
`brew`.*

To install the libs on linux, run the following command:

```{.python .input  n=1}
!sudo apt-get -qq install libfann-dev swig
```

Install nlcli using [pip](https://pip.pypa.io/en/stable/quickstart/):

```{.python .input  n=2}
!pip install -q nlcli
```

## Usage example

```{.python .input  n=3}
import nlcli


@nlcli.cmd(["hi", "Hi my name is {name}"])
def hi(name=""):
    return f"hi {name}"


@nlcli.cmd(
    ["search for {query} on {engine}", "search {query} on {engine}", "search {query} {engine}"]
)
def search(query, engine="google"):
    return f"query: {query}, engine: {engine}"
```

Call `nlcli.interact` to parse the query and call the function intent
automatically:

```{.python .input  n=4}
nlcli.interact("search for brazil on google", debug=True);
```

```{.json .output n=4}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{'name': 'search', 'sent': ['search', 'for', 'brazil', 'on', 'google'], 'matches': {'query': 'brazil', 'engine': 'google'}, 'conf': 1.0}\nquery: brazil, engine: google\n"
 }
]
```

```{.python .input  n=5}
nlcli.interact("hi", debug=True);
```

```{.json .output n=5}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{'name': 'hi', 'sent': ['hi'], 'matches': {}, 'conf': 1.0}\nhi \n"
 }
]
```

```{.python .input  n=6}
nlcli.interact("hi, my name is joao", debug=True);
```

```{.json .output n=6}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{'name': 'hi', 'sent': ['hi', ',', 'my', 'name', 'is', 'joao'], 'matches': {'name': 'joao'}, 'conf': 1.0}\nhi joao\n"
 }
]
```

By default, nlcli comes with two builtin commands: `help` and `exit`. When nlcli
fails to match a query with an intent, `help` command will be automatically
called, you can change the default command by passing `default=True` to the
desired `@nlcli.cmd` decorator.

```{.python .input  n=7}
nlcli.interact("help", debug=True);
```

```{.json .output n=7}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{'name': 'help', 'sent': 'help', 'matches': {}, 'conf': 0.49447914140834637}\nHeres what I can do:\n\thelp - usage: help (|me) with {skill}\n\tbye - usage: Goodbye!\n\thi - usage: hi\n\tsearch - usage: search for {query} on {engine}\n"
 }
]
```

All custom commands have `help` automatically, if you want `help` on a command,
simply ask for it:

```{.python .input  n=8}
nlcli.interact("help me with search", debug=True);
```

```{.json .output n=8}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "{'name': 'help', 'sent': ['help', 'me', 'with', 'search'], 'matches': {'skill': 'search'}, 'conf': 1.0}\nhere are some examples on how to use search:\n\tsearch for {query} on {engine}\n\tsearch {query} on {engine}\n\tsearch {query} {engine}\n"
 }
]
```

# CLI usage:

```{.python .input}
!git clone -q https://github.com/joaorafaelm/nlcli.git && cd nlcli
```

```{.python .input}
!python -m examples.getting_started hi my name is joao
```

# TODO
- Implement data augmentation lib in order to generate more samples, e.g
commands with typos, grammar errors, wrong spelling, etc.
https://github.com/makcedward/nlpaug
- Support intent files so that intent data can be decoupled from code.
- Response template and i18n.
- Add telegram and flask integration examples.
- Read from stdin.
- tests & ci setup.
