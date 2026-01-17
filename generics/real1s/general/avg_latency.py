from typing import List

def find_avg_latency(logs: List[dict]) -> dict:
    """input:
    logs = [
        {"service": "auth", "latency": 120},
        {"service": "payments", "latency": 300},
        {"service": "auth", "latency": 80},
    ]

    output: return avg latency per service
    {
        "auth": 100,
        "payments": 300
    }
    """
    output = {}
    if logs:
        intermediate = build_intermediate(logs)
        for service, values in intermediate.items():
            output[service] = values[0] // values[1]
    return output

        
def build_intermediate(logs: List[dict]) -> dict:
    output = {}
    for log in logs:
        if log['service'] in output:
            output[log['service']][0] += log['latency']
            output[log['service']][1] += 1
        else:
            output[log['service']] = [log['latency'], 1]
    return output

print(find_avg_latency(logs = [
        {"service": "auth", "latency": 120},
        {"service": "payments", "latency": 300},
        {"service": "auth", "latency": 80},
    ]))