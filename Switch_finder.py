import subprocess

applicationn_name = str(input("Enter the app/path "))


def find_silent_install_switch(application_name):
    command = f"{application_name} /?"
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout + result.stderr
    for line in output.split("\n"):
        line = line.strip()
        if "/S" in line or "/s" in line or "/q" in line or "/quiet" in line:
            return line
    return None


silent_switch = find_silent_install_switch(applicationn_name)

print(silent_switch)

