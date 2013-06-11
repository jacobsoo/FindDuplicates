import os,sys

def main(file1, file2):
    x = set([i.strip() for i in open(file1)])
    y = set([i.strip() for i in open(file2)])
    z = x.intersection(y)
    szFile1 = os.path.splitext(file1)[0]
    szFile2 = os.path.splitext(file2)[0]
    szOutName = szFile1 + "-" + szFile2 + ".txt"
    outfile = open(szOutName, 'wb')
    for i in z:
        outfile.write(i+"\r\n")
    outfile.close()

# Banner
def Banner():
    print("=================================================")
    print("Find Duplicates v0.1                             ")
    print("=================================================")

# Usage
def help_menu(cmd):
    print("Usage: %s <file_1> <file_2>\n") % (cmd)
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        help_menu(sys.argv[0])
        exit(0)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    main(file1, file2)
