import json

def get_from_viatuix_config(filename, key):
    try:
        # Open and read the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Extract username and password
            item = data.get(key)
            return item
    except FileNotFoundError:
        return "File not found.", None
    except json.JSONDecodeError:
        return "Invalid JSON format.", None
    except KeyError:
        return "Missing username or password in the JSON file.", None

## Example usage
#filename = 'viatuix.json'
#username, password = get_gh_credentials(filename)
#if username and password:
#    print("Username:", username)
#    print("Password:", password)
#else:
#    print("Error:", username)
