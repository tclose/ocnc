import numpy as np
import matplotlib.pyplot as plt
import neuron

nrn=neuron.h

nrn.load_file("stdrun.hoc")

#load neuron morphology
nrn.xopen("stellate_scaled_morpho.hoc")


#Biophysical parameters
gnabar=0.04               #sodium conductance, S/cm2
gka = 0.036               #A-type potassium density, S/cm2
gkdr = 0.036              #delayed rectifier density, S/cm2
#nrn.psection()
sec=nrn.SectionList(); sec.wholetree()
for s in sec: 
    s.cm=1
    s.Ra = 150
    s.insert('pas')#Insert passive mechanisms in all compartments
    for seg in s:
        seg.g_pas = 0.00005
        seg.e_pas = -65
    #Insert active mechanisms in all compartments
    s.insert('nap')
    gbar_nap=0.0
    s.insert('kdr')
    gkdrbar_kdr=0.5*gkdr
    s.insert('kap')
    gkabar_kap=1.0*gka
    
#nrn.psection()

class cell_sections:
    def __init__(self):
        #self.soma = nrn.Section(name = 'soma')
        self.dendrite = list()
        self.axon=list()

        for s in sec:
            if s.name().startswith('dend'):
                self.dendrite.append(s)
            elif s.name().startswith('axon'):
                self.axon.append(s)
 
listallsections=cell_sections()

