import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import netrw

def plot_property_values_over_time(propvals, ylabel = '' ):
    """
    Plot how a network property changes over time during a rewiring process.
    
    Parameters
    ----------
    propvals : Dictionary
        Dictionary of output from properties_overtime.
        The keys are the iteration number and the values are a list of the network property calculated
        at each step of the rewiring process.
    ylabel: string, optional
        Label for y axis of graph for mean and standard deviation of network property
        Default is no label.
    
    Returns
    -------
    property_dict: dictionary
        Dictionary of output where the keys are the iteration number and the values are a list of the network property calculated
        at each step of the rewiring process.

    """
    alllist = [] # list of all properties for all iterations at each of the time steps
    for k in range(len(propvals[0])):
        alllist.append([])
        for l in range(len(list(propvals.keys()))):
            alllist[k].append(propvals[l][k])
            
    # find mean and standard deviation over different iterations of rewiring process        
    meanlist = []
    sdlist = []
    for k in range(len(propvals[0])):
        meanlist.append(np.mean(alllist[k]))
        sdlist.append(np.std(alllist[k]))

    # find upper and lower bound of standard deviation interval around the mean
    upperbd = []
    lowerbd = []
    for a in range(len(meanlist)):
        upperbd.append(meanlist[a]+sdlist[a])
        lowerbd.append(meanlist[a]-sdlist[a])

    fig, (ax0) = plt.subplots(nrows=1)
    ax0.plot(range(len(propvals[0])), meanlist, color = 'blue')
    ax0.plot(range(len(propvals[0])), upperbd, color = 'blue')
    ax0.plot(range(len(propvals[0])), lowerbd, color = 'blue')
    ax0.fill_between(range(len(propvals[0])),upperbd, lowerbd, color = 'cornflowerblue')

    ax0.set_xlabel('number of rewiring steps')
    ax0.set_ylabel(ylabel)

    fig.show()

    return fig 