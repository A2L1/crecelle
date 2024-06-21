import json
import os
import subprocess


def build_dns_recon(path,file,scan):

    file_path = f"{path}/{scan}/dns-recon/{scan}_dns_recon_backup.json"

    file.write(f"<h3>Sub Domain - {scan}</h3>\n")

    if os.path.exists(file_path):
        with open(file_path,'r') as d:
            data = json.load(d)

            file.write("<table>\n")
            file.write("<tr>\n")
            file.write("<th>IP</th>\n")
            file.write("<th>Sous-domaine</th>\n")
            file.write("</tr>\n")
            for ip in data:
                file.write("<tr>\n")
                file.write(f'<td>{ip}</td>\n')
                file.write(f'<td></td>\n')
                file.write("</tr>\n")
                for sub_domain in data[ip]:
                    file.write("<tr>\n")
                    file.write(f'<td></td>\n')
                    file.write(f'<td>{sub_domain}</td>\n')
                    file.write("</tr>\n")
            file.write("</table>\n")
            file.write('<div class="page-break"></div>\n')
    else:
        file.write("<p>Pas de données sur les sous-domaines pour ce scan</p>\n")

def build_nmap_scan(path,file,scan):
    file_path = f"{path}/{scan}/nmap/{scan}-nmap.json"

    file.write(f"<h3>Nmap Vulners scan - {scan}</h3>\n")

    if os.path.exists(file_path):
        with open(file_path,'r') as d:
            data = json.load(d)
            file.write(f"<h4>Nmap Vulners scan IP/ports - {scan}</h4>\n")

            file.write("<table>\n")
            file.write("<tr>\n")
            file.write("<th>IP</th>\n")
            file.write("<th>Port - Services</th>\n")
            file.write("</tr>\n")

            for ip in data:
                file.write("<tr>\n")
                file.write(f'<th>{ip}</th>\n')
                file.write(f'<td></td>\n')
                file.write("</tr>\n")
                for port in data[ip]["ports"]:
                    file.write("<tr>\n")
                    file.write(f'<td></td>\n')
                    product = port["service"].get("product")
                    version = port["service"].get("version")

                    if product != "None" and version != "None":
                        file.write(f'<th>{port["service"].get("name")}/{port["port"]["port_id"]} - {product} {version}</th>\n')
                        file.write("</tr>\n")

                    elif product != "None" and version == "None":
                        product = product.split(" ")[0]
                        file.write(f'<th>{port["service"].get("name")}/{port["port"]["port_id"]} - {product}</th>\n')
                    else:
                        file.write(f'<th>{port["service"].get("name")}/{port["port"]["port_id"]}</th>\n')
                    file.write("</tr>\n")

            file.write("</table>\n")
            file.write('<div class="page-break"></div>\n')

            file.write(f"<h4>Nmap Vulners scan IP/ports/vuln - {scan}</h4>\n")

            file.write("<table>\n")
            file.write("<tr>\n")
            file.write("<th>IP</th>\n")
            file.write("<th>Port - Services</th>\n")
            file.write("<th>Vuln</th>\n")
            file.write("</tr>\n")

            for ip in data:
                file.write("<tr>\n")
                file.write(f'<th>{ip}</th>\n')
                file.write(f'<td></td>\n<td></td>\n')
                file.write("</tr>\n")
                for port in data[ip]["ports"]:
                    file.write("<tr>\n")
                    file.write(f'<td></td>\n')
                    product = port["service"].get("product")
                    version = port["service"].get("version")

                    if product != "None" and version != "None":
                        file.write(f'<th>{port["service"].get("name")}/{port["port"]["port_id"]} - {product} {version}</th>\n')
                        file.write(f'<td></td>\n')
                        file.write("</tr>\n")


                        vulnerabilities = port["vulnerabilities"]

                        for vuln in vulnerabilities:
                            if vuln["is_exploit"] == "true":
                                file.write("<tr>\n")
                                file.write(f'<td></td>\n<td></td>\n')
                                id = vuln['id']
                                file.write(f"<td>{id}</td>\n")
                                file.write("</tr>\n")


                    elif product != "None" and version == "None":
                        product = product.split(" ")[0]
                        file.write(f'<th>{port["service"].get("name")}/{port["port"]["port_id"]} - {product}</th>\n')
                        file.write(f'<td></td>\n')
                    else:
                        file.write(f'<th>{port["service"].get("name")}/{port["port"]["port_id"]}</th>\n')
                    file.write("</tr>\n")
            file.write("</table>\n")
            file.write('<div class="page-break"></div>\n')
    else:
        file.write("<p>Pas de données sur les sous-domaines pour ce scan</p>\n")

