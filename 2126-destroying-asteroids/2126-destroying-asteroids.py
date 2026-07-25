class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        netmass=mass
        prevlessval=float('inf')
        lessval=0
        mini=0
        # for i in range (len(asteroids)):
        #     if asteroids[i]<mass:
        #         lessval=mass-asteroids[i]
        #         if lessval<prevlessval:
        #             mini=i
        #         prevlessval=lessval
        asteroids.sort()
        for i in range (len(asteroids)):
            if netmass<asteroids[i]:
                return False
            netmass+=asteroids[i]
        return True