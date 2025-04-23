def html_parser(tokens, fix_errors=False):
    output = ""
    tag_stack = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token['type'] == 'OPEN_TAG':
            tag_stack.append(token['value'])
            output += f"<{token['value']}>"

        elif token['type'] == 'CLOSE_TAG':
            if tag_stack and tag_stack[-1] == token['value']:
                tag_stack.pop()
                output += f"</{token['value']}>"

            elif fix_errors:
                if token['value'] in tag_stack:
                    while tag_stack and tag_stack[-1] != token['value']:
                        output += f"</{tag_stack.pop()}>"
                    if tag_stack:
                        tag_stack.pop()
                        output += f"</{token['value']}>"
                else:
                    pass

            else:
                if token['value'] not in tag_stack:
                    raise Exception(f"Unmatched closing tag: </{token['value']}>")
                else:
                    for j in range(len(tag_stack) - 1, -1, -1):
                        if tag_stack[j] == token['value']:
                            unclosed_tag = tag_stack[-1]
                            raise Exception(f"<{unclosed_tag}> is not closed")

        elif token['type'] == 'TEXT':
            output += token['value']

        i += 1

    if fix_errors:
        while tag_stack:
            output += f"</{tag_stack.pop()}>"

    return output
