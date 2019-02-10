import json, os, argparse, sys

def check_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-f', '--file', type=str, action='store', help='enter JSON file: -p \'username_data.json\'')
    args_list = parse.parse_args()
    return args_list

def make_path(name, lang):
    if 'python' in lang:
        name += ".py"
    elif 'oracle' in lang or 'sql' in lang:
        name += ".sql"
    elif 'java' in lang:
        name += ".java"
    else:
        name += ".txt"
    return os.path.join(lang, name)

def make_folder(lang):
    if not os.path.exists(lang):
        os.makedirs(lang)

def writer(path, code):
    with open(path, 'w') as code_file:
            code_file.write(code)

def main():
    arg = check_args()

    if arg.file is None:
        sys.exit("Blank arguments. Enter JSON file: -p \'username_data.json\'")

    if os.path.isfile(arg.file):
        with open(arg.file, 'r') as json_file:
            data = json.load(json_file)
            total = 0
            for solution in data['submissions']:
                language = solution['language']
                make_folder(language)

                filename = "".join(letter for letter in solution['challenge'] if letter.isalnum())
                path = make_path(filename, language)

                code = solution['code']
                score = solution['score']
                # check if file doesn't exist, code is not blank and problem solved
                if not os.path.isfile(path) and code and score > 0:
                    writer(path, code)
                    print(f"{filename} was saved")
                    total += 1
            print(f"\n{total} problems were saved")
    else:
        print("File does not exist")


if __name__ == '__main__':
    main()



