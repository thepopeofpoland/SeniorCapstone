import json
family_data = {"Smith": 3}


def list_data():
    return family_data


def add_date():
    pass
    # save date as sqlite date type text and look at the python calendar module.


def add_family(sir_name, family_members):
    family_data[sir_name] = family_members


def update_family(family_members):
    """
           Modifies an entry to the fishing Data

           :param num: provide the new updated ice depth
           :type num: integer
           """
    fam_name = family_data["Smith"]
    print(fam_name)
    family_data["Smith"] = family_members
    return family_data


def clear_data():
    family_data.clear()


def save():
    with open('family_data', 'w') as f:
        json.dump(family_data, f)


def load():
    with open('family_data', 'r') as f:
        family_data.update(json.load(f))
