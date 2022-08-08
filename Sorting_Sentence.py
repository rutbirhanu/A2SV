class Solution:
    def sortSentence(self, string: str) -> str:

        ind = []
        final = []
        fin_ind = []
        string = string.split()
        for i in string:
            ind.append(i[-1])
            final.append(i[:-1])

        for i in range(1, 10):
            s = str(i)
            if s in ind:
                indd = ind.index(s)
                fin_ind.append(indd)
        for i, ele in enumerate(fin_ind):
            string[i] = final[ele]

        finaly = " ".join(string)

        return finaly
