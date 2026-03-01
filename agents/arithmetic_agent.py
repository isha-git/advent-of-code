"""
Arithmetic Agent System

This module implements a main agent that spawns multiple sub-agents,
each capable of performing different basic arithmetic operations.
"""

import concurrent.futures
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
import threading
import random


@dataclass
class ArithmeticSubAgent:
    """Represents a sub-agent that performs a specific arithmetic operation."""
    agent_id: str
    operation: str
    operand1: float
    operand2: float
    status: str = "pending"
    result: Optional[float] = None
    error: Optional[str] = None
    
    def execute(self) -> None:
        """Execute the arithmetic operation."""
        try:
            self.status = "executing"
            
            if self.operation == "add":
                self.result = self.operand1 + self.operand2
            elif self.operation == "subtract":
                self.result = self.operand1 - self.operand2
            elif self.operation == "multiply":
                self.result = self.operand1 * self.operand2
            elif self.operation == "divide":
                if self.operand2 == 0:
                    raise ValueError("Division by zero")
                self.result = self.operand1 / self.operand2
            else:
                raise ValueError(f"Unknown operation: {self.operation}")
                
            self.status = "completed"
        except Exception as e:
            self.status = "failed"
            self.error = str(e)


class ArithmeticAgent:
    """Main agent that spawns and manages arithmetic sub-agents."""
    
    def __init__(self):
        self.sub_agents: List[ArithmeticSubAgent] = []
        self.lock = threading.Lock()
    
    def create_arithmetic_agents(self, operations: List[str], 
                                operands: List[Tuple[float, float]]) -> None:
        """Create sub-agents for each arithmetic operation."""
        if len(operations) != len(operands):
            raise ValueError("Operations and operands lists must have the same length")
            
        with self.lock:
            self.sub_agents = [
                ArithmeticSubAgent(
                    agent_id=f"arithmetic_agent_{i}",
                    operation=operation,
                    operand1=operand_pair[0],
                    operand2=operand_pair[1]
                )
                for i, (operation, operand_pair) in enumerate(zip(operations, operands))
            ]
    
    def execute_all(self) -> None:
        """Execute all sub-agents in parallel."""
        if not self.sub_agents:
            return
            
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(agent.execute) for agent in self.sub_agents]
            concurrent.futures.wait(futures)
    
    def get_status(self) -> Dict[str, Any]:
        """Get the current status of all sub-agents."""
        with self.lock:
            return {
                "total_agents": len(self.sub_agents),
                "status_count": {
                    "pending": sum(1 for agent in self.sub_agents if agent.status == "pending"),
                    "executing": sum(1 for agent in self.sub_agents if agent.status == "executing"),
                    "completed": sum(1 for agent in self.sub_agents if agent.status == "completed"),
                    "failed": sum(1 for agent in self.sub_agents if agent.status == "failed")
                },
                "agents": [
                    {
                        "agent_id": agent.agent_id,
                        "operation": agent.operation,
                        "operand1": agent.operand1,
                        "operand2": agent.operand2,
                        "status": agent.status,
                        "result": agent.result,
                        "error": agent.error
                    }
                    for agent in self.sub_agents
                ]
            }


def main():
    """Example usage of the ArithmeticAgent."""
    # Create the arithmetic agent
    agent = ArithmeticAgent()
    
    # Define arithmetic operations and operands
    operations = ["add", "subtract", "multiply", "divide", "add"]
    operands = [
        (15.5, 7.3),
        (20.0, 8.5),
        (6.0, 4.0),
        (100.0, 25.0),
        (12.7, 3.8)
    ]
    
    # Create sub-agents for each operation
    agent.create_arithmetic_agents(operations, operands)
    print(f"Created {len(operations)} arithmetic sub-agents")
    
    # Execute all sub-agents
    print("Executing arithmetic operations...")
    agent.execute_all()
    
    # Get and display status
    status = agent.get_status()
    print(f"\nExecution complete. Status:")
    print(f"Total agents: {status['total_agents']}")
    print(f"Completed: {status['status_count']['completed']}")
    print(f"Failed: {status['status_count']['failed']}")
    
    # Show individual results
    print("\nArithmetic results:")
    for agent_data in status['agents']:
        operation_symbol = {
            "add": "+",
            "subtract": "-", 
            "multiply": "×",
            "divide": "÷"
        }.get(agent_data['operation'], "?")
        
        result_str = f"{agent_data['result']}" if agent_data['result'] is not None else "N/A"
        error_str = f" (Error: {agent_data['error']})" if agent_data['error'] else ""
        
        print(f"- {agent_data['agent_id']}: {agent_data['operand1']} {operation_symbol} {agent_data['operand2']} = {result_str}{error_str}")


if __name__ == "__main__":
    main()
