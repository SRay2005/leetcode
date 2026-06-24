class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 1. Convert obstacles to a set of tuples for instant lookups
        obstacle_set = {tuple(obs) for obs in obstacles}
        
        direction={'north': [0,1], 'south': [0,-1], 'east': [1,0], 'west': [-1,0]}
        current='north'
        
        x, y = 0, 0
        max_displacement=0
        
        for i in commands:
            if i>=1 and i<=9:
                # Get the movement for our current direction
                dx = direction[current][0]
                dy = direction[current][1]
                
                for k in range(i):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    else:
                        x += dx
                        y += dy
                
                if ((x**2) + (y**2)) > max_displacement:
                    max_displacement=((x**2) + (y**2))
                    
            elif i==-2:
                if current=='north':
                    current='west'
                elif current=='south':
                    current='east'
                elif current=='east':
                    current='north'
                else:
                    current='south'
            else:
                if current=='north':
                    current='east'
                elif current=='south':
                    current='west'
                elif current=='east':
                    current='south'
                else:
                    current='north'
                
        return max_displacement