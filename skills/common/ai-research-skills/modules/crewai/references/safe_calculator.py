"""Bounded arithmetic; no names, calls, attributes or containers."""
import ast
import math
import operator

OPS = {
    ast.Add: ("+", operator.add), ast.Sub: ("-", operator.sub),
    ast.Mult: ("*", operator.mul), ast.Div: ("/", operator.truediv),
    ast.FloorDiv: ("//", operator.floordiv), ast.Mod: ("%", operator.mod),
    ast.Pow: ("**", operator.pow),
}


def calculate(expression, allowed_operators=None):
    if not isinstance(expression, str) or not 0 < len(expression) <= 256:
        raise ValueError("Expression must contain 1-256 characters")
    allowed = set(allowed_operators) if allowed_operators is not None else {
        item[0] for item in OPS.values()
    }
    tree = ast.parse(expression, mode="eval")
    if sum(1 for _ in ast.walk(tree)) > 64:
        raise ValueError("Expression too complex")

    def bounded(value):
        if type(value) not in (int, float) or not math.isfinite(value) or abs(value) > 1e12:
            raise ValueError("Numeric result out of bounds")
        return value

    def visit(node):
        if isinstance(node, ast.Constant):
            return bounded(node.value)
        if isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub):
            symbol = "+" if isinstance(node.op, ast.UAdd) else "-"
            if symbol not in allowed:
                raise ValueError("Operator not allowed")
            value = visit(node.operand)
            return bounded(value if symbol == "+" else -value)
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            symbol, operation = OPS[type(node.op)]
            if symbol not in allowed:
                raise ValueError("Operator not allowed")
            left, right = visit(node.left), visit(node.right)
            if symbol == "**" and abs(right) > 12:
                raise ValueError("Exponent out of bounds")
            return bounded(operation(left, right))
        raise ValueError("Only numeric arithmetic is supported")

    return visit(tree.body)
