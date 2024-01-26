import shlex
from ast import literal_eval

def parse_command(cmd):
    # Normalize the command by stripping and replacing line breaks
    normalized_cmd = ' '.join(cmd.strip().splitlines())

    # Use shlex to handle quoted strings properly
    tokens = shlex.split(normalized_cmd)

    args = []
    kwargs = {}

    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.startswith('--'):
            key = token.lstrip('-')

            # Check if format is --key=value
            if '=' in key:
                key, value = key.split('=', 1)
                try:
                    # attempt to eval it it (e.g. if bool, number, or etc)
                    attempt = literal_eval(value)
                except (SyntaxError, ValueError):
                    # if that goes wrong, just use the string
                    attempt = value
                kwargs[key] = attempt
            else:
                # Check if next token is a value (not a key)
                if i + 1 < len(tokens) and not tokens[i + 1].startswith('--'):
                    kwargs[key] = tokens[i + 1]
                    i += 1  # Skip next token as it's a value
                else:
                    # Boolean flag style argument
                    kwargs[key] = True
        else:
            if token.strip():
                args.append(token)

        i += 1

    return args, kwargs