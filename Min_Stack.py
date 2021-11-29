{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 "Time Complexity - O(1)"\
"Space Complexity - O(n)"\
\
class MinStack(object):\
\
    def __init__(self):\
        self.stack = []\
        self.min_value = float('inf')\
       \
    \
    def push(self, val):\
        """\
        :type val: int\
        :rtype: None\
        """\
        if self.min_value >= val:\
            self.stack.append(self.min_value)\
            self.min_value = val\
        self.stack.append(val)\
        \
\
    def pop(self):\
        """\
        :rtype: None\
        """\
        popped = self.stack.pop()\
        if popped == self.min_value:\
            self.min_value = self.stack.pop()\
        \
\
    def top(self):\
        """\
        :rtype: int\
        """\
        return self.stack[-1]\
        \
\
    def getMin(self):\
        """\
        :rtype: int\
        """\
        return self.min_value\
\
# Your MinStack object will be instantiated and called as such:\
# obj = MinStack()\
# obj.push(val)\
# obj.pop()\
# param_3 = obj.top()\
# param_4 = obj.getMin()}