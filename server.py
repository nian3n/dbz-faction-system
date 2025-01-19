from flask import Flask, request, jsonify, render_template
import json

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

def load_data():
    with open("factions.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("factions.json", "w") as f:
        json.dump(data, f, indent=4)
print(load_data())

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route("/tmp")
def temp():
    return jsonify({'he' :'lo'})

@app.route("/handle_get")
def dashboard():
    #data = request.json
    #full_name = data["full_name"]

    #existent_user = False
    factions = load_data()
    #for faction_name, faction_info, in factions["factions"].items():
    #    if full_name in faction_info["members"]:
    #        existent_user = True
    #    if not existent_user:
    #        return jsonify({"error": "User not found"}), 404
    return jsonify(factions)
        

@app.route("/update_name", methods=["POST"])
def update_fullname():
    data = request.json
    prev = data["prev"]
    new = data["new"]

    factions = load_data()
    for faction_info in factions["factions"].items():
        if prev in faction_info["members"]:
            faction_info["members"][new] = faction_info["members"].pop(prev)
            save_data(factions)
            return jsonify({"message": "Name updated successfully"}), 200

    return jsonify({"error": "User not found"}), 404

@app.route("/update_point", methods=["POST"])
def update_points():
    data = request.json
    faction_name = data["faction"]
    member_name = data["name"]
    new_points = data["point"]

    factions = load_data()

    for key in factions:
        if member_name in factions[key]['members']:
            factions[key]['members'][member_name] += new_points
            break

    #factions["factions"][faction_name]["members"][member_name] = new_points

    #factions["factions"][faction_name]["faction_points"] = sum(
    #    factions["factions"][faction_name]["members"].values()
    #)

    save_data(factions)
    return "None"

    

if __name__ == '__main__':
    app.run()
