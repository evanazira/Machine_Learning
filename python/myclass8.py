class participant:
    course = "Python data science / machine learing"

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        count = 1
        print(self.fname, self.lname, count)

    def getFullname(self):
        print(self.fname, self.lname)

khairi = participant("Kahiri","abu baKarr")
print(khairi.fi)