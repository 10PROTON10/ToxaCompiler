import json


def evaluate(node):
    if node["type"] == "INT":
        return node["value"]
    elif node["type"] == "FLOAT":
        return node["value"]
    elif node["type"] == "PLUS":
        return evaluate(node["left"]) + evaluate(node["right"])
    elif node["type"] == "MINUS":
        return evaluate(node["left"]) - evaluate(node["right"])
    elif node["type"] == "MULT":
        return evaluate(node["left"]) * evaluate(node["right"])
    elif node["type"] == "DIV":
        return evaluate(node["left"]) / evaluate(node["right"])
    elif node["type"] == "ASSIGN":
        return evaluate(node["value"])
    elif node["type"] == "PRINT":
        return evaluate(node["value"])

if __name__ == "__main__":
    with open("ast.json", "r") as file:
        tree = json.load(file)

    result = evaluate(tree)
    print("Результат:", result)
