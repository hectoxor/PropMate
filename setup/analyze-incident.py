def analyze_incident(incident_description):
    manager_prompt = f"Analyze the following incident reported by a resident of the property owners' association: '{incident_description}'. Provide a simplified version and suggest some solutions for the manager."
    resident_prompt = f"Based on the reported incident: '{incident_description}', provide a list of steps the resident can take to improve the situation."

    manager_response = generate_response(manager_prompt, max_tokens=500)
    resident_response = generate_response(resident_prompt, max_tokens=500)

    return manager_response, resident_response
