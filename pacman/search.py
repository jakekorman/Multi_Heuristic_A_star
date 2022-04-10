
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
          state: pacman state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: pacman state

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
    return  [s, s, w, s, w, w, s, w]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """pacman the node that has the lowest combined cost and heuristic first."""

    startState = problem.get_start_state()
    #a * using priority queue so as to prioriize the successors with least
    #heuristic cost
    fringe = util.PriorityQueue()
    visited = []

    #the fringe apart from the state , action, cost also has combined cost 0 here
    #of which is we want the least combined cost first
    fringe.push((startState, [], 0), 0)

    #keep popping till no more nodes in the fringe
    while not fringe.isEmpty():
        currentState, actions, costs = fringe.pop()
        #curcial as this prevents expanding the same node twice
        if not currentState in visited:
            #update visited status
            visited.append(currentState)
            #if this goal state return the actions to reach it
            if problem.is_goal_state(currentState):
                return actions
            #push all successors not in visited
            for state, action, cost in problem.get_successors(currentState):
                if not state in visited:
                    # update cost to reflect combined path and heuristic cost
                    # and prioritize the least for popping as the priority queue
                    # is implemented using heapq which pops smallest element
                    # first and pushes such to maintain this order
                    heuristicCost = costs + cost + heuristic(state, problem)
                    fringe.push((state, actions + [action], costs + cost), heuristicCost)


def WaStarSearch(problem, heuristic=nullHeuristic, weight=1):
    """pacman the node that has the lowest combined cost and heuristic first where the heuristic is weighted."""

    startState = problem.get_start_state()
    #a * using priority queue so as to prioriize the successors with least
    #heuristic cost
    fringe = util.PriorityQueue()
    visited = []

    #the fringe apart from the state , action, cost also has combined cost 0 here
    #of which is we want the least combined cost first
    fringe.push((startState, [], 0), 0 )

    #keep popping till no more nodes in the fringe
    while not fringe.isEmpty():
        currentState, actions, costs = fringe.pop()
        #curcial as this prevents expanding the same node twice
        if not currentState in visited:
            #update visited status
            visited.append(currentState)
            #if this goal state return the actions to reach it
            if problem.is_goal_state(currentState):
                return actions
            #push all successors not in visited
            for state, action, cost in problem.get_successors(currentState):
                if not state in visited:
                    #update cost to reflect combined path and heuristic cost
                    # and prioritize the least for popping as the priority queue
                    # is implemeneted using heapq which pops smallest element
                    # first and pushes such to maintain this order
                    heuristicCost = costs + cost + weight * heuristic(state, problem)
                    fringe.push((state, actions + [action], costs + cost), heuristicCost)
    util.raiseNotDefined()

# Abbreviations
astar = aStarSearch
