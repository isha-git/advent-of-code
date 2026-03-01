#!/usr/bin/env python3
"""
Agent System that dynamically creates sub-agents based on input.
"""

import importlib
import sys
from typing import Dict, Callable, Any


class SubAgent:
    """Base class for all sub-agents."""
    
    def __init__(self, name: str):
        self.name = name
    
    def execute(self, *args, **kwargs) -> Any:
        """Execute the sub-agent's task."""
        raise NotImplementedError("Sub-agents must implement the execute method")


class PrimeCheckAgent(SubAgent):
    """Sub-agent for prime number checking."""
    
    def execute(self, n: int) -> Dict[str, Any]:
        """Check if a number is prime."""
        if n <= 1:
            return {"result": False, "message": f"{n} is not a prime number"}
        if n == 2:
            return {"result": True, "message": f"{n} is a prime number"}
        if n % 2 == 0:
            return {"result": False, "message": f"{n} is not a prime number (even)"}
        
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return {"result": False, "message": f"{n} is not a prime number (divisible by {i})"}
        
        return {"result": True, "message": f"{n} is a prime number"}


class EvenOddAgent(SubAgent):
    """Sub-agent for even/odd checking."""
    
    def execute(self, n: int) -> Dict[str, Any]:
        """Check if a number is even or odd."""
        if n % 2 == 0:
            return {"result": "even", "message": f"{n} is an even number"}
        else:
            return {"result": "odd", "message": f"{n} is an odd number"}


class LessThanHundredAgent(SubAgent):
    """Sub-agent for checking if number is less than 100."""
    
    def execute(self, n: int) -> Dict[str, Any]:
        """Check if a number is less than 100."""
        if n < 100:
            return {"result": True, "message": f"{n} is less than 100"}
        else:
            return {"result": False, "message": f"{n} is not less than 100"}


class AgentFactory:
    """Factory for creating sub-agents."""
    
    @staticmethod
    def create_agent(agent_type: str) -> SubAgent:
        """Create a sub-agent based on the specified type."""
        agents = {
            "prime": PrimeCheckAgent,
            "even_odd": EvenOddAgent,
            "less_than_hundred": LessThanHundredAgent,
        }
        
        if agent_type not in agents:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        return agents[agent_type](agent_type)


class MainAgent:
    """Main agent that coordinates sub-agents."""
    
    def __init__(self):
        self.agents: Dict[str, SubAgent] = {}
    
    def create_sub_agent(self, agent_type: str) -> SubAgent:
        """Create and register a sub-agent."""
        agent = AgentFactory.create_agent(agent_type)
        self.agents[agent_type] = agent
        return agent
    
    def execute_task(self, agent_type: str, *args, **kwargs) -> Any:
        """Execute a task using the specified sub-agent."""
        if agent_type not in self.agents:
            self.create_sub_agent(agent_type)
        
        return self.agents[agent_type].execute(*args, **kwargs)
    
    def run_all_checks(self, n: int) -> Dict[str, Any]:
        """Run all available checks on a number."""
        results = {}
        
        # Create and run all agents
        prime_agent = self.create_sub_agent("prime")
        even_odd_agent = self.create_sub_agent("even_odd")
        hundred_agent = self.create_sub_agent("less_than_hundred")
        
        results["prime"] = prime_agent.execute(n)
        results["even_odd"] = even_odd_agent.execute(n)
        results["less_than_hundred"] = hundred_agent.execute(n)
        
        return results


def main():
    """Main entry point."""
    agent = MainAgent()
    
    try:
        num = int(input("Enter a number to analyze: "))
        results = agent.run_all_checks(num)
        
        print("\n" + "="*50)
        print(f"Analysis Results for {num}:")
        print("="*50)
        
        for check_name, check_result in results.items():
            print(f"\n{check_name.replace('_', ' ').title()}: {check_result['message']}")
        
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()