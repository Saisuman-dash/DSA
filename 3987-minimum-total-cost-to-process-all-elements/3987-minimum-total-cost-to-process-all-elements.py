class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        resourceavailable = k
        attempt = 0
        cost = 0

        for num in nums:
            if resourceavailable < num:
                needed = num - resourceavailable
                refills = (needed + k - 1) // k

                cost += refills * (2 * attempt + refills + 1) // 2
                cost %= MOD

                attempt += refills
                resourceavailable += refills * k

            resourceavailable -= num

        return cost
        # resourceavailable = k
        # attempt=0
        # cost=0
        # MOD= 10**9+7
        # for i in range (len(nums)):
        #     if resourceavailable>=nums[i]:
        #         resourceavailable-=nums[i]
        #     else:
        #         while resourceavailable<nums[i]:
        #             attempt+=1
        #             resourceavailable+=k
        #             cost=(cost+attempt) % MOD
        #         resourceavailable-=nums[i] 
        # return cost


        