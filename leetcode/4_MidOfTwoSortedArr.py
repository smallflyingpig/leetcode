class Solution1:
    def getKth1(self, nums, k):
        if isinstance(k, int):
            return nums[k]
        else:
            return (nums[int(k)]+nums[int(k+1)])//2

    def getKth(self, nums1, nums2, k):
        print(nums1, nums2, k)    
        if len(nums1)==0:
            return self.getKth1(nums2, k-1)
        if len(nums2)==0:
            return self.getKth1(nums1, k-1)
        if k==1:
            return min(nums1[0], nums2[0])
        elif k==0:
            return min(nums1[0], nums2[0])
        elif k==len(nums1)+len(nums2):
            return max(nums1[-1], nums2[-1])

        idx1 = max(0, len(nums1)-1-(len(nums1)+len(nums2)-k)//2)
        idx2 = max(0, min(int(k)-idx1-1, len(nums2)-1))
        if nums1[idx1] == nums2[idx2]:
            return nums1[idx1]
        elif nums1[idx1]>nums2[idx2]:
            return self.getKth(nums1[:idx1], nums2, k)
        elif nums1[idx1]<nums2[idx2]:
            return self.getKth(nums1, nums2[:idx2], k)


    def findMedianSortedArrays(self, nums1, nums2):
        m_n = len(nums1)+len(nums2) 
        if m_n % 2 == 0:
            return (self.getKth(nums1, nums2, (m_n//2))+self.getKth(nums1, nums2, (m_n//2)+1))/2.0
        else:
            return self.getKth(nums1, nums2, (m_n+1)//2)


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m,n = len(nums1), len(nums2)
        if m>n:
            nums1, nums2 = nums2, nums1
            m, n = n, m 
        mid = (m+n)//2
        
        if m==0:
            return nums2[mid] if (m+n)%2 else (nums2[mid]+nums2[mid-1])/2.0
        if n==0:
            return nums1[mid] if (m+n)%2 else (nums1[mid]+nums1[mid-1])/2.0
        val_min = min(nums1[0], nums2[0])-1
        val_max = max(nums1[-1], nums2[-1])+1
        idx1 = min(mid//2, m-1)
        idx2 = mid-idx1
        max1 = max(nums1[idx1-1] if idx1>0 else val_min, nums2[idx2-1] if idx2>0 else val_min)
        min2 = min(nums1[idx1] if idx1<m else val_max, nums2[idx2] if idx2<n else val_max)
        def get_val(val_list, idx):
            if idx<0:
                return val_min
            if idx>=len(val_list):
                return val_max
            return val_list[idx]
        min_idx1 = 0
        min_idx2 = 0
        max_idx1 = m
        max_idx2 = n
        while max1>min2:
            print(max1, min2, idx1, idx2, min_idx1, min_idx2, max_idx1, max_idx2)
            if get_val(nums1, idx1-1)>get_val(nums2, idx2-1):
                min_idx2 = idx2
                max_idx1 = idx1
                idx1 = (idx1+min_idx1)//2
                idx2 = mid-idx1
            else:
                min_idx1 = idx1
                max_idx2 = idx2
                idx1 = (idx1+max_idx1+1)//2
                idx2 = mid-idx1
            max1 = max(get_val(nums1, idx1-1), get_val(nums2, idx2-1))
            min2 = min(get_val(nums1, idx1), get_val(nums2, idx2))
        return min2 if (m+n)%2 else (max1+min2)/2.0


                







if __name__=="__main__":
    l1 = [2,3,4,5,6]
    l2 = [1]
    s = Solution()
    v = s.findMedianSortedArrays(l1, l2)
    print(v)