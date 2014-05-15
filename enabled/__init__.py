import pkgutil

# Set up a list of triggers and functions to execute.
plugin_pairs = []

# Find all packages in the current directory.
for loader, name, ispkg \
    in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)

    # Try to access the module's trigger and execute functions.
    try:
        plugin_pairs.append((name, module.trigger, module.execute))
    except Exception as e:
        print("Skipping module {}: {}".format(name, e))

# Define a convenience function for running all plugins if their
# trigger function returns true.
def execute(**songinfo):
    for pair in plugin_pairs:
        try:
            if pair[1](**songinfo): pair[2](**songinfo)
        except Exception as e:
            print("Module {} caused: {}".format(pair[0], e))
