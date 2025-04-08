def formatNames(names):
    # Get names
    # Syntax: [1:]
    # The above means grab all items starting at index 1 of the array to the end of the array
    firstNames = []
    lastNames = []
    abbreviatedNames = []

    for name in names[1:]:
        # Finds first space in name string
        index = name.find(" ")

        # First name
        # The part [0:index] means to grab everything starting at index 0 and going up until "index"    (which in this case is the first space detected in the string)
        firstName = name[0:index]
        firstNames.append(firstName)

        # Last name(s)
        lastName = name[index:]
        lastNames.append(lastName)

        abbreviatedName = firstName[0] + ". " + lastName
        abbreviatedNames.append(abbreviatedName)

    return {
        "first": firstNames,
        "last": lastNames,
        "fullname": names[1:],
        "abbreviatedname": abbreviatedNames,
    }


def formatHometown(hometowns):
    formattedTowns = []
    # Format Hometown
    for home in hometowns[1:]:
        index = home.find("/")

        hometown = home[0:index]
        formattedTowns.append(hometown)
    
    return {"hometown": formattedTowns}