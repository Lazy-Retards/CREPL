from .executor import run_code
from .generic import GENERIC_TEMPLATE

class CodeBuffer:
    def __init__(self):
        self.lines = []
        self.block = []

    def add_line(self, line):
        self.block.append(line)

    def flush_block(self):
        self.lines.extend(self.block)
        self.block.clear()

    def view(self):
        return "\n".join(self.lines)

    def clear(self):
        self.lines.clear()
        self.block.clear()

    def run(self):
        self.flush_block()
        run_code(self.lines)

    def generic(self):
        self.lines.extend(GENERIC_TEMPLATE)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write("\n".join(self.lines) + "\n")
