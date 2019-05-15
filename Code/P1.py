from search import Problem
import utils
import copy

class WaterJugProblem(Problem):
    
    def __init__(self, init_state, final_state, max_qty):
        Problem.__init__(self, init_state, final_state)
        self.max_qty = max_qty


    def actions(self, state):
        ret_actions = []

        for i in range(len(state)):
            new_action = dict()

            if state[i] == 0:
                new_action[i] = self.max_qty[i]
            elif state[i] != self.max_qty[i]:
                new_action[i] = -state[i]
                ret_actions.append(new_action)
                new_action[i] = self.max_qty[i] - state[i]
            else:
                new_action[i] = -state[i]
            
            ret_actions.append(new_action)

        for i in range(len(state)):
            for j in range(len(state)):
                new_action = dict()
                
                if i == j:
                    continue

                move_qty = min(state[i], self.max_qty[j] - state[j])
                new_action[i] = -move_qty
                new_action[j] = move_qty

                ret_actions.append(new_action)

        return ret_actions

    
    def result(self, state, action):
        new_state = list(copy.deepcopy(state))

        for key, value in action.items():
            new_state[key] += value

        new_state = tuple(new_state)
        return new_state


    def h(self, node):
        sum = 0

        for i in range(len(node.state)):
            sum += abs(node.state[i] - self.goal[i])

        return sum
