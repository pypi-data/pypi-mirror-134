#! /usr/bin/env pyhton

from gnpp.gnpp import gnp 

def cli():
    generate_project = gnp()
    generate_project.createProject()
