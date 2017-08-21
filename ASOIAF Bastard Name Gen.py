regions = ['The North', 'Iron Islands', 'Riverlands', 'The Reach', 'Westerlands', 'Crownlands', 'Stormlands', 'The Vale', 'Dorne']
print('This Program Outputs a Bastard Name Depending on Your Birthplace.')
print('What is your desired first name?')
firstName = input()
print('Where in the 9 regions were you born, ' + firstName + '?')
print(regions)
birthPlace = input()
baseName = birthPlace

def bastard(location):
    if location == 'The North':
        baseName = 'Snow'
    elif location == 'Iron Islands':
        baseName = 'Pyke'
    elif location == 'Riverlands':
        baseName = 'Rivers'
    elif location == 'The Reach':
        baseName = 'Flowers'
    elif location == 'Westerlands':
        baseName = 'Hill'
    elif location == 'Crownlands':
        baseName = 'Waters'
    elif location == 'Stormlands':
        baseName = 'Storm'
    elif location == 'The Vale':
        baseName = 'Stone'
    elif location == 'Dorne':
        baseName = 'Sand'
    else:
        baseName = 'of ' + location
    return (baseName)

print('Your Westeros Full Name is: ' + firstName + ' ' + bastard(birthPlace))

