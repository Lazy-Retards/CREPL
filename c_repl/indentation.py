def next_indent(line):
    stripped = line.strip()
    return stripped.endswith("{") or stripped.endswith("(") or stripped.endswith("[")
