# simple-binary-search-tree-in-python

A Refresher tutorial for keeping skills up to date.

## Binary Search Tree (BST)

This implementation assumes values within node to be integers. In considering methods to implement we need to predicate the details based on type of trees we wish to work with- aiming for 'complete' trees to become 'full'-ly height balanced and sorted with self-balancing search trees being way more labor and logic intensive to implement. KISS this one hello if not looking for all the best practices:) [Here's conda's link](https://anaconda.org/conda-forge/binarytree) for binarytree module.

## Big Oh face

Just food for thought- if we continually just add integers that are numerically increasing to the end we effectively have a linked list, and thats OOOOOOOOH(n); where we are attempting to get better logarithmic results using BST. So average is logn performance for most operations like access, add, delete, and search, worst case O(n) for the linked list like operation.

## Other considerations

So some of the conditions we will be checking will be while not full or not complete is this value less or greater than current node in question? If so we choose to go to the left or right down the tree, where left is less and right is greater than.

## Steps to implement

For myself, implementing print was a tricky way to refresh on recursion. Modern coding obfuscates the tedious stuff. Getting to a base case and then popping was is fun to draw out, even when learning this over a decade ago. The first shot at print did not include a height variable passed around to allow a visual of what the tree really looked like, because it was printing values in order, instead of by height. 

This can lead us down a path of really not being able to visualize where insertions are taking place, especially when using the fill_tree() which randomly adds values. There exists a cli tree printer that makes things look oh so pretty... 

So we can go back and add a height variable into the print method and draw out the tree after filling it. The next step would be instead of just adding in the variable, figure out how to implement a decorator to the print function adding in a variable for height that way. Steps would be to comment out the added height variable lines, add in the @decorator functionality, and test. 

After implementing the _height method and calling it (`bst.height()`), we can compare the height variable in the print with the recursive call to verify they all match- the hand drawing, the print height variable, and the _height() comparison. 

### Printing

We are using integer values to print therefore we are getting an ordered traversal if we implement insertion properly. Current node prints value in-between left and right recursive calls.

#### Recursion

This implementation has both public and private methods partitioned to allow for recursion using the '_xxx' version to denote the private version. Linters such as pylint will not emit "unused variable" warnings for this symbol as of May 2021.

The idea of calling the same method again using self is a bit tricky to conceptualize. Add on the fact that people tend to skip that as the 'first' parameter, and the interpreter even yells at you zero based with one positional argument but two given:);):) I came from 'this' keyword in JavaScript, when 'class' did not even exist in Python. Moving on... 

Recursion happens with private '_' print, _insert, _height, and _search methods. This will separate what the human interacts with and what happens in the background. For print, as we pop elements off, and due to the fact we are using integer values in the tree, the elements come out in sorted order. Often in recursion we traverse to the end and work our way back. BST traversal here drills down to the leaves.

This is not always the case with preorder or postorder traversals. That's a whole other story.

### Search

Returns True if it is found in the tree, or false if not. We also could add in the height to verify that we have drawn the tree out properly on paper. We could also easily modify search to return the actual node or the value. However this might be better left as a bool for humans to use in checking the tree is well-formed.

We will make another method .find() for deleting that actually returns the node and not a bool afterwords.

### Deletion

There are three cases to address. The first is where there is only one child to delete, then two, and lastly also the root. Each case needs specific things to happen in order to maintain the tree. 

### New switch match case to Python 3.10

If you're like me we take it to the next level. There now exists a match case which can best branching logic with lots of if's (like the three below). Try and re-write this logic after the implementation is realized using if's.

### Delete breakdown

In each case we need to find and return the actual node as to be able to do something with the node in question. If there is no node found, the deletion results in nothing done (returns None).

To delete a node with no children, we find which node placeholder has the reference, and set the parent node's appropriate child to None. This is known as the "leaf" deletion method. 

To delete a node with a single child we find the parent of the node to be deleted, and swap out the appropriate child reference from the node to be deleted parent's child- either one that the left or right contains- to whichever one parent's right or left. It sounds tricky but in logic we just assume that if it isn't the first one we check, it has to be the other- or its the leaf case and was already addressed. 

For deletion of a node with both children there are quite a few sub steps needing to be implemented. We have to traverse the tree inorder to find the inorder successor. E.g. If the elements of the tree were in an array in sorted order, it would be the element directly after the one to be deleted. The trick here is that the min value function traverses down the left side of the tree, but we call it on the next sequential number. Mind bender element reader ;) We then might have two copies of the successor node, calling the deletion method again recursively to delete the original successor node. 

#### Note on AI backed IDE's

Watch out for smart automatic vscode imports these days. Maybe kite extension and automatic documentation is not the way to go. I'm not sure what that looks like in pycharm these days. Either way might try to import the requests delete function instead of ours. How is this the thing of the future? Nanu, nanu. They're getting there, though... Fly be free. Don't waste human time implementing it in production unless it's right- or it's contributing to counter-productivity:)

### Changes to binary_search_with_delete.py

The biggest notable to start handling a delete is that we need a variable for storing the parent information in class node to assign new references. This is much like a linked list's version of setting new references to next/previous. 

We also write two delete functions- one to call the other with after finding the node to be deleted.
