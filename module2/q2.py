import math

class DataProfiler():
    def __init__(self, _list):
        self.list = _list
        self.mean = None
        self.min = None
        self.max = None
    def get_summary_stats(self):
        self.mean = sum(self.list) / len(self.list)
        self.min = min(self.list)
        self.max = max(self.list)
        return self.mean, self.min, self.max
    def get_mmscale(self):
        mms_lamda = lambda num: (num - self.min) / ((self.max) - (self.min))
        mms_list = [mms_lamda(num) for num in self.list]
        return mms_list
    def get_zscore_scale(self):
        items = [(_num - self.mean) ** 2 for _num in self.list]
        item_sum = sum(items)
        sd = math.sqrt(item_sum / (len(self.list)))
        zscores = [((_num - self.mean) / sd) for _num in self.list]
        return zscores

if __name__ == "__main__":
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    profiler0 = DataProfiler(b)
    stats = profiler0.get_summary_stats()
    print("Mean = " + str(stats[0]))
    print("Min = " + str(stats[1]))
    print("Max = " + str(stats[2]))
    mmscale = profiler0.get_mmscale()
    print("Min Max scale b = " +  str(mmscale))
    zscores = profiler0.get_zscore_scale()
    print("ZScores of b = " + str(zscores))