def build_searchsploit_scan(path,file,scan):

    file_path = f"{path}/{scan}/searchsploit/{scan}-searchsploit.json"

    file.write(f"<h3>Searchsploit - {scan}</h3>\n")

    file.write("<table>\n")
    file.write("<tr>\n")
    file.write("<th>IP</th>\n")
    file.write("<th>Port - Services</th>\n")
    file.write("<th>Exploit Path</th>\n")
    file.write("<th>Description</th>\n")
    file.write("</tr>\n")

    if os.path.exists(file_path):
        with open(file_path,'r') as d:
            data = json.load(d)

            for ip in data:
                file.write("<tr>\n")
                file.write(f'<th>{ip}</th>\n')
                file.write(f'<td></td>\n<td></td>\n')
                file.write("</tr>\n")
                for port in data[ip]:
                    
                    for type in data[ip][port]:
                        file.write("<tr>\n")
                        file.write(f'<td></td>\n')
                        if data[ip][port][type] != "No Results":
                            file.write(f'<th>{port}/{type}</th>\n')
                            file.write(f'<td></td>\n')
                            file.write("</tr>\n")

                            for path_exploit in data[ip][port][type]:
                                file.write("<tr>\n")
                                file.write(f'<td></td>\n<td></td>\n')
                                file.write(f"<td>{path_exploit}</td>\n")
                                file.write(f"<td>{data[ip][port][type][path_exploit]}</td>\n")
                                file.write("</tr>\n")
                        else:
                            file.write(f'<th>{port}/{type}</th>\n<th>No results</th>\n')
                            file.write("</tr>\n")


    file.write("</table>\n")
    file.write('<div class="page-break"></div>\n')

def build_for_each_scan(path,file,scan):
    file.write(f"<h2>Report for {scan}</h2>")
    build_dns_recon(path,file,scan)
    build_nmap_scan(path,file,scan)
    build_searchsploit_scan(path,file,scan)


    

def build_from_all_scan(project_name,file):
    path = f"/crecerelle-project/utils/load/{project_name}"
    existing_available_scan = os.listdir(path)

    if not existing_available_scan:
        file.write('<p>Pas de données disponibles</p>\n')
    else:
        for scan in existing_available_scan:
            if scan != "report":
                build_for_each_scan(path=path,file=file,scan=scan)

def build_html(project_name):

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    COLOR_OFF = "\033[0m"

    dir_path = f"/crecerelle-project/utils/load/{project_name}/report"
    html_path = f"{dir_path}/report.html"
    pdf_path = f"{dir_path}/report.pdf"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    command = f"rm -f {html_path}"       
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    f = open(html_path,'w')
    f.write('<!DOCTYPE html>\n')
    f.write(f'<html>\n<head>\n<meta charset="UTF-8">\n<title>{project_name}</title>\n')
    f.write("""<style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            margin-left: auto;
            margin-right: auto;
            table-layout: fixed;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
            border-right: 1px solid #ddd;
            word-wrap: break-word;
            overflow-wrap: break-word
        }
        th {
            background-color: #f2f2f2;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
        th:last-child, td:last-child {
            border-right: none;
        }
        .page-break {
            page-break-after: always;
        }
    </style>""")
    f.write('</head>\n<body>\n')
    f.write(f'<h1>{project_name}</h1>\n')
    build_from_all_scan(project_name=project_name,file=f)
    f.write(f"</body>\n</html>\n")
    f.close()

    command = f"rm -f {pdf_path}"       
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    command = f"weasyprint {html_path} {pdf_path}"       
    result = subprocess.run(command,stderr=subprocess.PIPE, shell=True, executable="/bin/bash")

    if result.stderr:
        print(f"{RED}Erreur lors de l'execution: {COLOR_OFF}")
        print(result.stderr)
    else:
        print(f"{GREEN}PDF généré{COLOR_OFF}")
        print(f"{BLUE}le fichier existe: {pdf_path}{COLOR_OFF}")