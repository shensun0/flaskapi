from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def chart():
    r = requests.get('http://auth.chargeup.asia:1337/user')
    data = r.json()
        
    no_of_users = len(data)


    virtualusers = dict()
    for user in data:
        if "virtual" in user:
            virtualusers["virtual"] = virtualusers.get("virtual", 0) + 1
    virtualusers["nonvirtual"] = no_of_users -virtualusers.get("virtual")
        
        
    updatedstamps = dict()    
    for user in data:
        if "updatedAt" in user:
            userdate = user['updatedAt'].split('T', 1)[0]
            updatedstamps[userdate] = updatedstamps.get(userdate, 0) + 1                           
           
    email = dict()       
    for user in data:
        if "email" in user:
           email_data = user['email'].split('@', 1)
           if len(email_data)>1:
               email[email_data[1]] = email.get(email_data[1], 0) + 1
            #some of the email data only contained the usernname
            

    
    return jsonify(virtualusers, updatedstamps, email)
    
if __name__ == "__main__":
    app.run(debug = True)

