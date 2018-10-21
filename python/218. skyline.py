from heapq import _heapify_max, _heappop_max
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        start_end_array = []
        array_data_dict = {}
        for building in buildings:
            if building[0] not in array_data_dict:
                array_data_dict[building[0]] = {
                    's': [building[2]],
                    'e': []
                }
            else:
                array_data_dict[building[0]]['s'].append(building[2])
            if building[1] not in array_data_dict:
                array_data_dict[building[1]] = {
                    'e': [building[2]],
                    's': []
                }
            else:
                array_data_dict[building[1]]['e'].append(building[2])

        array_x_sorted = sorted(array_data_dict.keys())
        for x in array_x_sorted:
            same_x = array_data_dict[x]
            same_x_start = same_x.get('s')
            same_x_end = same_x.get('e')
            if same_x_start:
                same_x_start = sorted(same_x_start, reverse=True)
                for s_i in same_x_start:
                    start_end_array.append((x, s_i, True))
            if same_x_end:
                same_x_end = sorted(same_x_end)
                for e_i in same_x_end:
                    start_end_array.append((x, e_i, False))

        priority_que_dict = {0 : 1}
        ans = []
        # priority_que = _heapify_max([])

        max_height = -1
        for corrd in start_end_array:

            if corrd[2]:
                if corrd[1] in priority_que_dict:
                    priority_que_dict[corrd[1]] += 1
                else:
                    priority_que_dict[corrd[1]] = 1
                    # priority_que = heappop(list(priority_que_dict.keys()))

                    test = list(priority_que_dict.keys())
                    _heapify_max(test)


            else:
                priority_que_dict[corrd[1]] -= 1
                if priority_que_dict[corrd[1]] == 0:
                    del priority_que_dict[corrd[1]]
                    # priority_que = list(priority_que_dict.keys())
                    # _heappop_max(test)
                    test = list(priority_que_dict.keys())
                    _heapify_max(test)



            height = test[0]
            if max_height != height:
                max_height = height
                ans.append([corrd[0], height])
        return ans

sol = Solution()
print(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))