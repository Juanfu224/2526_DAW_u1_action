import subprocess
from datetime import datetime


def run_tests():
    dia_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    try:
        subprocess.check_call(["pytest", "-q"])
        return f"✅ {dia_hora_actual} Tests correctos"
    except subprocess.CalledProcessError:
        return f"❌ {dia_hora_actual} Tests fallidos"


def update_readme(status: str):
    new_lines = []

    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status + "\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
