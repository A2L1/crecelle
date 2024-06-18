import os
import sys
import time

def wipe_text(sleep=0.5):
    time.sleep(sleep)
    print("\033c")


def handle_input(message=""):
    answer = input(message)
    wipe_text()
    return answer 


def define_condition_to_verify_input(boolean,answer,list_available_answer):
    if boolean:
        condition = answer in list_available_answer
    else: 
        condition = answer not in list_available_answer

    return condition

def get_input_choice(list_available_answer,while_available_answer,input_message="",error_message="Vous avez mal saisi les possibilités de réponses"):

    answer = handle_input(input_message)

    while define_condition_to_verify_input(boolean=while_available_answer,answer=answer,list_available_answer=list_available_answer):
        print(error_message)
        answer = handle_input(input_message)

    return answer

def create_or_load_project():
    print("Veuillez choisir entre le chargement d'un projet ou la création d'un nouveau")

    available_choice = {"1":"Créer un nouveau projet",
                        "2":"Charger un projet"}
    print_available_choice = "\n".join(f"{key}. {available_choice[key]}" for key in available_choice.keys()) + "\n"

    answer = get_input_choice(list_available_answer=available_choice.keys(),while_available_answer=False,input_message=print_available_choice,error_message="Veuillez choisir un nom de projet valide:\n")
    
    list_available_project = os.listdir("/crecerelle-project/utils/load")
    
    match answer:
        case "1":

            print("Choisissez le nom de votre projet: \n")
            project_name = get_input_choice(list_available_project,while_available_answer=True,error_message="Veuillez selectionner un projet pas encore utilisé: \n")

        case "2":
            print("Choisissez le projet à charger: \n")
            
            loop_printing_available_projects = "\n".join(f". {project}" for project in list_available_project) + "\n"

            project_name = get_input_choice(list_available_project,while_available_answer=False,input_message=loop_printing_available_projects,error_message="Veuillez selectionner un projet valide: \n")

    return project_name


def banner():
    PURPLE = '\033[0;36m'
    NC = '\033[0m'  # No Color
    BANNER = r"""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
        %%%%                                                                                        
      @%%#####%%%%%%%
      *%%%%%%%%%%%%%%%%%%%%%%%%                                                                   
          ****#%%%%####%%%%%%%%%%%%%%                                                               
             +*#%%#*##%##%%%%%%%%%%%%%%%                                                            
                 ***######%%%%%%%%%%%%%%%%%    +*#*            *%%##%%%%#%%%%%            @@        
                    ++#*#######%%%%%%%%%%%%%%##@@@@@*+*##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%#%%@@      
                        ++***#####%%%%%%%@@@%%%@@@@%%%%%%%%%%%%%%%%%%%#%%#%###%###%%###%%##%        
                            +++***###**##%%%%%%@%%%%%%%%%%%%%%#%%%%%%%######*###*##**#              
                                  +++++##%%%%%%%%%%#####%########*##%##*##*****                     
                                    ###%%%%%%%%%%%*+++*+***+*******+**++                            
                              ****#*#**#%%%%%%%####                                                 
                          +%#*********###%#*%%####**#                                               
                         +%%*+**+******###*#%**********                                             
                           %%#++**+****##*******+**+*+*##                                           
                             %%#++**+**##**+*++**+*+*%@                                             
                             *# %%#+**#***+**++*#%%@ %*                                             
                                #% %%%#%##%%%%%%%                                                   
                                                                                                    

"""
    print(f"{PURPLE}{BANNER}{NC}")

def kill_chain_step_choice():

    print("Choisissez l'étape de la killchain voulue:")

    step_kill_chain = {"1":"Reconnaissance",
                       "2":"Enumeration",
                       "3":"Weaponization",
                       "@":"Sortie du programme"}
    print_step_kill_chain = "\n".join(f"{key}. {step_kill_chain[key]}" for key in step_kill_chain.keys()) + "\n"

    answer = get_input_choice(step_kill_chain.keys(),while_available_answer=False,input_message=print_step_kill_chain)
    return answer

def recon_on_ip_domain():
    print("----------------Reconnaissance----------------")
    print("Voulez-vous faire de la reconaissance sur:")

    available_choice = {"1":"Récupérer les IP utilisées par un domaine"}
    print_available_choice = "\n".join(f"{key}. {available_choice[key]}" for key in available_choice.keys()) + "\n"


    answer = get_input_choice(list_available_answer=available_choice.keys(),while_available_answer=False,input_message=print_available_choice)

    return answer

def choice_load_or_input_ip():
    print("----------------Enumeration----------------")
    print("Choissisez une action à faire: ")

    available_choice = {"1":"Charger une liste d'ip depuis l'enumération",
                        "2":"Saisir une IP ou une plage d'IP"}
    print_available_choice = "\n".join(f"{key}. {available_choice[key]}" for key in available_choice.keys()) + "\n"

    answer = get_input_choice(list_available_answer=available_choice.keys(),while_available_answer=False,input_message=print_available_choice)

    return answer

def choice_file_to_load(project_name):

    path = f"/crecerelle-project/utils/load/{project_name}"
    existing_available_scan = os.listdir(path)

    list_available_scan = []

    for scan in existing_available_scan:
        if os.path.exists(f"{path}/{scan}/dns-recon/{scan}_dns_recon_backup.json"):
            list_available_scan.append(scan)

    if not list_available_scan:
        return 0

    loop_printing_available_scans = "\n".join(f". {project}" for project in list_available_scan) + "\n"

    print("Selectionnez un des scans disponibles: \n")

    selected_scan = get_input_choice(list_available_scan,while_available_answer=False,input_message=loop_printing_available_scans,error_message="Veuillez sélectionner un scan valide")

    return selected_scan

def choice_nmap_to_load(project_name):

    print("----------------Weaponization----------------")
    print("Choissisez le fichier à charger: ")

    path = f"/crecerelle-project/utils/load/{project_name}"
    existing_available_scan = os.listdir(path)

    list_available_scan = []

    for scan in existing_available_scan:
        if os.path.exists(f"{path}/{scan}/nmap/{scan}-nmap.json"):
            list_available_scan.append(scan)

    if not list_available_scan:
        return 0

    loop_printing_available_scans = "\n".join(f". {project}" for project in list_available_scan) + "\n"

    print("Selectionnez un des scans disponibles: \n")

    selected_scan = get_input_choice(list_available_scan,while_available_answer=False,input_message=loop_printing_available_scans,error_message="Veuillez sélectionner un scan valide")

    return selected_scan