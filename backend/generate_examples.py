import time
import ujson


'''
This script is supposed to generate the example parameters for each endpoint
in the schema/openapi-3.0.0.json
'''

# Load the schema using ujson
time_start_ujson = time.time()
with open('schema/openapi-3.0.0.json', 'r') as f:
    schema = ujson.load(f)
time_end_ujson = time.time()
print(f'Loading the schema in {round(time_end_ujson - time_start_ujson, 3)} seconds')


# Get the paths
paths = schema['paths']

# Get a list of all possible parameters for all endpoints
parameters = []
for path, path_obj in paths.items():
    # Only consider objects that represent HTTP methods
    methods = [method for method in path_obj if method.startswith('x-') or method.upper() in ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')]
    for method in methods:
        if 'parameters' in path_obj[method]:
            for parameter in path_obj[method]['parameters']:
                if parameter not in parameters and parameter['required']:
                    parameters.append(parameter)

# Write the parameters to a file
with open('schema/parameters.json', 'w') as f:
    ujson.dump(parameters, f, indent=2)

# Print the number of parameters
print(f'Found {len(parameters)} required parameters')