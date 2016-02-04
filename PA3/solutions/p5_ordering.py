# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'

from p1_is_complete import *
from Queue import PriorityQueue

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """
    if(is_complete(csp)):
        return None

    unassigned = filter(lambda x: not x.is_assigned(), csp.variables)

    # Getting a minimum before looping through all the variables to find the right min
    minimum = len(unassigned[0].domain)
    varFinal = unassigned[0]

    for var in unassigned[1:]:
        if minimum > len(var.domain):
            minimum = len(var.domain)
            varFinal = var
        elif minimum == len(var.domain):
            if (len(csp.constraints[var]) >= len(csp.constraints[varFinal])):
                varFinal = var
            else:
                varFinal = varFinal
            
    return varFinal
            

def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """
    rating = 0 #To prioritize
    queue = PriorityQueue()
    lister = [] #List that is going to be returned
    
    for value in variable.domain:
        rating = 0 #Reset back to 0 for rating of a new value in the domain of the variable
        for constraint in csp.constraints[variable]: #Get the constraints of the variable
            for dim in constraint.var2.domain: #Check with all the value of the constraint varaibles domain to check if the value can be satisfied with these domain values
                if (constraint.is_satisfied(value, dim)):
                    rating = rating + 1
        queue.put((rating, value)) # Ordered by rating
    
    while not queue.empty(): #Putting into a list
        i = 0
        holder = queue.get()
        lister.insert(i, holder[1])
        i = i + 1
    return lister