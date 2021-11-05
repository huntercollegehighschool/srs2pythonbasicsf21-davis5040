"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(5) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""

def diamond(size):
  s1 = size-1
  s2 = -1
  for i in range(size):
    print(" " * s1, end = "")
    print("*", end = "")
    if s2 > 0:
      print(" " * s2, end = "")
      print("*", end = "")
    print("\n")
    s1 -= 1
    s2 += 2
  s1 += 1
  s2 -= 2
  for i in range(size-1):
    s1 += 1
    s2 -= 2
    print(" " * s1, end = "")
    print("*", end = "")
    if s2 > 0:
      print(" " * s2, end = "")
      print("*", end = "")
    print("\n")