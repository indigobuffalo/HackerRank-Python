class BracketAnalyzer(object):
    def corresponding_type(self, bracket):
        if bracket == "[":
            return "]"
        elif bracket == "(":
            return ")"
        elif bracket == "{":
            return "}"

    def brackets_match(self, bracket_string):
        return self.corresponding_type(bracket_string[0]) == bracket_string[-1]

    def is_balanced(self, bracket_string):
        if not bracket_string:
            raise Exception("No string passed in")
        elif len(bracket_string) == 2:
            if self.brackets_match(bracket_string):
                print "YES"
            else:
                print "NO"
        elif len(bracket_string) % 2 != 0:
            print "NO"
        else:
            if self.brackets_match(bracket_string):
                self.is_balanced(bracket_string[1:-1])
            else:
                print "NO"


if __name__ == "__main__":
    t = int(raw_input().strip())
    ba = BracketAnalyzer()
    for i in xrange(t):
        s = raw_input().strip()
        ba.is_balanced(s)

