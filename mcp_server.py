"""MCP Server for Max-Sum Factor Graph Skill."""
import json
import sys
from client import MaxSumFactorGraph

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "solve_max_sum",
                            "description": "Solve coordination chain using Max-Sum belief propagation",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "node_costs": {"type": "object"},
                                    "edge_matrix": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    }
                                },
                                "required": ["node_costs", "edge_matrix"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                compat = {("A", "B"): args["edge_matrix"]}
                out = MaxSumFactorGraph.solve_simple_chain(args["node_costs"], compat)
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"optimal_assignment": out})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
