"""
This solution is more verbose, but it is also faster since it 
catches an unbalanced string at the first offending bracket 
rather than requiring that the entire string always be read.
"""
class BracketAnalyzer(object):
    def balance_check(self, br_str):
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]
        open_stack = []
        for index, br in list(enumerate(br_str)):
            if br in opening:
                if len(open_stack) >= len(br_str[index:]):
                    print "NO"
                    return
                else:
                    open_stack.append(br)
            elif br in closing:
                if len(open_stack) == 0:
                    print "NO"
                    return
                else:
                    if open_stack.pop() == opening[closing.index(br)]:
                        continue
                    else:
                        print "NO"
                        return

        print("YES" if len(open_stack) == 0 else "NO")

if __name__ == "__main__":
    num = int(raw_input().strip())
    for br_str in xrange(num):
        br_str = raw_input().strip()
        ba = BracketAnalyzer()
        ba.balance_check(br_str)


