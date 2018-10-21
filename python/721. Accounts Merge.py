class Solution:
    def accountsMerge(self, accounts):
        email_dcit = {}
        i = 0
        for arr in accounts:
            if arr[0] in email_dcit:
                email_dcit[arr[0]].append(i)
            else:
                email_dcit[arr[0]] = [i]
            i += 1

        i = 0

        for arr in accounts:
            indices = email_dcit.get(arr[0])
            for ind in indices:
                if ind == i:
                    continue

            i += 1
