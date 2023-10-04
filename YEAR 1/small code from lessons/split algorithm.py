def split(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        print(split(lefthalf))
        print(split(righthalf))



if __name__ == "__main__":
    split([1,2,3,4,5,6,7,8,9])


