import xml.dom.minidom
import re
import pandas as pd

def count_child_nodes(go_id, parent_child_relations):
    # Helper function to calculate the number of child nodes for a given GO ID

    if go_id not in parent_child_relations:
        return 0

    child_nodes = parent_child_relations[go_id]
    count = len(child_nodes)

    for child_node in child_nodes:
        # Recursively call count_child_nodes() to calculate the number of child nodes of the child nodes
        count += count_child_nodes(child_node, parent_child_relations)

    return count


dom = xml.dom.minidom.parse("go_obo.xml")
term_elements = dom.getElementsByTagName("term")

parent_child_relations = {}

# First iteration: Build the parent-child relations dictionary
for term_element in term_elements:
    go_id = term_element.getElementsByTagName("id")[0].firstChild.data
    is_a_elements = term_element.getElementsByTagName("is_a")
    for is_a_element in is_a_elements:
        is_a_id = is_a_element.firstChild.data.strip().split(' ! ')[0]
        if is_a_id not in parent_child_relations:
            parent_child_relations[is_a_id] = []
        parent_child_relations[is_a_id].append(go_id)

id_list = []
name_list = []
defstr_list = []
child_count_list = []

# Second iteration: Process terms with "autophagosome" condition
for term_element in term_elements:
    defstr_element = term_element.getElementsByTagName("def")[0].getElementsByTagName("defstr")[0]
    defstr_value = defstr_element.firstChild.data
    match_autophagosome = re.search('autophagosome', defstr_value)
    if match_autophagosome:
        id_element = term_element.getElementsByTagName("id")[0]
        id_value = id_element.firstChild.data

        name_element = term_element.getElementsByTagName("name")[0]
        name_value = name_element.firstChild.data

        id_list.append(id_value)
        name_list.append(name_value)
        defstr_list.append(defstr_value)

        is_a_count = count_child_nodes(id_value, parent_child_relations)
        child_count_list.append(str(is_a_count))

df = pd.DataFrame({'ID': id_list, 'Name': name_list, 'Defstr': defstr_list, 'Child Count': child_count_list})

id_str = ",".join(id_list)
name_str = ",".join(name_list)
defstr_str = ",".join(defstr_list)
child_count_str = ",".join(child_count_list)

print("ID:", id_str)
print("Name:", name_str)
print("Defstr:", defstr_str)
print("Child Count:", child_count_str)

df.to_excel('autophagosome.xlsx', index=False)
