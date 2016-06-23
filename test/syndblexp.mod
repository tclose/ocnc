COMMENT
//****************************		//
// Created by Alex Tran-Van-Minh	//
// alexandra.tran.van.minh@gmail.com//
//		2015						//
//****************************		//
ENDCOMMENT

COMMENT
an synaptic current with alpha function conductance defined by
        i = g * (v - e)      i(nanoamps), g(micromhos);
        where
         g = 0 for t < onset and
         g = gmax *(A1 *  exp(-(t - onset )/tau1) + A2 *  exp(-(t - onset )/tau2))
          for t > onset
this has the property that the maximum value is gmax and occurs at
 t = delay + tau.
ENDCOMMENT
					       
NEURON {
	POINT_PROCESS syn_dblexp
	RANGE onset, A1, tau1, A2, tau2, gmax, e, i
	NONSPECIFIC_CURRENT i
}
UNITS {
	(nA) = (nanoamp)
	(mV) = (millivolt)
	(umho) = (micromho)
}

PARAMETER {
	onset=0(ms)
	A1=0.8
	tau1=.3 (ms)
	A2=0.2
	tau2=1.6
	gmax=0 	(umho)
	e=0	(mV)
	v	(mV)
}

ASSIGNED { i (nA)  g (umho)}

BREAKPOINT {
	g = gmax * gdblexp(t-onset)
	i = g*(v - e)
}

FUNCTION gdblexp(x) {
	if (x < 0) {
		gdblexp = 0
	}
	else{
		gdblexp =(A1 *  exp(-(x )/tau1) + A2 *  exp(-(x)/tau2))
	}
}
