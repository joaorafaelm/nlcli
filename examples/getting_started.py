import nlcli


@nlcli.cmd([
    'Hi there!', 
    'Hello.',
    "Hi",
    'Hi im {name}', 
    'Hi my name is {name}',
])
def hello(name=''):
    return f"hi {name}"

@nlcli.cmd([
    'search for {query} on {engine}',
    'search {query} on {engine}',
    'search {query} {engine}',
    'search (--query|-q)={query} (--engine|e)={engine}'
])
def search(query, engine="google"):
    return f"query: {query}, engine: {engine}"


if __name__ == "__main__":
    # print(nlcli.interact("search for brazil on google", debug=True))
    # print(nlcli.interact("search -q brazil -e google", debug=True))
    # print(nlcli.interact("search brazil", debug=True))
    # print(nlcli.interact("help with search", debug=True))
    # print(nlcli.interact("hi im joao", debug=True))
    nlcli.interact()
