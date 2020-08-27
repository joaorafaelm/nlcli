# nlcli

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/github/joaorafaelm/nlcli/blob/master/readme.ipynb)

Nlcli is a python package that offers a natural language interface for your
programs. It is primarly focused on command line interaction, but it can be used
as a chatbot and even as an interface for HTTP based programs; checkout the
[examples](https://github.com/joaorafaelm/nlcli/tree/master/examples).

Built on top of [mycroftai/padatious](https://github.com/MycroftAI/padatious)
and [libfann/fann](https://github.com/libfann/fann).

# Getting started

*You can run this tutorial interactively on [google colab](https://colab.research.google.com/github/joaorafaelm/nlcli/blob/master/readme.ipynb).*

### Instalation

Both https://github.com/libfann/fann and https://github.com/swig/swig are
required in order to install nlcli.

*On macos you might have to compile FANN from source, swig can be instaled via
`brew`.*

To install the libs on linux, run the following command:

```python
!sudo apt-get -qq install libfann-dev swig
```

Install nlcli using [pip](https://pip.pypa.io/en/stable/quickstart/):

```python
!pip install -q nlcli
```

### Usage example

```python
import nlcli


@nlcli.cmd(["hi", "Hi my name is {name}"])
def hi(name=""):
    return f"hi {name}"


@nlcli.cmd(
    ["search for {query} on {engine}", "search {query} on {engine}", "search {query} {engine}"]
)
def search(query, engine="google"):
    return f"query: {query}, engine: {engine}"


if __name__ == "__main__":
    nlcli.interact()
```

```
$ python example.py hi my name is joao
hi joao

$ python example.py search python on bing
query: python, engine: bing
```

### Python api

Call `nlcli.interact` to parse the query and call the function intent
automatically:

```python
>>> nlcli.interact("search for brazil on google", debug=True)
```
>{'name': 'search', 'sent': ['search', 'for', 'brazil', 'on', 'google'], 'matches': {'query': 'brazil', 'engine': 'google'}, 'conf': 1.0}
>
>query: brazil, engine: google


```python
>>> nlcli.interact("hi", debug=True)
```
>{'name': 'hi', 'sent': ['hi'], 'matches': {}, 'conf': 1.0}
>
>hi

```python
>>> nlcli.interact("hi, my name is joao", debug=True)
```
>{'name': 'hi', 'sent': ['hi', ',', 'my', 'name', 'is', 'joao'], 'matches': {'name': 'joao'}, 'conf': 1.0}
>
>hi joao

By default, nlcli comes with two builtin commands: `help` and `exit`. When nlcli
fails to match a query with an intent, `help` command will be automatically
called, you can change the default command by passing `default=True` to the
desired `@nlcli.cmd` decorator.

```python
>>> nlcli.interact("help", debug=True)
```
>{'name': 'help', 'sent': 'help', 'matches': {}, 'conf': 0.49447914140834637}
>
>Heres what I can do:
>
>	help - usage: help (|me) with {skill}
>
>	bye - usage: Goodbye!
>
>	hi - usage: hi
>
>	search - usage: search for {query} on {engine}

All custom commands have `help` automatically, if you want `help` on a command,
simply ask for it:

```python
>>> nlcli.interact("help me with search", debug=True)
```
>{'name': 'help', 'sent': ['help', 'me', 'with', 'search'], 'matches': {'skill': 'search'}, 'conf': 1.0}
>
>here are some examples on how to use search:
>
>	search for {query} on {engine}
>
>	search {query} on {engine}
>
>	search {query} {engine}

### CLI usage:

```python
!git clone -q https://github.com/joaorafaelm/nlcli.git && cd nlcli
```

```python
!python -m examples.getting_started hi my name is joao
```

### TODO
- Implement data augmentation lib in order to generate more samples, e.g
commands with typos, grammar errors, wrong spelling, etc.
https://github.com/makcedward/nlpaug
- Support intent files so that intent data can be decoupled from code.
- Response template and i18n.
- Add telegram and flask integration examples.
- Read from stdin.
- tests & ci setup.
