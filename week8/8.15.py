def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case', 'mug', 'tupperware']
completed_models = []

print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)