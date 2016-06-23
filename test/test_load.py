import numpy as np
import matplotlib.pyplot as plt
import neuron

nrn=neuron.h

nrn.load_file("stdrun.hoc")

#load neuron model
nrn.xopen("stellate_scaled2.hoc")
soma = nrn.Section(name='soma')
nrn.psection()