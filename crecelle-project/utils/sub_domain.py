import subprocess

def lauch_subfinder(domain,name):
    print("Execution subfinder")
    output_path = "out/sub_domain/{name}-subfinder.txt"
    command = f'nohup subfinder -silent -recursive -active -domain {domain} -output {output_path}'
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    if result.stderr:
        print("Erreur lors de l'execution: ")
        print(result.stderr)
    else:
        print("subfinder research done")
        print("loaded in this session and stored at this following path : {}")
    
    return result.stdout
