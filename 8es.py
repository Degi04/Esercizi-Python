#De Gironimo Matteo 5A


def merge_lists(l1,l2):
  dim1 = len(l1)
  dim2 = len(l2)
  
  i, j = 0,0
  ris = []
 
  while i < dim1 and j < dim2:
      if l1[i] < l2[j]:
          ris.append(l1[i])
          i += 1
      else: 
          ris.append(l2[j])
          j += 1
  ris = ris + l1[i:] + l2[j:]
  return ris

assert merge_lists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert merge_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_lists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert merge_lists([1, 2, 3], []) == [1, 2, 3]
assert merge_lists([], [1, 2, 3]) == [1, 2, 3]
