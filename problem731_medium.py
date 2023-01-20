# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2023/1/19 20:10
"""
"""
实现一个 MyCalendar 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。
MyCalendar 有一个 book(int start, int end)方法。它意味着在 start 到 end 时间内增加一个日程安排，注意，这里的时间是半开区间，
即 [start, end), 实数 x 的范围为，  start <= x < end。
当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。
每次调用 MyCalendar.book方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 true。
否则，返回 false 并且不要将该日程安排添加到日历中。
请按照以下步骤调用MyCalendar 类: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

示例：
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
解释： 
前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。
"""
"""
思路：首先检测新加入的区间 [start,end) 是否与已经预定过两次的区间有交集，如果没有冲突，则将新加入的区间与已经预定的区间进行检查，
求出新增的预定两次的区间。对于两个区间 [s1，e1) 和 [s2，e2)，则他们之间的交集为 [max(s1,s2),min(e1,e2))。
"""


class MyCalendarTwo:
    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        if any(s < end and start < e for s, e in self.overlaps):
            return False
        for s, e in self.booked:
            if s < end and start < e:
                self.overlaps.append((max(s, start), min(e, end)))
        self.booked.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
