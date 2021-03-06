from flask import Flask, request, jsonify
import json
import pandas as pd
app = Flask(__name__)



class SizeFinder:
    def __init__(self, json_str_or_file):
        json_reader = json.loads if isinstance(json_str_or_file, str) else json.load
        json_data = json_reader(json_str_or_file)
        self.data_df = pd.json_normalize(json_data['sellableUnits'], 'attributes')

    def find_size(self, size):
        size_ids = self.data_df.loc[
            (self.data_df.type == 'size') & (self.data_df.value == str(size).strip())
            ].id.to_list()

        return size_ids


@app.route('/getsize/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    storlek = request.args.get("name", None)
    size = request.data

    response = {}
    sizen = SizeFinder(size)
    sizen.find_size(storlek)

    # Check if user sent a name at all
    if not size:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(size).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {size} to our awesome platform!!"

    # Return the response in json format
    return size_id

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('size')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    SizeF)inder(

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)