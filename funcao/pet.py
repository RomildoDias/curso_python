def separador():
  print("-"*30)

def describe_pet(animal_type, animal_name):
    """Describe a pet"""
    separador()
    print("I have a " + animal_type + "\ncalled " + animal_name + ".")
    separador()

describe_pet("dog", "Spot")
describe_pet("cat", "yuna")