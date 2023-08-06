#! /usr/bin/env python

from os import path as p

d = p.dirname(p.abspath(__file__))
setup = p.join(d, "assets/setup.txt")
mit = p.join(d, "assets/MIT.txt")
ggpl = p.join(d, "assets/GNU GENERAL PUBLIC LICENSE.txt")
apache = p.join(d, "assets/Apache License.txt")
unlicense = p.join(d, "assets/unlicense.txt")
readme = p.join(d, "assets/README.txt")

with open(mit, "r") as mt:
    mit = mt.read()

with open(ggpl, "r") as gpl:
    ggpl = gpl.read()

with open(apache, "r") as ap:
    apache = ap.read()

with open(unlicense, "r") as ul:
    unlicense = ul.read()

with open(setup, "r") as st:
    setup = st.read()

with open(readme, "r") as rm:
    readme = rm.read()

def licenseProject(ls):
    if ls == "mit":
        ls = mit
    elif ls == "gnu":
        ls = ggpl
    elif ls == "apache":
        ls = apache
    elif ls == "unlicense":
        ls = unlicense
    return ls
