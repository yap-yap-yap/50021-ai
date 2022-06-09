# Homework - Week 3

Basic backtracking search: 
```
number of assignments 9
('V1', 1)
('V2', 2)
('V3', 3)
('V4', 2)
('V5', 3)
('V6', 1)
('V7', 3)
('V8', 1)
('V9', 2)
```

With variable ordering (minimum remaining values)
```
number of assignments 9
('V1', 2)
('V2', 1)
('V3', 3)
('V4', 1)
('V5', 3)
('V6', 2)
('V7', 3)
('V8', 2)
('V9', 1)
```

With value ordering (least constraining values):
```
number of assignments 9
('V1', 1)
('V2', 2)
('V3', 3)
('V4', 2)
('V5', 3)
('V6', 1)
('V7', 3)
('V8', 1)
('V9', 2)
```

With forward checking:
```
number of assignments 9
('V1', 1)
('V2', 2)
('V3', 3)
('V4', 2)
('V5', 3)
('V6', 1)
('V7', 3)
('V8', 1)
('V9', 2)
```

With AC-3 inference algorithm:
```
number of assignments 9
('V1', 1)
('V2', 2)
('V3', 3)
('V4', 2)
('V5', 3)
('V6', 1)
('V7', 3)
('V8', 1)
('V9', 2)
```

With MRV heuristic, LCV heuristic, AC-3 algorithm: 
```
number of assignments 9
('V1', 3)
('V2', 1)
('V3', 2)
('V4', 1)
('V5', 2)
('V6', 3)
('V7', 2)
('V8', 3)
('V9', 1)
```

Since the basic backtracking algorithm is able to find a solution with 9 assignments (the minimum, as there are 9 variables), there is no need for any further optimisation using variable ordering, value ordering or inference. The reason why the minimum number of assignments was reached through only basic backtracking is most likely because the problem is simple. However, the results of the testing are still documented here. 