# -*- coding: utf-8 -*-
__author__ = 'Please write your names, separated by commas.'
__email__ = 'Please write your email addresses, separated by commas.'

from collections import deque

def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.

    If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
    for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
    in the queue.

    Note that the current domain of each variable can be retrieved by 'variable.domains'.

    This method returns True if the arc consistency check succeeds, and False otherwise."""

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

def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    removed = False
    check = []
    checker = True
    for constraint in csp.constraints[xi,xj]:
        for x in xi.domain:
            for y in xj.domain:
                if(constraint.is_satisfied(x,y)):
                    check.append(x)
                    break
    if (len(check) != len(xi.domain)):
        removed = True
    return (removed, len(check))