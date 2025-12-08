import subprocess
from rich.console import Console

console = Console()

def info(msg): console.log(f"[blue][INFO][/]: {msg}")
def success(msg): console.log(f"[green][OK][/]: {msg}")
def error(msg): console.log(f"[red][ERROR][/]: {msg}")

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

