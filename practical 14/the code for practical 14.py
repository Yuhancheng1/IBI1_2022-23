import xml.dom.minidom
import re
import pandas as pd

# Parse the XML file
dom = xml.dom.minidom.parse('go_obo.xml')
root = dom.documentElement
term_elements = root.getElementsByTagName('term')

data = []
id_list = []
name_list = []
defstr_list = []
child_count_list = []

# Dictionary to store the child counts for each term
child_counts = {}

# Iterate over each term element
for term_element in term_elements:
    # Get the ID, name, and defstr values
    id_element = term_element.getElementsByTagName('id')[0]
    id_value = id_element.firstChild.data

    name_element = term_element.getElementsByTagName('name')[0]
    name_value = name_element.firstChild.data

    def_element = term_element.getElementsByTagName('def')[0]
    defstr_element = def_element.getElementsByTagName('defstr')[0]
    defstr_value = defstr_element.firstChild.data

    # Check if defstr contains 'autophagosome'
    match_autophagosome = re.search('autophagosome', defstr_value)

    # If 'autophagosome' is found, add the values to the respective lists
    if match_autophagosome:
        id_list.append(id_value)
        name_list.append(name_value)
        defstr_list.append(defstr_value)

    # Store the child count for the current term
    child_counts[id_value] = 0

# Iterate over each term element again to count the child nodes
for term_element in term_elements:
    is_a_elements = term_element.getElementsByTagName('is_a')

    if is_a_elements:
        # Iterate over each is_a element
        for is_a_element in is_a_elements:
            # Get the parent term ID
            parent_id = is_a_element.firstChild.data.strip().split(' ! ')[0]

            # Increment the child count for the parent term
            child_counts[parent_id] = child_counts.get(parent_id, 0) + 1

# Add child counts to the child_count_list
for id_value in id_list:
    child_count_list.append(str(child_counts[id_value]))

# Create a DataFrame from the collected data
df = pd.DataFrame({'ID': id_list, 'Name': name_list, 'Defstr': defstr_list, 'Child Count': child_count_list})

# Convert the lists to comma-separated strings
id_str = ",".join(id_list)
name_str = ",".join(name_list)
defstr_str = ",".join(defstr_list)
child_count_str = ",".join(child_count_list)

# Print the results
print("ID:", id_str)
print("Name:", name_str)
print("Defstr:", defstr_str)
print("Child Count:", child_count_str)

# Export the DataFrame to an Excel file
df.to_excel('autophagosome.xlsx', index=False)
