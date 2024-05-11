from utils.project import Project
from utils import create_or_load_project,kill_chain_step_choice,recon_on_ip_domain

print("\033c")

project_name = create_or_load_project()

project = Project(project_name)

print(project.repertory_path)
print(project.repertory_content)

answer = kill_chain_step_choice()

match answer:
    case "1":
        recon_on_ip_domain()
    case "2":
        print("fin")

# project.new_subfinder_search('company1.com')



