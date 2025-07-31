from .buffer import CodeBuffer
from .commands import handle_command
from .indentation import next_indent
import readline

class CRepl:
    def __init__(self):
        self.buffer = CodeBuffer()
        self.indent_spaces = ""

    def run(self):
        print("C REPL (type '§run', '§view', '§clear', '§save filename', 'exit')")

        def prefill():
            readline.insert_text(self.indent_spaces)
            readline.redisplay()

        while True:
            readline.set_pre_input_hook(prefill)
            try:
                line = input(">>> " if not self.buffer.block else "... ")
            except EOFError:
                break
            finally:
                readline.set_pre_input_hook()

            # Commands
            if line.startswith("§"):
                if handle_command(line.strip(), self.buffer):
                    continue

            self.buffer.add_line(line)
            if next_indent(line):
                self.indent_spaces += "    "
            elif line.strip().startswith("}"):
                self.indent_spaces = self.indent_spaces[:-4] if len(self.indent_spaces) >= 4 else ""
            elif line.strip().endswith(";") and not next_indent(line):
                self.buffer.flush_block()
                self.indent_spaces = ""
