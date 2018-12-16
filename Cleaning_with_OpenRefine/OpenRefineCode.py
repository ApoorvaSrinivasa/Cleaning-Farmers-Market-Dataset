
### This data cleaning was carried out in OpenRefine using Python language

## Removing "NA", "n/a", "None", "No" from Facebook, Twitter, Youtube
# For Facebook
if value.lower() == "n/a" or value.lower()=="none" or value.lower()=="no":
    return ""
else:
    return value

# For Twitter
if value.lower() == "n/a" or value.lower() == "na" or value.lower()=="none" or value.lower()=="no" or value.lower == "no twitter":
    return ""
else:
    return value

# For Youtube
if value.lower() == "n/a" or value.lower() == "na" or value.lower()=="none" or value.lower()=="no":
    return ""
else:
    return value


## Treating Facebook column as discussed in the project report
import re
if re.search( "facebook\.com”, value):
    return value
elif len(value) < 1:
    return value
else:
    return "https://facebook.com/" + value

## Treating Twitter column
import re
if re.search("twitter\.com", value):
    return value
elif len(value) < 1:
    return value
elif value[0] == "@":
    return "https://twitter.com/" + value[1:]
else:
    return "https://twitter.com/" + value


## Treating Youtube Columns
import re
if re.search("youtube\.com", value):
    return value
elif len(value) < 1:
    return value
elif value[0] == "@":
    return "https://youtube.com/" + value[1:]
else:
    return "https://youtube.com/" + value


## Extracting month column from the spilt columns of Season1StartDate
if value == None  :
    return ""
elif len(value.lower().split("/")) > 1 :
    return value.lower().split("/")[0]
else :
    if value.lower()[:3] == 'jan':
        return "01"
    elif  value.lower()[:3] == 'feb':
        return "02"
    elif  value.lower()[:3] == 'mar':
        return "03"
    elif  value.lower()[:3] == 'apr':
        return "04"
    elif  value.lower()[:3] == 'may':
        return "05"
    elif  value.lower()[:3] == 'jun':
        return "06"
    elif  value.lower()[:3] == 'jul':
        return "07"
    elif  value.lower()[:3] == 'aug':
        return "08"
    elif  value.lower()[:3] == 'sep':
        return "09"
    elif  value.lower()[:3] == 'oct':
        return "10"
    elif  value.lower()[:3] == 'nov':
        return "11"
    elif  value.lower()[:3] == 'dec':
        return "12"
