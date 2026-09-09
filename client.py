"""
Autonomous Agent Max-Sum Factor Graph Skill
Pure Python Standard Library implementation.
"""
from typing import List, Dict, Tuple, Any

class MaxSumFactorGraph:
    """
    Max-Sum Belief Propagation on factor graphs for decentralized DCOP.
    """
    @staticmethod
    def solve_simple_chain(node_costs: Dict[str, List[float]], 
                           edge_compatibility: Dict[Tuple[str, str], List[List[float]]]) -> Dict[str, int]:
        edge = ("A", "B")
        compat = edge_compatibility[edge]

        msg_A_to_B = []
        for x_B in range(len(node_costs["B"])):
            best = max(node_costs["A"][x_A] + compat[x_A][x_B] for x_A in range(len(node_costs["A"])))
            msg_A_to_B.append(best)

        belief_B = [node_costs["B"][x_B] + msg_A_to_B[x_B] for x_B in range(len(node_costs["B"]))]
        opt_B = int(max(range(len(belief_B)), key=lambda i: belief_B[i]))

        opt_A = int(max(range(len(node_costs["A"])), key=lambda x_A: node_costs["A"][x_A] + compat[x_A][opt_B]))
        return {"A": opt_A, "B": opt_B}
