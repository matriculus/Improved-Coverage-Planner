# Improved-Coverage-Planner

## Introduction

Coverage Path Planning is an interesting problem for robotics where a robot has to visit all the required points in space only once and the total distance travelled should be minimum. This problem is very similar to Travelling Salesman Problem.

There are lots of applications for this planning problem. For example:

1. Surveillance
2. Roomba like vacuum cleaners
3. Industrial vacuum cleaning to cover all locations inside warehouses
4. Lawn mowers which needs to cover the whole surface of the ground (golf courses, etc.)

## Environment

The environment for this path planner is a grid space (of any rectangle) but the algorithm works for any grid space (cocave or convex). The grid should have upto 5 values. The values correspond to the status.

- 0, if free
- 1, if occupied
- 2, starting point
- 3, end point
- 4, visited

## Solution

The solution is arrived by converting the grid space into a connected graph. From the graph, minimum spanning tree (MST) is obtained. From MST, using Christofides algorithm, the coverage planning is obtained.
