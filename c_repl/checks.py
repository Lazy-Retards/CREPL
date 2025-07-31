import shutil
from rich.console import Console

console = Console()

def check_gcc():
    if shutil.which("gcc") is None:
        console.print("no gcc binary found, please install gcc using the following:", style="bold red")
        console.print("[bold red]apt:[/] build-essential")
        console.print("[bold blue]windows:[/] mingw-w64 or MSYS2")
        console.print("[bold green]dnf/yum:[/] gcc")
        console.print("[bold magenta]macOS:[/] xcode-select --install")
        console.print("[bold cyan]apk:[/] build-base")
        return False
    return True
