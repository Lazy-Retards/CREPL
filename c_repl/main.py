from c_repl.repl import CRepl
from c_repl.checks import check_gcc

def main():
    if not check_gcc():
        exit(1)
    repl = CRepl()
    repl.run()

if __name__ == "__main__":
    main()
