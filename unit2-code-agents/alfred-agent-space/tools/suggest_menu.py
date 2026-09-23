from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "suggest_menu"
    description = "Suggests a menu based on the occasion. Use one of the allowed occasion values."
    inputs = {
        'occasion': {
            'type': 'string',
            'description': 'The type of occasion. Must be exactly one of: "casual", "formal", "superhero", "custom".'
        }
    }
    output_type = "string"

    def forward(self, occasion: str) -> str:
        occasion = occasion.lower()
        if "casual" in occasion:
            return "Pizza, snacks, and drinks."
        elif "formal" in occasion:
            return "3-course dinner with wine and dessert."
        elif "superhero" in occasion:
            return "Buffet with high-energy and healthy food."
        else:
            return "Custom menu for the butler."