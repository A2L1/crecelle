import os
import sys
import time

def handle_input(message=""):
    answer = input(message)
    time.sleep(0.5)
    print("\033c")
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
    first_choice = "1. Créer un nouveau projet\n2. Charger un projet\n"
    
    
    answer = get_input_choice(["1","2"],while_available_answer=False,input_message=first_choice,error_message="Veuillez choisir un nom de projet valide:\n")
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

def kill_chain_step_choice():
    print("Choisissez l'étape de la killchain voulue:")

    step_kill_chain = {"1":"Reconnaissance",
                       "@":"Sortie du programme"}
    print_step_kill_chain = "\n".join(f"{key}. {step_kill_chain[key]}" for key in step_kill_chain.keys()) + "\n"

    answer = get_input_choice(step_kill_chain.keys(),while_available_answer=False,input_message=print_step_kill_chain)
    return answer


def recon_on_ip_domain():
    print("----------------Reconnaissance----------------")
    print("Voulez-vous faire de la reconaissance sur:")
    print("1. IP\n2. Nom de domaines\n")
    