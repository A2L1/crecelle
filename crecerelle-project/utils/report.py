import json
import os
import subprocess
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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

    build_graphics(path,scan,file_path)

    file.write(f"<h3>Nmap Vulners scan - {scan}</h3>\n")

    score_graph = f"{path}/report/{scan}-cvss_score.png"
    severity_graph = f"{path}/report/{scan}-severity_score.png"
    score,severity = True,True

    
    if os.path.exists(file_path):
        with open(file_path,'r') as d:
            data = json.load(d)
            file.write(f"<h4>Nmap Vulners scan IP/ports - {scan}</h4>\n")

            if os.path.exists(score_graph):
                file.write(f'<img src="{score_graph}">\n')
                score = False

            if os.path.exists(severity_graph):
                file.write(f'<img src="{severity_graph}">\n')
                severity = False

            if score and severity:
                file.write("<p>Pas de vulnérabilités à afficher dans un graphique</p>")
            else:
                file.write('<div class="page-break"></div>\n')

            

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
        img {
            max-width: 100%;
            height: auto;    
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

def get_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def build_dataframe(data):
    df = pd.DataFrame()
    for ip, ip_data in data.items():
        for port_data in ip_data["ports"]:
            port = port_data["port"]
            service = port_data["service"]
            for vuln in port_data["vulnerabilities"]:
                new_row = {
                    "ip": ip,
                    "port_id": port["port_id"],
                    "port_protocol": port["protocol"],
                    "port_state": port["state"],
                    "service_name": service["name"],
                    "service_product": service["product"],
                    "service_version": service["version"],
                    "vulnerability_is_exploit": vuln["is_exploit"],
                    "vulnerability_type": vuln["type"],
                    "vulnerability_id": vuln["id"],
                    "vulnerability_cvss": vuln["cvss"]
                }
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    if "vulnerability_is_exploit" in df.columns:
        df = df[df["vulnerability_is_exploit"] == "true"]

        df = df.sort_values(by="vulnerability_cvss", ascending=True)
        df['vulnerability_cvss'] = df['vulnerability_cvss'].astype(float)

        def __cvss_to_severity(cvss_score):
            if cvss_score <= 3.9:
                return "low"
            if cvss_score <= 6.9:
                return "medium"
            if cvss_score <= 8.9:
                return "high"
            return "critical"

        df["severity"] = df["vulnerability_cvss"].apply(__cvss_to_severity)

    return df

def generate_countplot_scores(nmap_df, palette,path,scan):
    plt.figure(figsize=(10, 6))
    bar_plot = sns.countplot(data=nmap_df, x="vulnerability_cvss", hue="severity", palette=palette)
    plt.xticks(rotation=90)
    plt.xlabel("Score CVSS")
    plt.ylabel("Nombre de vulnérabilités")
    plt.title("Distribution of Vulnerabilities by CVSS Score")

    graph_path = f"{path}/report/{scan}-cvss_score.png"
    bar_plot.get_figure().savefig(graph_path)

def generate_countplot_severity(nmap_df, palette,path,scan):
    plt.figure(figsize=(10, 6))
    count_plot = sns.countplot(data=nmap_df, x="severity", hue="severity", palette=palette,
                               order=["low", "medium", "high", "critical"])
    plt.xlabel("Severity")
    plt.ylabel("Number of vulnerabilities")
    plt.title("Distribution of vulnerabilities by severity")

    graph_path = f"{path}/report/{scan}-severity_score.png"

    count_plot.get_figure().savefig(graph_path)


def count_vuln_searchsploit(data):
    # get all the adress ip
    ip_list = []
    for ip, ip_data in data.items():
        ip_list.append(ip)

    # get ports for each ip
    port_list = {}
    for ip, ip_data in data.items():
        port_list[ip] = []
        for port, port_data in ip_data.items():
            port_list[ip].append(port)

    # get number of 'Exploit' for each ip and port
    for ip, ip_ports in port_list.items():
        port_list[ip] = 0
        for port in ip_ports:
            amount_of_vuln = len(data[ip][port]['Exploit'])
            port_list[ip] += amount_of_vuln

    return port_list

def build_graphics(dir_path,scan,file_path):

    nmap = get_data(file_path)
    nmap_df = build_dataframe(nmap)

    base_palette = {
        "low": "#127da1",
        "medium": "#2ca112",
        "high": "#fcba03",
        "critical": "#c2100a"
    }

    if "vulnerability_is_exploit" in nmap_df.columns:
        generate_countplot_scores(nmap_df, base_palette,dir_path,scan)
        generate_countplot_severity(nmap_df, base_palette,dir_path,scan)

    # searchsploit = get_data("searchsploit.json")
    # port_list = count_vuln_searchsploit(searchsploit)