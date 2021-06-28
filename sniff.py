import re
import optparse

#cli argument parser for specifying the input file
parser = optparse.OptionParser()
parser.add_option("-f","--file",dest="f",help="ip file")
#parser.set_defaults(f="text1.txt")
(options,arguments) = parser.parse_args()

if options.f is None:
    print("Enter the input file name: ")
    parser.set_defaults(f=input())
    (options,arguments) = parser.parse_args()

#creating regular expression object for all_ip's and  valid ip's
all_ip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
valid_ip = re.compile(r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([1-9][0-9]|[0-9]|1[0-9[0-9]|2[0-4][0-9]|25[0-5])")

#declaring empty list for storing all ip's and valid ip's respectively
a = []
v = []

#iterating through the lines of the file and looking for a match for all ip's
class ip_sniffer:
    def __init__(self,input_file):
        self.input_file = input_file

        for line in open(input_file):
            for match in re.finditer(all_ip, line):
                a.append(match.group())

#iterating through the lines of the file and looking for a match for only valid ip's
        for line in open(input_file):
            for match in re.finditer(valid_ip, line):
                v.append(match.group())
        self.setv = set(v)

#iterating through the list of all_ip's and extracting ip's other than valid ip's
        self.res = [i for i in a if i not in v]

#writing valid_ip to output1 file
    def generate_log_files(self):
        o = open("output1","w")
        o.write("list of valid ip's\n")
        for i in self.setv:
            out =str(i) + " : " + str(v.count(i))
            o.write(out)
            o.write("\n")
        o.close()
        print("Valid ip's file generated as output1")

#writing invalid_ip to output2 file
        o = open("output2","w")
        o.write("list of invalid ip's\n")
        for i in self.res:
            o.write(i)
            o.write("\n")
        o.close()
        print("Invalid ip's file generated as output2")

#writing duplicate ip's
        o = open("output3","w")
        o.write("list of duplicate ip's\n")
        for i in self.setv:
            if v.count(i) > 1:
                o.write(i)
        print("Duplicate ip's file generated as output3")

obj = ip_sniffer(options.f)
obj.generate_log_files()



