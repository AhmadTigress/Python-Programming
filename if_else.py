"""
Metro Token Purchase Based on Height Requirement:
This code determines if someone taller than 3 feet needs to buy a token before boarding the metro, 
otherwise no token is required
"""
height = float(input("Enter your height in fts: "))

if height > 3:
    print("Buy token")
    print("Now you can board the metro")
    
else:
    print("Yoyr height is less than 3.")
    print("No token required")