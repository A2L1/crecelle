import subprocess
import os

def lauch_subfinder(domain,name,directory_save_path):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    COLOR_OFF = "\033[0m"

    print(f"{BLUE}Execution subfinder{COLOR_OFF}")
    scan_path = f"{directory_save_path}/{domain}/sub-domain/"
    output_path = f"{scan_path}{name}-subfinder.txt"
    if os.path.isfile(output_path):
        open(output_path, 'w').close()
    command = f'subfinder -silent -recursive -active -domain {domain} -output {output_path} &'
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    if result.stderr:
        print(f"{RED}Erreur lors de l'execution: {COLOR_OFF}")
        print(result.stderr)
    else:
        print(f"{GREEN}Subfinder research done{COLOR_OFF}")
        print(f"{BLUE}Loaded in this session and stored at this following path : {output_path}{COLOR_OFF}")
    
    return output_path
