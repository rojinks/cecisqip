if __name__ == '__main__':
    n = int(input())
    a = input()
    arr = list(map(int,a.split(" ")))
    arr.sort()
    for i in range(n-2,-1,-1):
       if(arr[i] != arr[i+1]):
           print(arr[i])
           break
    
