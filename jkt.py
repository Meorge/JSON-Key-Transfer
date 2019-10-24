import sys
import json


def TransferKeys(masterName, childName):
    # first, get all the keys in master
    with open(masterName, "r") as master:
        masterText = master.read()

    masterJSON = json.loads(masterText)

    with open(childName, "r") as child:
        childText = child.read()

    childJSON = json.loads(childText)

    for key, value in masterJSON["strings"].items():
        if key not in childJSON["strings"]:
            print("%s" % key)
            childJSON["strings"][key] = "**UNTRANSLATED** - Original: '%s'" % value


    with open("out.json", "w") as childOut:
        childOut.write(json.dumps(childJSON, indent="\t", ensure_ascii=False))





if len(sys.argv) != 3:
    print("Incorrect arguments")
    print("""Syntax:
    jkt.py [master].json [child].json
    Will add any keys in [master].json to [child].json and sort [child].json
    """)

else:
    TransferKeys(sys.argv[1], sys.argv[2])

