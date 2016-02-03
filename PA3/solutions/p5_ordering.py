# -*- coding: utf-8 -*-
__author__ = 'Sivasubramanian Chandrasegarampillai, Walter Curnow'
__email__ = 'rchandra@uci.edu,wcurnow@uci.edu'

from p1_is_complete import *

def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
    the variable with the smallest number of values left in its available domain.  If MRV ties,
    then it picks the variable that is involved in the largest number of constraints on other
    unassigned variables.
    """

    # TODO implement this
    minimum = -1

    if(is_complete(csp)):
        return None

    unassigned = filter(lambda x: not x.is_assigned(), csp.variables)

    for var in unassigned:
        if not var.is_assigned():
            minimum = len(var.domain)
            varia = var
            break

    for var in unassigned:
        if not var.is_assigned():
            if minimum < len(var.domain):
                minimum = len(var.domain)
                varia = var
            elif minimum <= len(var.domain):
                for constraint in csp.constraints
                    minimum = len

    for 
    return varia
            

def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    This method implements the least-constraining-value (LCV) heuristic; that is, the value
    that rules out the fewest choices for the neighboring variables in the constraint graph
    are placed before others.
    """

    # TODO implement this
    pass
