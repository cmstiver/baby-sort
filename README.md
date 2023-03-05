# This is a meme algorithm based on this short video:

https://youtube.com/shorts/X2ozuxtfDB4

## Example of it running:

```
Sorting list [8, 6, 1, 5, 4, 10, 2, 3, 7, 9] into a stack.
Attempting to fit cup with the size of 1 into top cup...
None.
1->
Attempting to fit cup with the size of 6 into top cup...
1->
Removing cups from top until this cup fits:
None.
6->
Attempting to fit cup with the size of 8 into top cup...
6->
Removing cups from top until this cup fits:
None.
8->
Attempting to fit cup with the size of 2 into top cup...
8->
2->8->
Attempting to fit cup with the size of 1 into top cup...
2->8->
1->2->8->
Attempting to fit cup with the size of 7 into top cup...
1->2->8->
Removing cups from top until this cup fits:
2->8->
8->
7->8->
Attempting to fit cup with the size of 3 into top cup...
7->8->
3->7->8->
Attempting to fit cup with the size of 6 into top cup...
3->7->8->
Removing cups from top until this cup fits:
7->8->
6->7->8->
Attempting to fit cup with the size of 5 into top cup...
6->7->8->
5->6->7->8->
Attempting to fit cup with the size of 2 into top cup...
5->6->7->8->
2->5->6->7->8->
Attempting to fit cup with the size of 9 into top cup...
2->5->6->7->8->
Removing cups from top until this cup fits:
5->6->7->8->
6->7->8->
7->8->
8->
None.
9->
Attempting to fit cup with the size of 5 into top cup...
9->
5->9->
Attempting to fit cup with the size of 4 into top cup...
5->9->
4->5->9->
Attempting to fit cup with the size of 2 into top cup...
4->5->9->
2->4->5->9->
Attempting to fit cup with the size of 6 into top cup...
2->4->5->9->
Removing cups from top until this cup fits:
4->5->9->
5->9->
9->
6->9->
Attempting to fit cup with the size of 7 into top cup...
6->9->
Removing cups from top until this cup fits:
9->
7->9->
Attempting to fit cup with the size of 3 into top cup...
7->9->
3->7->9->
Attempting to fit cup with the size of 1 into top cup...
3->7->9->
1->3->7->9->
Attempting to fit cup with the size of 2 into top cup...
1->3->7->9->
Removing cups from top until this cup fits:
3->7->9->
2->3->7->9->
Attempting to fit cup with the size of 5 into top cup...
2->3->7->9->
Removing cups from top until this cup fits:
3->7->9->
7->9->
5->7->9->
Attempting to fit cup with the size of 6 into top cup...
5->7->9->
Removing cups from top until this cup fits:
7->9->
6->7->9->
Attempting to fit cup with the size of 3 into top cup...
6->7->9->
3->6->7->9->
Attempting to fit cup with the size of 8 into top cup...
3->6->7->9->
Removing cups from top until this cup fits:
6->7->9->
7->9->
9->
8->9->
Attempting to fit cup with the size of 4 into top cup...
8->9->
4->8->9->
Attempting to fit cup with the size of 2 into top cup...
4->8->9->
2->4->8->9->
Attempting to fit cup with the size of 6 into top cup...
2->4->8->9->
Removing cups from top until this cup fits:
4->8->9->
8->9->
6->8->9->
Attempting to fit cup with the size of 5 into top cup...
6->8->9->
5->6->8->9->
Attempting to fit cup with the size of 7 into top cup...
5->6->8->9->
Removing cups from top until this cup fits:
6->8->9->
8->9->
7->8->9->
Attempting to fit cup with the size of 3 into top cup...
7->8->9->
3->7->8->9->
Attempting to fit cup with the size of 10 into top cup...
3->7->8->9->
Removing cups from top until this cup fits:
7->8->9->
8->9->
9->
None.
10->
Attempting to fit cup with the size of 3 into top cup...
10->
3->10->
Attempting to fit cup with the size of 5 into top cup...
3->10->
Removing cups from top until this cup fits:
10->
5->10->
Attempting to fit cup with the size of 9 into top cup...
5->10->
Removing cups from top until this cup fits:
10->
9->10->
Attempting to fit cup with the size of 3 into top cup...
9->10->
3->9->10->
Attempting to fit cup with the size of 7 into top cup...
3->9->10->
Removing cups from top until this cup fits:
9->10->
7->9->10->
Attempting to fit cup with the size of 6 into top cup...
7->9->10->
6->7->9->10->
Attempting to fit cup with the size of 1 into top cup...
6->7->9->10->
1->6->7->9->10->
Attempting to fit cup with the size of 8 into top cup...
1->6->7->9->10->
Removing cups from top until this cup fits:
6->7->9->10->
7->9->10->
9->10->
8->9->10->
Attempting to fit cup with the size of 3 into top cup...
8->9->10->
3->8->9->10->
Attempting to fit cup with the size of 5 into top cup...
3->8->9->10->
Removing cups from top until this cup fits:
8->9->10->
5->8->9->10->
Attempting to fit cup with the size of 6 into top cup...
5->8->9->10->
Removing cups from top until this cup fits:
8->9->10->
6->8->9->10->
Attempting to fit cup with the size of 4 into top cup...
6->8->9->10->
4->6->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
4->6->8->9->10->
2->4->6->8->9->10->
Attempting to fit cup with the size of 3 into top cup...
2->4->6->8->9->10->
Removing cups from top until this cup fits:
4->6->8->9->10->
3->4->6->8->9->10->
Attempting to fit cup with the size of 7 into top cup...
3->4->6->8->9->10->
Removing cups from top until this cup fits:
4->6->8->9->10->
6->8->9->10->
8->9->10->
7->8->9->10->
Attempting to fit cup with the size of 1 into top cup...
7->8->9->10->
1->7->8->9->10->
Attempting to fit cup with the size of 3 into top cup...
1->7->8->9->10->
Removing cups from top until this cup fits:
7->8->9->10->
3->7->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
3->7->8->9->10->
2->3->7->8->9->10->
Attempting to fit cup with the size of 5 into top cup...
2->3->7->8->9->10->
Removing cups from top until this cup fits:
3->7->8->9->10->
7->8->9->10->
5->7->8->9->10->
Attempting to fit cup with the size of 4 into top cup...
5->7->8->9->10->
4->5->7->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
4->5->7->8->9->10->
2->4->5->7->8->9->10->
Attempting to fit cup with the size of 1 into top cup...
2->4->5->7->8->9->10->
1->2->4->5->7->8->9->10->
Attempting to fit cup with the size of 6 into top cup...
1->2->4->5->7->8->9->10->
Removing cups from top until this cup fits:
2->4->5->7->8->9->10->
4->5->7->8->9->10->
5->7->8->9->10->
7->8->9->10->
6->7->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
6->7->8->9->10->
2->6->7->8->9->10->
Attempting to fit cup with the size of 4 into top cup...
2->6->7->8->9->10->
Removing cups from top until this cup fits:
6->7->8->9->10->
4->6->7->8->9->10->
Attempting to fit cup with the size of 5 into top cup...
4->6->7->8->9->10->
Removing cups from top until this cup fits:
6->7->8->9->10->
5->6->7->8->9->10->
Attempting to fit cup with the size of 3 into top cup...
5->6->7->8->9->10->
3->5->6->7->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
3->5->6->7->8->9->10->
2->3->5->6->7->8->9->10->
Attempting to fit cup with the size of 1 into top cup...
2->3->5->6->7->8->9->10->
1->2->3->5->6->7->8->9->10->
Attempting to fit cup with the size of 4 into top cup...
1->2->3->5->6->7->8->9->10->
Removing cups from top until this cup fits:
2->3->5->6->7->8->9->10->
3->5->6->7->8->9->10->
5->6->7->8->9->10->
4->5->6->7->8->9->10->
Attempting to fit cup with the size of 1 into top cup...
4->5->6->7->8->9->10->
1->4->5->6->7->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
1->4->5->6->7->8->9->10->
Removing cups from top until this cup fits:
4->5->6->7->8->9->10->
2->4->5->6->7->8->9->10->
Attempting to fit cup with the size of 3 into top cup...
2->4->5->6->7->8->9->10->
Removing cups from top until this cup fits:
4->5->6->7->8->9->10->
3->4->5->6->7->8->9->10->
Attempting to fit cup with the size of 1 into top cup...
3->4->5->6->7->8->9->10->
1->3->4->5->6->7->8->9->10->
Attempting to fit cup with the size of 2 into top cup...
1->3->4->5->6->7->8->9->10->
Removing cups from top until this cup fits:
3->4->5->6->7->8->9->10->
2->3->4->5->6->7->8->9->10->
Attempting to fit cup with the size of 1 into top cup...
2->3->4->5->6->7->8->9->10->
1->2->3->4->5->6->7->8->9->10->
```
