

# Import the xmltodict library
import xmltodict

# Open the sample xml file and read it into variable
with open("xml_example.xml") as f:
    xml_example = f.read()

# Print the raw XML data
print('\nThis is the raw XML: \n')
print(xml_example)

# Parse the XML into a Python dictionary
xml_dict = xmltodict.parse(xml_example)
print('\nThis is the dictionary of the imported XML: \n')
print(xml_dict)

# Save the interface name into a variable using XML nodes as keys
int_name = xml_dict["interface"]["name"]
print('\nThis is the interface name from the dictionary: \n')
print(int_name)

int_addr = xml_dict["interface"]["ipv4"]["address"]["ip"]
print('\nThis is the interface address now from the dictionary: \n')
print(int_addr)
# Change the IP address of the interface
xml_dict["interface"]["ipv4"]["address"]["ip"] = "99.99.99.99"

int_addr = xml_dict["interface"]["ipv4"]["address"]["ip"]
print('\nThis is the interface address now from the dictionary: \n')
print(int_addr)

# Revert to the XML string version of the dictionary
print('\nThis is the raw XML now: \n')
print(xmltodict.unparse(xml_dict))
