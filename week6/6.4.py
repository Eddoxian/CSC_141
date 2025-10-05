glossary = {
    'variable': 'a name that stores a value',
    'function': 'A set of code that performs a task',
    'loop': 'a way for code to repeat back to a certain point',
    'list': 'exactly what the name suggests, a list of items',
    'dictionary': 'a list of key-value pairs'
}
for word, meaning in glossary.items():
    (print(f"{word.title()}: {meaning}"))
    
glossary['tuple'] = 'An immutable list.'
glossary['string'] = 'A series of characters.'
glossary['boolean'] = 'A value that can be True or False.'
glossary['argument'] = 'A value passed to a function.'
glossary['looping'] = 'The act of iterating over items.'
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")