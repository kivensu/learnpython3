# 将列表传递给函数时，函数可对其进行修改，函数中对列表的任何修改都是永久的
def printed_models(unprinted_designs, completed_models):
    """simulation """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing models: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['Nphnoe X', 'Nphone Xs', 'Nphone XsMax']
completed_models = []
printed_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# 每个函数都应该负责一项具体的工作！
# 还可以把列表的副本传递进去