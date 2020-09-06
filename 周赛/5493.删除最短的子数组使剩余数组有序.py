import bisect
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # n = len(arr)
        # k = n-1
        # while k>0 and arr[k-1]<=arr[k]: k-=1
        # r = k
        # if r==0: return 0
        # j = 0
        # while j< n-1:
        #     ci = bisect.bisect_left(arr[k:], arr[j])
        #     t = n-((n-k-ci)+j+1)
        #     if r>t: r=t
        #     if arr[j]>arr[j+1]: break
        #     j+=1
        # return r


        n = len(arr)
        k = n - 1
        while k > 0 and arr[k] >= arr[k-1]:
            k-=1
        r = k
        if r == 0:
            return 0
        
        j = 0
        while j < (n - 1):
            ci = bisect.bisect_left(arr[k:], arr[j])
            t = n - ((n - k - ci) + j + 1)
            if r > t:
                r = t
            if arr[j] > arr[j+1]:
                break

        return r

if __name__ == "__main__":
    obj = Solution()
    print(obj.findLengthOfShortestSubarray([1,5,5,5,10,3,5,5,5,20]))