import unreal
import json

# Serialize a single Blueprint node into a dictionary format
def serialize_node(node):
    node_type = node.get_class().get_name()  # Get the node's class name (e.g., K2Node_Event)
    node_name = node.get_name()              # Get the node's display name
    pins = node.get_all_pins()               # Retrieve all input/output pins on the node

    pin_data = []
    for pin in pins:
        # For each pin, capture its name, direction, and linked connections
        pin_data.append({
            "name": pin.get_name(),
            "direction": str(pin.get_direction()),
            "linked_to": [linked.get_name() for linked in pin.get_links()]
        })

    # Return the full node structure
    return {
        "node_name": node_name,
        "node_type": node_type,
        "pins": pin_data
    }

# Convert a Blueprint's Event Graph into a JSON representation
def blueprint_to_json(bp):
    try:
        # Attempt to access the Event Graph from the Blueprint asset
        graph = bp.get_editor_property("event_graph")
    except Exception as e:
        print("Failed to get event graph:", str(e))
        return None

    if not graph:
        print("No event graph found.")
        return None

    # Extract all nodes from the graph
    nodes = graph.get_nodes()

    # Serialize each node into a structured format
    serialized_nodes = [serialize_node(n) for n in nodes]

    # Package the Blueprint name and its serialized nodes into a dictionary
    blueprint_data = {
        "blueprint": bp.get_name(),
        "nodes": serialized_nodes
    }

    # Convert the dictionary to a formatted JSON string
    return json.dumps(blueprint_data, indent=2)

# Generate a prompt for the LLM based on the currently selected Blueprint in the editor
def generate_prompt_from_selected_blueprint():
    # Get the currently selected assets in the Unreal Editor
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

    if not selected_assets:
        print("No asset selected.")
        return None

    bp = selected_assets[0]  # Use the first selected asset
    print("Selected asset type:", bp.get_class().get_name())

    # Ensure the selected asset is a Blueprint type
    if not bp.get_class().get_name().endswith("Blueprint"):
        print("Selected asset is not a Blueprint.")
        return None

    # Convert the Blueprint to JSON format
    blueprint_json = blueprint_to_json(bp)
    if not blueprint_json:
        return None

    # Construct the prompt for the LLM to analyze the Blueprint logic
    prompt = f"""
    Here is a Blueprint graph from Unreal Engine. Please explain what it does, suggest improvements, and identify potential logic issues.

    {blueprint_json}
    """
    return prompt
