#! /usr/bin/env python

from gnpp.template import setup, readme, licenseProject
from gnpp.arg import ArgumentParser
from datetime import datetime as th
from os import mkdir, chdir, listdir, getcwd

desc = """
 ██████╗ ███╗   ██╗██████╗ ██████╗
██╔════╝ ████╗  ██║██╔══██╗██╔══██╗
██║  ███╗██╔██╗ ██║██████╔╝██████╔╝
██║   ██║██║╚██╗██║██╔═══╝ ██╔═══╝
╚██████╔╝██║ ╚████║██║     ██║
 ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝
=== Generate New Project Python ===
Simple tool for generate :
name_project folder, name_project.py, LICENSE, README.md, setup.py
"""
class gnp:
    def __init__(self):
        arg = ArgumentParser(description=desc, allow_abbrev=False, add_help=False)
        arg.add_argument("-h", "--help", action="help", help="Display this message")
        arg.add_argument("-p", "--project-name",type=str, help="Project name")
        arg.add_argument("-l", "--license", type=str, help="License project (apache ,gnu, mit, unlicense)")
        arg.add_argument("-a", "--author", type=str, help="Author project")
        arg.add_argument("-d", "--description", type=str, help="Description project")
        arg.add_argument("-e", "--email", type=str, help="Email project")
        arg.add_argument("-u", "--url", type=str, help="Url project")
        self.args = arg.parse_args()

        if self.args.project_name != None:
            self.args.project_name = self.args.project_name.replace(" ", "_")
        else:
            self.args.project_name = "new_project"

        self.years = th.now().strftime("%Y")
        self.license = {"apache": "Apache License",
                "gnu": "GNU GENERAL PUBLIC LICENSE",
                "mit": "MIT",
                "unlicense": "Unlicense"}
    
    def createProject(self):
        if self.args.license != None and self.args.author != None and self.args.description != None and self.args.email != None and self.args.url != None:
            if self.args.license not in self.license:
                print("Registered license only exists :")
                for keys in self.license:
                    print(f"* {keys}")
                exit()
            else:
                ls = licenseProject(self.args.license)
                ls  = ls.replace("<author>", self.args.author).replace("<tahun>", self.years).replace("<nama project>", self.args.project_name )
            ls_name = self.license[self.args.license]
            at = self.args.author
            des = self.args.description
            em = self.args.email
            url = self.args.url
        
        else:
            ls = licenseProject("unlicense")
            ls_name = "Unlicense"
            at = "author"
            des = self.args.project_name
            em = self.args.project_name + "@email.com"
            url = "https://pypi.org/project/" + self.args.project_name
        st = setup
        st = st.replace("<nama_package>", self.args.project_name).replace("<description>", des).replace("<author>", at).replace("<email>", em).replace("<license>", ls_name).replace("<url_repo>", url)
        rdm = readme
        rdm = rdm.replace("<nama project>", self.args.project_name).replace("<description>", des).replace("<name_package>", self.args.project_name)
        mkdir(self.args.project_name)
        chdir(self.args.project_name)
        mkdir(self.args.project_name)
        with open(f"{self.args.project_name}/{self.args.project_name}.py", "w") as pn:
            pn.write("#! /usr/bin/env python")

        with open("LICENSE", "w") as licen:
            licen.write(ls)

        with open("setup.py", "w") as stp:
            stp.write(st)

        with open("README.md", "w") as rm:
            rm.write(rdm)
        
        dir_project = getcwd() 
        ls_project = listdir(dir_project)
        print(f"Project {self.args.project_name} has been created :")
        for file in ls_project:
            print(f"* {file}")
