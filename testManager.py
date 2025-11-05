from PositionManager import PositionManager

pm = PositionManager(3)

pm.add_position(100, "Engineer")
pm.add_position(200, "Accountant")
pm.add_position(999, "Quality Assurance")
print("*" * 20)
pm.get_position(200)
pm.get_position(555)
pm.display_positions()
print("*"*20)

pm.add_position(555, "IT Specialist")
pm.remove_position(200)
pm.display_positions()
print("*"*20)
pm.add_position(200, "Analyst")
pm.display_positions()
