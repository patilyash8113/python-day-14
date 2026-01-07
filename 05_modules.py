#There are two types of modules in python
# -built in Module 
# -External module
import math
print(math.sqrt(16))
import os
import mymodule
mymodule.hello()

import requests
r=requests.get("https://www.google.com/")
print(r.text) #text is not a ,ethod its a property
