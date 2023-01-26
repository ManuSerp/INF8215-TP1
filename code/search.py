# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    """


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
    """

    init_pos=problem.getStartState()
    fifo=[(init_pos,None,0,None)] # node structure =[pos,action,cost,parent]
    already_seen=[] #list where we stock every visited node in chained tuple
    control=[] #list where we stock every visited postition
    node=fifo.pop(0) #exploration of the graph
    while not problem.isGoalState(node[0]):
        successor=problem.getSuccessors(node[0])
        already_seen.append(node)
        control.append(node[0])
        for node_neigh in successor:
            if not node_neigh[0] in control:
                fifo.append((node_neigh[0],node_neigh[1],node_neigh[2],node))
        node=fifo.pop(0)
    
    actions_list=[]
    action=node[1]
    while action: #On remonte la liste chainée à partir du noeud objectif pour trouver le chemin.
        actions_list.append(action)
        node=node[3]
        action=node[1]

    return actions_list[::-1]
    








def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    """
    init_pos=problem.getStartState()
    fringe=[(init_pos,None,0,None)] # node structure =[pos,action,cost,parent]
    already_seen=[] #list where we stock every visited node in chained tuple
    control=[] #list where we stock every visited position
    node=fringe.pop(0) #exploration of the graph
   
    while not problem.isGoalState(node[0]):
        successor=problem.getSuccessors(node[0])
        already_seen.append(node)
        control.append(node[0])
        for node_neigh in successor:
            if not node_neigh[0] in control:
                fringe.append((node_neigh[0],node_neigh[1],node_neigh[2],node))
        
        # choix du noeud de cout le plus faible
        node=fringe[0]
        cost=node[2]
        index=0
        for i,n in enumerate(fringe):
            if n[2]<cost:
                cost=n[2]
                node=n
                index=i
        fringe.pop(index)
        

    actions_list=[]
    action=node[1]
    while action: #On remonte la liste chainée à partir du noeud objectif pour trouver le chemin.
        actions_list.append(action)
        node=node[3]
        action=node[1]

    return actions_list[::-1]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    """
        INSÉREZ VOTRE SOLUTION À LA QUESTION 4 ICI
    """



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
