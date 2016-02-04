# -*- coding: utf-8 -*-
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from collections import deque
from p1_is_complete import *
from p2_is_consistent import *
from p5_ordering import *
from p4_ac3 import revise

def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """
    if is_complete(csp):
        return True
    uvar = select_unassigned_variable(csp)
    for value in order_domain_values(csp, uvar):
        if is_consistent(csp, uvar, value):
            csp.variables.begin_transaction()
            if(inference(csp, uvar) != False):
                uvar.assign(value)
            outcome = backtrack(csp)
            if outcome != False:
                return True
            csp.variables.rollback()
    return False

def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise.  Note that this method does not
    return any additional variable assignments (for simplicity)."""

    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())

    while queue_arcs:                               
        (xi, xy) = queue_arcs.pop() 
        temp = revise(csp, xi, xy)  
        if(temp[0]):  
            if (temp[1] == 0):
                return False                     
            for constraint in csp.constraints[xi]:
                if(constraint.var2 != xy):
                    tup = (constraint.var2, constraint.var1)
                    if tup not in queue_arcs:
                        queue_arcs.append(tup)
    return True