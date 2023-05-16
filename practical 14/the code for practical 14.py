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

    # Count the number of is_a child elements
    child_count = len(term_element.getElementsByTagName('is_a'))

    # Check if defstr contains 'autophagosome'
    match_autophagosome = re.search('autophagosome', defstr_value)

    # If 'autophagosome' is found, add the values to the respective lists
    if match_autophagosome:
        id_list.append(id_value)
        name_list.append(name_value)
        defstr_list.append(defstr_value)
        child_count_list.append(str(child_count))
        data.append([id_value, name_value, defstr_value, child_count])

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=['ID', 'Name', 'Defstr', 'Child Count'])

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
