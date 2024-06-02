class Solution:
    # Using the merge sort then linear search method:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Implementing Merge sort
        self.MergeSort(nums)
        return self.LinSearch(nums)


# Performs the merge sort algorithm given an array
    def MergeSort(self, arr):
                if len(arr) > 1:
                    r = len(arr) // 2
                    l = arr[:r]
                    m = arr[r:]
                    self.MergeSort(l)
                    self.MergeSort(m)
                    i = j = k = 0

                    while i < len(l) and j < len(m):
                        if l[i] < m[j]:
                            arr[k] = l[i]  
                            i += 1
                        else:
                            arr[k] = m[j]
                            j += 1
                        k += 1

                    while i < len(l):
                        arr[k] = l[i]  
                        i += 1
                        k += 1

                    while j < len(m):
                        arr[k] = m[j]
                        j += 1
                        k += 1
# Performs the Linear Search Algorithm given an array and returns true if any elements are true, otherwise returns false
    def LinSearch(self, arr):

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return True
        return False