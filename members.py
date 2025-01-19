class DBZFactionSystem:
    def __init__(self):
        # Initialize the system with predefined data
        self.factions = {
            "Faction A": {
                "leader": "Alice Smith",
                "members": {
                    "Alice Smith": 120,
                    "Bob Johnson": 85,
                    "Charlie Brown": 95
                }
            },
            "Faction B": {
                "leader": "David Williams",
                "members": {
                    "David Williams": 150,
                    "Emily Davis": 110,
                    "Frank Moore": 70
                }
            },
            "Faction C": {
                "leader": "Grace Wilson",
                "members": {
                    "Grace Wilson": 140,
                    "Hannah Taylor": 100,
                    "Ian Anderson": 90
                }
            }
        }

    def displayMemberInfo(self, fullName):
        # Iterate through factions to find the user's details
        for faction_name, faction_info in self.factions.items():
            if fullName in faction_info["members"]:
                faction_leader = faction_info["leader"]
                faction_members = faction_info["members"]
                user_points = faction_members[fullName]

                return {
                    "faction_name": faction_name,
                    "faction_leader": faction_leader,
                    "faction_members": faction_members,
                    "user_points": user_points
                }
        return "Member DOES NOT EXIST"

newSystem = DBZFactionSystem()

fullName = input("Enter your full name: ").strip()
details = newSystem.displayMemberInfo(fullName)

if details:
    print("\n--- User Details ---")
    print(f"Faction Name: {details['faction_name']}")
    print(f"Faction Leader: {details['faction_leader']}")
    print("Faction Members:")
    for member, points in details['faction_members'].items():
        print(f"  - {member}: {points} points")
    print(f"Your Points: {details['user_points']}")
else:
    print("\nUser not found in any faction.")
