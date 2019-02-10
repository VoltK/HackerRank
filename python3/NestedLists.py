if __name__ == '__main__':
    gradelist = []

    for _ in range(int(input())):
        gradelist.append([input(),float(input())])

    second_lowest = sorted(set([grade for name, grade in gradelist]))[1]

    for name, grade in sorted(gradelist):
        if grade == second_lowest:
            print(name)
           

        

