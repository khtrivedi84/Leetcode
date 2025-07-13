class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force
        if len(nums1) == 0 and len(nums2) == 0:
            return []

        combined_sorted_arr = []
        p1 = 0
        p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                combined_sorted_arr.append(nums1[p1])
                p1 += 1
            else:
                combined_sorted_arr.append(nums2[p2])
                p2 += 1
        
        while p1 < len(nums1):
            combined_sorted_arr.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            combined_sorted_arr.append(nums2[p2])
            p2 += 1
        
        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (combined_sorted_arr[n//2] + combined_sorted_arr[(n//2 - 1)]) / 2
        else:
            return combined_sorted_arr[n//2]

        # Better - Space Optimized
        n1 = len(nums1)
        n2 = len(nums2)

        n = n1 + n2

        index1 = n // 2
        index2 = (n // 2) - 1
        index1_ele = None
        index2_ele = None
        p1 = 0
        p2 = 0
        curr_index = 0
        while p1 < n1 and p2 < n2:
            if nums1[p1] <= nums2[p2]:
                if curr_index == index1:
                    index1_ele = nums1[p1]
                if curr_index == index2:
                    index2_ele = nums1[p1]
                p1 += 1
            else:
                if curr_index == index1:
                    index1_ele = nums2[p2]
                if curr_index == index2:
                    index2_ele = nums2[p2]
                p2 += 1

            curr_index += 1
        
        while p1 < n1:
            if curr_index == index1:
                    index1_ele = nums1[p1]
            if curr_index == index2:
                index2_ele = nums1[p1]
            p1 += 1
            curr_index += 1
        
        while p2 < n2:
            if curr_index == index1:
                    index1_ele = nums2[p2]
            if curr_index == index2:
                index2_ele = nums2[p2]
            p2 += 1
            curr_index += 1

        if n % 2 == 0:
            return (index1_ele + index2_ele) / 2
        else:
            return index1_ele

        # Optimal - Binary Search
        n1 = len(nums1)
        n2 = len(nums2)
        
        # Make sure binary search is performed on smaller array to handle edge cases and boundaries
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        n = n1 + n2 
        left_side_length = (n1 + n2 + 1) // 2
        low = 0
        high = n1
        while low <= high:
            nums1_mid = (low + high) // 2
            nums2_mid = left_side_length - nums1_mid

            left1 = float('-inf')
            left2 = float('-inf')
            right1 = float('inf')
            right2 = float('inf')

            # Update left1 and right1
            if nums1_mid < n1:
                right1 = nums1[nums1_mid]
            if nums1_mid - 1 >= 0:
                left1 = nums1[nums1_mid - 1]
            
            # Update left2 and right2
            if nums2_mid < n2:
                right2 = nums2[nums2_mid]
            if nums2_mid - 1 >= 0:
                left2 = nums2[nums2_mid - 1]
            
            # Binary search to find the answer or eliminate a half
            if left1 <= right2 and left2 <= right1:
                if n % 2 == 0:
                    ele1 = max(left1, left2)
                    ele2 = min(right1, right2)
                    ans = (ele1 + ele2) / 2
                    return ans
                else:
                    return max(left1, left2)

            if left1 > right2:
                high = nums1_mid - 1
            elif left2 > right1:
                low = nums1_mid + 1
        return 0.0