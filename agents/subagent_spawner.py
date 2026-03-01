"""
Sub-Agent Spawner

This module implements an agent that can spawn multiple sub-agents to handle
different tasks in parallel.
"""

import concurrent.futures
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import threading


@dataclass
class SubAgent:
    """Represents an individual sub-agent with its task and status."""
    agent_id: str
    task: str
    status: str = "pending"
    result: Optional[Any] = None
    error: Optional[str] = None
    
    def execute(self) -> None:
        """Execute the sub-agent's task."""
        try:
            self.status = "executing"
            # Simulate task execution
            # In a real implementation, this would call the actual agent logic
            self.result = f"Completed task: {self.task}"
            self.status = "completed"
        except Exception as e:
            self.status = "failed"
            self.error = str(e)


class SubAgentSpawner:
    """Main agent that spawns and manages sub-agents."""
    
    def __init__(self):
        self.sub_agents: List[SubAgent] = []
        self.lock = threading.Lock()
    
    def create_sub_agents(self, tasks: List[str]) -> None:
        """Create sub-agents for each task."""
        with self.lock:
            self.sub_agents = [
                SubAgent(agent_id=f"agent_{i}", task=task)
                for i, task in enumerate(tasks)
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
                        "task": agent.task,
                        "status": agent.status,
                        "result": agent.result,
                        "error": agent.error
                    }
                    for agent in self.sub_agents
                ]
            }


def main():
    """Example usage of the SubAgentSpawner."""
    # Create the spawner
    spawner = SubAgentSpawner()
    
    # Define some tasks
    tasks = [
        "Process data from source A",
        "Analyze sentiment of customer reviews",
        "Generate report for Q3 2023",
        "Update database with new records",
        "Send notification emails"
    ]
    
    # Create sub-agents for each task
    spawner.create_sub_agents(tasks)
    print(f"Created {len(tasks)} sub-agents")
    
    # Execute all sub-agents
    print("Executing all sub-agents...")
    spawner.execute_all()
    
    # Get and display status
    status = spawner.get_status()
    print(f"\nExecution complete. Status:")
    print(f"Total agents: {status['total_agents']}")
    print(f"Completed: {status['status_count']['completed']}")
    print(f"Failed: {status['status_count']['failed']}")
    
    # Show individual results
    print("\nIndividual results:")
    for agent in status['agents']:
        print(f"- {agent['agent_id']}: {agent['status']} - {agent['result']}")


if __name__ == "__main__":
    main()