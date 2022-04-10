def h_index(n, citations):
  ans = []
  h_index = 0
  my_list = []          # list[3 3 15]     size = 3 h_index = 3
  size = 0
  # 1 3 3 2 2 15  -> 1 1 2 2 2 3
  # TODO: Complete the function to get the H-Index scores after each paper
  for num in citations:
      if num > h_index:             #only add if num > previous h_index
          my_list.append(num)
          size = len(my_list)
          for i in my_list:
              if i < size:
                my_list.pop(my_list.index(i))
          size = len(my_list)
          h_index = size
          ans.append(h_index)
      else:
          ans.append(h_index)

          
      for i in my_list: # for removing any number less than the h_index
          if i < h_index:
              my_list.pop(my_list.index(i))

      if num <= h_index:
          if num in my_list:
              my_list.pop(my_list.index(num))
          size = len(my_list)
      print(my_list)

  return ans

if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):
    n = int(input())                      # The number of papers
    citations = map(int, input().split()) # The number of citations for each paper
    h_index_scores = h_index(n, citations)
    print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
