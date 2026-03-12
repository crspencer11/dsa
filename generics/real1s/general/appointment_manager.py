import json

# Available tools!!!
def schedule_appointment(patient_name, date, time):
    return f"Appointment scheduled for {patient_name} on {date} at {time}"

def cancel_appointment(patient_name):
    return f"Appointment cancelled for {patient_name}"

TOOLS = {
    "schedule_appointment": schedule_appointment,
    "cancel_appointment": cancel_appointment,
}

def execute_tool(llm_output: str):
    data = json.loads(llm_output)

    tool = data["tool"]
    args = data["arguments"]

    if tool not in TOOLS:
        raise ValueError(f"Unknown tool: {tool}")

    return TOOLS[tool](**args)