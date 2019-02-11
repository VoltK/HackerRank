if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uniq = set(arr)
    uniq.remove(max(uniq))
    print(max(uniq))
    
    


