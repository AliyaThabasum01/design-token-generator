from generator import css_tokens, json_tokens

colors = {}

print("=" * 45)
print("🎨 Design Token Generator")
print("=" * 45)

while True:
    name = input("Color Name (or press ENTER to finish): ")

    if name == "":
        break

    value = input("HEX Value: ")

    colors[name.lower()] = value

css = css_tokens(colors)
json_data = json_tokens(colors)

with open("output.css","w") as f:
    f.write(css)

with open("output.json","w") as f:
    f.write(json_data)

print("\n✅ Tokens Generated!")
