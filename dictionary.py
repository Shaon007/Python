monthConversions = {
    "Jan" : "January",
    'Feb' : 'February',
    'Mar' : 'March',
    'Apr' : 'April',
    'May' : 'May',
    'Jun' : 'June',
    'Jul' : 'July',
    'Aug' : 'August',
    'Sep' : 'September',
    'Oct' : 'October',
    'Nov' : 'November',
    '12' : 'December',
 }
 
print(monthConversions["Jul"])
print(monthConversions["12"])
print(monthConversions.get("sdf"))
print(monthConversions.get("sdf",'Not a valid key'))