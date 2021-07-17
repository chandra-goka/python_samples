import os

print('USER > ', os.environ['USERss'])
print('HOME > ', os.environ['HOME'])
print('PATH > ', os.environ['PATH'])
print('PYTHONPATH > ', os.environ['PYTHONPATH'])

if 'IP' in os.environ:
    print(f"IP found in environ {os.environ['IP']}")
else:
    print("IP not found in environ so creating it")
    os.environ['IP'] = "0.0.0.0"
    print('IP > ', os.environ['IP'])

print('IP > ', os.environ['IP'])

try:
    print('IP > ', os.environ['IP'])
except KeyError as err:
    print(f"Given key not found - {err}")


for item, value in os.environ.items():
    print(f"{item} > {value}")
