
import sys

name = sys.argv[1]
list_of_pram = [sys.argv[i] for i in range(2, len(sys.argv))]
params = "self, "
this = ""
f = open(f"{sys.argv[1]}.py", 'a')
for itm in list_of_pram:
    this += f'self._{itm} = {itm}\n\t\t'
    params += f'{itm}, '
string = f"class {name}:\n\tdef __init__({params}):\n\t\t{this}"
f.write(string)
f.close()



