import os
PATH = "/Volumes/Release/Projects/SDK"
import subprocess


# for path, dirs, files in os.walk(PATH):
#     # print path
#     print dirs
    # print files
def printList():

    l = subprocess.Popen(["ls", PATH], stdout=subprocess.PIPE)
    output, err = l.communicate()
    # print output

    keys = output.split('\n')
    del keys[len(keys) - 1]
    for key in keys:
        # print PATH + "/" + key
        i = subprocess.Popen(["ls", PATH + "/" + key], stdout=subprocess.PIPE)
        output, err = i.communicate()
        lis = output.split("\n")
        del lis[len(lis) - 1]
        for n in lis:
            # print "\t",PATH +"/" + key + "/" + n
            i = subprocess.Popen(["ls", PATH + "/" + key + "/" + n], stdout=subprocess.PIPE)
            output, err = i.communicate()
            output = output.split("\n")
            del output[len(output) - 1]
            for m in output:
                print PATH + "/" + key + "/" + n + "/" + m


def printTree():
    PATH = "/Users/terences/PychamProjects/sandbox/output"
    if os.path.exists(PATH) != True:
        os.makedirs(PATH)
    f = file("/Users/terences/PycharmProjects/sandbox/repos.txt")
    l = f.readlines()
    for dir in l:
        dir_loc =  dir.replace("\n","")
        print dir_loc
        dir = dir.split("/")
        proj = dir[len(dir) - 3]
        branch = dir[len(dir) - 2]
        vers = dir[len(dir) - 1]
        if (os.path.isfile("/Users/terences/PycharmProjects/sandbox/output/" + proj + "-" + branch + "-" + vers + ".txt") != True):
            i = subprocess.Popen(["tree", dir_loc], stdout=subprocess.PIPE)
            output, err = i.communicate()

            wf = open("/Users/terences/PycharmProjects/sandbox/output/" + proj + "-" + branch + "-" + vers + ".txt", "w")
            wf.write(output)
            wf.close()
        # print output

printTree()