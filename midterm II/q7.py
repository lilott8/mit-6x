'''
Write a Monte Carlo simulation that estimates the probability of a student having a final score >= 70 and <= 75. Assume that 10,000 trials are sufficient to provide an accurate answer.
'''

import random, pylab
def sampleQuizzes():
    yes = 0
    no = 0
    trials = 10000
    for x in range(trials):
        prob = 0
        finalScore = generateRandomGrades()
        if finalScore >= 70.0 and finalScore <=75.0:
            yes += 1
        else:
            no += 1
    return float(yes)/float(trials)
    
    
def generateRandomGrades():
    m1, m2 = .25 * random.randrange(50,80), .25 * random.randrange(50,80)
    f = .5 * random.randrange(55,95)
    return m1 + m2 + f

#sampleQuizzes()

def plotQuizzes():
    numTrials = 10000
    scores = []
    mean = 0
    scores = generateScores(numTrials)
    mean = scores[-1]
    del scores[-1]
    pylab.hist(scores, bins=7, range=(55,90))#, normed=1)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()
    

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the mean score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    finalGrades = []
    for x in range(numTrials):
        m1 = .25 * random.randrange(50,80)
        m2 = .25 * random.randrange(50,80)
        f =.5 * random.randrange(55,95)
        finalGrades.append(m1 + m2 + f)
    finalGrades.append(sum(finalGrades)/numTrials)
    return finalGrades
        
        
plotQuizzes()