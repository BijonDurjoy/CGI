# Bresenham's algorithm 

# Modifications for Slopes m > 1

When the slope m is greater than 1, it means the line is steeper, and for each step in the x-direction, the corresponding step in the y-direction is greater than 1. To adapt Bresenham's algorithm for such cases, the roles of x and y are swapped. That is, instead of considering each x-coordinate, we consider each y-coordinate and calculate the corresponding x-coordinate. This ensures that we cover each pixel in the line without skipping any pixels.

# Outputs

* The output of Task 1 is : Case 1 Points: Case 1 Points: [(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4)]

Case 1 Line Drawing:


![Screenshot from 2024-02-09 15-02-25](https://github.com/BijonDurjoy/CGI/assets/94054428/fd6c0220-7ee2-4692-b8bb-bb15039057a0)

* Case 2 Points: [(1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (4, 7), (4, 8)]

Case 2 Line Drawing: 

![Task 2](https://github.com/BijonDurjoy/CGI/assets/94054428/028a7583-d9ff-4000-8af8-1e9647b048ee)
