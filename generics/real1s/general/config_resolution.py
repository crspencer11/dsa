# def config(defaults, overrides):
#     """
#     defaults = {"timeout": 30, "retries": 3}
#     overrides = [
#         {"env": "prod", "timeout": 60},
#         {"env": "staging", "retries": 1},
#     ]
#     output:
#     {
#         "prod": {"timeout": 60, "retries": 3}
#         ...
#     }
#     """
#     output = {}
#     for override in overrides:
#         output.update(override['env'], defaults) 

#     for override in overrides:
#         output[overrides['env']][override[1]] = override[1].value()
    
#     print(output)
#     return output

# config(defaults = {"timeout": 30, "retries": 3},
#     overrides = [
#         {"env": "prod", "timeout": 60},
#         {"env": "staging", "retries": 1},
#     ])
import json

with open("/Users/lilblick/Projects/dsa/generics/real1s/general/prompts.json") as f:
    PROMPTS = json.load(f)
    print("Loaded prompts:", PROMPTS.items())