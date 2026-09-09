"""Example usage for Max-Sum Factor Graph Skill."""
from client import MaxSumFactorGraph

def main():
    print("Executing Max-Sum Factor Graph...")
    node_costs = {"A": [2.0, 5.0], "B": [1.0, 4.0]}
    compat = {("A", "B"): [[3.0, 1.0], [0.0, 6.0]]}
    solution = MaxSumFactorGraph.solve_simple_chain(node_costs, compat)
    print("Optimal Coordination Assignment:", solution)
    assert solution["A"] == 1 and solution["B"] == 1
    print("Max-Sum Factor Graph verified successfully!")

if __name__ == "__main__":
    main()
