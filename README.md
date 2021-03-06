# ClassicComputerScienceProblems

######    _Developed By Kelton Bassingthwaite_

Solutions to 'Classic Computer Problems in Python' by David Kopec


## Table of Contents



1. ___Small Problems___
    1. _Fibonacci Sequence_
        > Calculating the Fibonacci Sequence using various techniques such as 
        recursion, memoization, iteration, and generators.
        
    1. _Trivial Compression_
        > Compressing genes by storing the eight-bit String Nucleotides ('A', 'C','G' or, 'T')
        as a two-bit bit-string (0b00 to 0b11). 
    
    1. _Unbreakable Encryption_
        > Encrypts by XORing a data bit-string with random bit-string of the same length. 
    
    1. _Calculating Pi_
        > A Conversion of the Leibniz formula into Python.
        
    1. _Towers of Hanoi_
        > Uses Stacks and recursion so solve the Towers of Hanoi
        problem for 3 towers and 3 rings
        
    1. _Exercises_
        1. A conversion of the Fast-Doubling Fibonacci Algorithm to Python.
            > It takes about 0.25us to get the 10,000th Fibonacci Number.
        1. A wrapper to compress a stream of characters into a bit-string.
            > Uses @property for ease of use and is iterable.
     
1. ___Search Problems___
    1. _DNA Search_
        > Searches for a Codon within a Gene using Linear and Binary Search. 
    
    1. _Maze Solving_
        > Generate, then solve a random maze using Depth-First, Breadth-First and, A* Search
    
    1. _Missionaries and Cannibals_
        > Encode, then solve the Missionaries and Cannibals puzzle using 
        Depth-First, Breadth-First and, A* Search
    
    1. _Exercises_
        1. Compares Binary Search and Linear Search performance.
            >  Uses a 1,000,000 element list. Both sorted and unsorted.
        1. Compares Depth-First, Breadth-First and, A* Search on for Maze Solving
            > Counts the average number of nodes each search visited for 200 mazes.
       
1. ___Constraint Satisfaction Problems___
    1. _Building the CSP Framework_
        > A Generalized Constraint Satisfaction Problem Framework with a backtracking search.
        As well as ABC for constraints.
    
    1. _Map Coloring_
         > Colors the seven Australian provinces such that
         no two adjacent provinces have the same color.
         
    1. _Eight Queens_
        > Positions eight Queens such that no Queen can attack another.
    
    1. _Word Search_
        > Positions several words in a grid such that there is no overlap.
    
    1. _SEND+MORE=MONEY_
        > Finds what digits to replace the letters such that the equation
        holds.
      
    1. _Exercises_
        1. _Circuit Board Layout_
            > Fit different sized NxM rectangles into an AxB rectangle.
        1. _Suduku Solver_
            > Solves Suduku Puzzles, albeit very slowly. The more clues provided the faster it is.
            (17 Clues --> 32 hours, 36 Clues --> 5s)
            
1. ___Graph Problems___
    1. _The Basis_
        > Classes for Weighted and Unweighted Graphs and edges for use in later problems.
        
    1. _HyperLoop_
        > Demonstrating Weighted and Unweighted Graphs using a HyperLoop network.
        Using BFS to find the shortest path between two Vertices
        
    1. _Minimum Spanning Tree_
        > Implementing Jarník's Algorithm (AKA the Prim–Dijkstra algorithm).
        
    1. _Dijkstra's Algorithum_
        > Implementing Dijkstra's Algorithm.
        
        
        
1. ___Genetic Algorithms___
    1. _The Basis_
        > Base class for the Chromosomes and the Genetic Algorithm implementation.
        
    1. _Simple Equation_
        > Models `f(x, y) = 6x - x² + 4y - y²` as a chromosome, then finds the maximum `f(3, 2) = 13`.
                
    1. _SEND+MORE=MONEY v2_
        > Finds what digits to replace the letters such that the equation holds. The Genetic Algorithm approach finds more solutions than the constraint satisfaction approach.
        
    1. _Optimizing List Compression_
        > This application uses a genetic algorithm to find the most efficient order to compress a list. 
