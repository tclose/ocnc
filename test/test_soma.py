# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:30:29 2016

@author: Alex
"""
import numpy as np
import matplotlib.pyplot as plt
import neuron
nrn=neuron.h

def soma_only():
    nrn('forall delete_section()')
    soma = nrn.Section('soma')
    soma.L = 10 # um
    soma.diam = 10  # um
    soma.nseg = 1  
    
    for sec in nrn.allsec():
        sec.insert('pas')
        sec.Ra = 100
        sec.cm = 1
        for seg in sec:
            seg.g_pas = 0.00003
            seg.e_pas = -65

    return soma
    
def soma_wmech():
    soma2 = nrn.Section('soma')
    soma2.L = 10 # um
    soma2.diam = 10  # um
    soma2.nseg = 1  
    
    for sec in nrn.allsec():
        sec.insert('pas')
        sec.Ra = 100
        sec.cm = 1
        for seg in sec:
            seg.g_pas = 0.00003
            seg.e_pas = -65
        sec.insert('nap')

    return soma2
    
def insert_current_clamp(input_site, dur=1e9):
    """
    Inserts a current clamp in the neuron model
    :param input_site: Where to place the current clamp. Example: soma(0.5), where 0.5 means 'center',
           0 would mean start, and 1 would mean at the end of the segment in question.
           dur: Duration of the current pulse.
    :return: The NEURON object current clamp. This must be returned, otherwise it is lost.
    """
    stim = nrn.IClamp(input_site)
    stim.delay = 10
    stim.amp = 0.005
    stim.dur = dur
    return stim
    
def run_simulation(record_site):
    """
    Runs the NEURON simulation
    :param record_site: Where to record membrane potential from. Example: soma(0.5), where 0.5 means 'center',
           0 would mean start, and 1 would mean at the end of the segment in question.
    :return: Time and voltage numpy arrays
    """
    rec_t = nrn.Vector()
    rec_t.record(nrn._ref_t)
    # Record Voltage from the record site
    rec_v = nrn.Vector()
    rec_v.record(record_site._ref_v)
    neuron.h.dt = 2**-3
    nrn.finitialize(-65)
    neuron.init()
    neuron.run(200)
    return np.array(rec_t), np.array(rec_v)
    
def test_no_mech():
    soma_nomech=soma_only()
    stim1 = insert_current_clamp(soma_nomech(0.5))
    t, v_test = run_simulation(soma_nomech(0.5))
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(t, v_test, 'gray', label='"Experiment passive"')
    
def test_mech():
    soma_na_mech=soma_wmech()
    t, v_nap = run_simulation(soma_na_mech(0.5))  
    fig = plt.figure()
    ax2 = fig.add_subplot(212)
    ax2.plot(t, v_nap, 'red', label='"Experiment na"')
    
if __name__ == '__main__':
    test_no_mech()
    test_mech()
    plt.show()
    print 'done'
