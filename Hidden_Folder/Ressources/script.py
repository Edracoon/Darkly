import requests

def get_href_value(line):
    href_start_index = line.find('<a href="') + len('<a href="')
    href_end_index = line.find('">', href_start_index)
    href = line[href_start_index:href_end_index]
    return href

def read_readme(url, output_file):
    res = requests.get(url)
    if res.status_code == 200:
        # Check if the URL ends with "/README"
        # print("Found in README:", res.text)
        output_file.write(res.text)

def iterate_hidden_folder(url, output_file):
    res = requests.get(url)

    if res.status_code != 200:
        return
    lines = res.text.split('\n')
    for line in lines:
        if line.startswith('<a href="'):
            href = get_href_value(line)
            next_url = url + href
            print(next_url)
            if next_url.strip().endswith("README"):
                read_readme(next_url, output_file)
            else:
                iterate_hidden_folder(next_url, output_file)


# Output file to write results
output_file_path = "results.txt"

# Open the output file in write mode
with open(output_file_path, "w") as output_file:
    url = "http://192.168.1.40/.hidden/"
    iterate_hidden_folder(url, output_file)