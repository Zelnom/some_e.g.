# Fiind dat titlul unui produs, sa se transforme in varianta lui de URL cu ajutorul unei functii, folosind TDD.
# Litere mari -> Litere mici
# Spatii -> Minus-uri
# Diacritice -> Non-diacritice
# Caractere speciale -> remove

def URL(name):
    result : str = name.lower()
    for i in range(0, len(result)):
        if not result[i].isalnum() and name[i] != " ":
            result = result.replace(result[i], "")

    to_replace = {
        "ț": "t",
        "ș": "s",
        "ă": "a",
        "î": "i",
        "â": "a",
        "Ț": "t",
        "Ș": "s",
        "Ă": "a",
        "Î": "i",
        "Â": "a",
        " ": "-",

    }
    for key in to_replace:
        result = result.replace(key, to_replace.get(key))

    return result
