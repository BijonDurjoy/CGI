# CGI_Tasks

# Modifications for Slopes m > 1

When the slope m is greater than 1, it means the line is steeper, and for each step in the x-direction, the corresponding step in the y-direction is greater than 1. To adapt the Bresenham's algorithm for such cases, the roles of x and y are swapped. That is, instead of considering each x-coordinate, we consider each y-coordinate and calculate the corresponding x-coordinate. This ensures that we cover each pixel in the line without skipping any pixels.

* The output of Task 1 is : Case 1 Points: Case 1 Points: [(1, 1), (2, 1), (3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4)]

Case 1 Line Drawing:

![Image1](/media/bijon/myHDD/Code/Git/CGI/CGI_Tasks/Img/Screenshot from 2024-02-09 15-02-25.png)