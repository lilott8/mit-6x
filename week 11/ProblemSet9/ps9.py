# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b_precompiled_27 import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    steps = [300,150,75,0]
    numTrials = 10
    averages = [False] * (steps[0] + 150)
    avg_resist = [False] * (steps[0] + 150)
    averageResults = [False] * len(steps)
    avgResistResults = [False] * len(steps)
    #Virus stuff
    maxBirthProb = .1
    clearProb = .05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = .005
    numViruses = 100
    #TreatedPatient stuff
    maxPop = 1000
    stepsAfterDrugs = 150
    for super in range(len(steps)):
        #Number of trials
        for t in range(numTrials):
            #Create the Viruses
            viruses = [ResistantVirus(maxBirthProb, clearProb,
                                      resistances, mutProb)
                       for _ in range(numViruses)]
            #Put the viruses into our patient
            tp = TreatedPatient(viruses, maxPop)
            #Step through our model without drugs
            for step in range(steps[super]):
                #print step
                averages[step] += tp.update()
                avg_resist[step] += tp.getResistPop(['guttagonol'])
            #Add our drug    
            tp.addPrescription('guttagonol')
            #Lets check our stages now 
            for sad in range(stepsAfterDrugs):
                averages[sad+step] += tp.update()
                avg_resist[step+sad] += tp.getResistPop(['guttagonol'])
        averageResults.append(averages)
        avgResistResults.append(avg_resist)
    
    #print averageResults
    print avgResistResults
    for i in range(len(avgResistResults)):
        if i is not False:
            for x in range(len(avgResistResults[i])):
                avgResistResults[x] /= numTrials
                averageResults[x] /= numTrials
    #print averageResults
    #print avgResistResult



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    
simulationDelayedTreatment(100)