"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        # Case 1: Left Right - DONT Collide 
        # Case 2: Left Left
        # Case 3: Right Right
        # Case 4: Right Left - Collide

        for a in asteroids:
            while s and a < 0 < s[-1]: # While !Stack.isEmpty() and Current Asteroid is negative and top of stack is positive. At this point we know a collision is guarenteed.
                if abs(a) > s[-1]: # If the negative (left) asteroid is greater, pop the top of stack and continue.
                    s.pop()
                    continue
                elif abs(a) == s[-1]:
                    #Same logic except now both asteroids destroy eachother so dont continue.
                    s.pop()
                break
            else:
                #If the stack is empty or there is no collision simply append Current Asteroid.
                s.append(a)

        return s
           
                
        