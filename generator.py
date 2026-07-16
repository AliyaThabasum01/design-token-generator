import json


def css_tokens(colors):

    css = ":root {\n"

    for key,value in colors.items():
        css += f"  --{key}: {value};\n"

    css += "}"

    return css


def json_tokens(colors):

    return json.dumps(
        {
            "color":colors
        },
        indent=4
    )
