bst = []


def insert(key):
    if len(bst) == 0:  # check if tree (array) is empty
        bst.append(key)  # insert key in tree (array)
        for i in range(2):
            bst.append(None)  # appending 2 child nodes of the key
    else:
        if key == bst[0]:  # check if the key already exists at root
            print('key already exists')
        else:
            i = 0
            while i in range(len(bst)):  # loop through 0 to last element of tree i.e last index of array
                if bst[i] is None:  # check if the index contains None then it means we have reached the insertion node
                    bst[i] = key  # insert key at that index
                    # check if the index of right child for this particular key is greater than the size of array
                    if 2 * i + 3 > len(bst):
                        for j in range(len(bst), 2 * i + 3):  # then loop through last index to that particular index
                            bst.append(None)  # append empty nodes upto that index
                    else:  # and if the index is less than length of array
                        for j in range(2):  # then just simply append 2 nodes containing None
                            bst.append(None)
                    break  # break the loop to avoid additional and useless iterations
                else:  # if the index does not contain None then it means we have to continue the binary search
                    if key < bst[i]:  # if key is less than the current key
                        i = 2 * i + 1  # store the index of it's left child to go on left in the next iteration
                    elif key > bst[i]:  # if key is greater than the current key
                        i = 2 * i + 2  # store the index of it's right child to go on right in the next iteration
                    else:  # if the key is equal to the current key
                        print('key already exists')


def search(key):
    if len(bst) == 0:  # if tree is empty then abandon the search and return None
        return None
    else:
        if key == bst[0]:  # if key is on the root then return 0 as the index of key
            return 0
        else:  # if the key is not on root then
            i = 0
            while i < len(bst):  # loop through 0 to last element of array i.e last node of tree
                if bst[i] is None:  # if we've reached an empty node then it means the key does not exist
                    return None  # abandon the search by returning None
                if key < bst[i]:  # if key is less than the current key
                    i = 2 * i + 1  # store the index of it's left child to go on left in the next iteration
                elif key > bst[i]:  # if key is greater than the current key
                    i = 2 * i + 2  # store the index of it's right child to go on right in the next iteration
                elif key == bst[i]:  # if the key is equal to the current key
                    return i  # abandon the search by returning the index of key


def delete(key):
    if len(bst) > 1:  # if the tree is not empty
        ind = search(key)  # get the index of given key by calling the search function that we've written up here
        if ind is not None:  # if ind does not contains None then it means we've found the index of this key
            i = 2 * ind + 1  # store the index of it's left child
            while bst[i] is not None:  # loop through that node upto its most right node until we reach to None
                i = 2 * i + 2  # getting the index of right child
            # We have reached to the most right node None. Now we have to get it's parent index that contains a key
            i = i // 2 - 1
            bst[ind] = bst[i]  # set the key of this node on the index of given key
            bst[i] = bst[i * 2 + 1]  # store the key of left child at it's parent (current node)
            bst[i * 2 + 1] = None  # set the left child to None
            return True  # return True as the deletion is always successful when we get the index of given key
        return False  # return False if ind contains None


insert(50)
insert(30)
insert(70)
insert(20)
insert(40)
insert(60)
insert(80)
insert(90)
print(search(90))
print(bst)
print(delete(30))
print(bst)
