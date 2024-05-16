# Python Task Quiz 1
# Print my name
name = "Brent"
print(name)
# Count up to my favorite number squared then commit
bestNumber = 12
for i in range(1,bestNumber*bestNumber+1):
    print(i)
# Create a class called engineers
class Engineers:
    # Class attribute
    skill = "problem solver"
    def __init__(self, name: str , type: str, experience: int) -> None:
        # Instance attributes
        self.name = name
        self.type = type
        self.experience = experience
# Create two different egnineers (objects)
engineer1 = Engineers(name = "Brad", type="Electrical", experience=10)
engineer2 = Engineers(name = "Karen", type = "Civil", experience = 15)
# Print attributes
print(engineer1.skill)
print(engineer1.name)
print(engineer1.type)
print(engineer1.experience)

print(engineer2.skill)
print(engineer2.name)
print(engineer2.type)
print(engineer2.experience)
# Reverse name
reverseName = name[::-1]
print(reverseName)
# Commit and post link
