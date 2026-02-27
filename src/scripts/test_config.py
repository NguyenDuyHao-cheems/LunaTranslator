import json
with open('c:/Users/nguye/Projects/LunaTranslator/src/LunaTranslator/defaultconfig/config.json', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('        },\n        "50": {\n            "name": "??????"\n        },', '        "50": {\n            "name": "??????"\n        },')
text = text.replace('        "_35": {\n            "name": "Anki_??"\n        }\n    }\n},\n"reader": {', '        "_35": {\n            "name": "Anki_??"\n        }\n        }\n    }\n},\n"reader": {')
with open('c:/Users/nguye/Projects/LunaTranslator/src/LunaTranslator/defaultconfig/config.json', 'w', encoding='utf-8') as f:
    f.write(text)
json.loads(text)
print("SUCCESS")
