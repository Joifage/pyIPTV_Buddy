def ask(_output_length):
    _selection = 0
    while _selection <= 0 or _selection >= _output_length:
        _selection = input('\n# of selection or 0 for back: ')
        return int(_selection)
