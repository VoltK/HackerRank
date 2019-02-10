if __name__ == '__main__':
    s = raw_input()
    for command in ['.isalnum()', '.isalpha()', '.isdigit()', '.islower()', '.isupper()']:
        print any(eval('c'+command) for c in s)
        
            

