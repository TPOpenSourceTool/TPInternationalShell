# -*- coding:utf-8 -*-

import os
from optparse import OptionParser
from StringsXmlFileUtil import  StringsXmlFileUtil
import pyExcelerator

#Add command option
def addParser():
    parser = OptionParser()

    parser.add_option("-f", "--filesDirectory",
                      help="StringsXml files directory.",
                      metavar="filesDirectory")

    parser.add_option("-t", "--targetFilePath",
                      help="Target File (xls) Path.",
                      metavar="targetFilePath")

    (options, args) = parser.parse_args()

    return options


# Start convert Strings.xml to xls
def startConvert(options):
    directory = options.filesDirectory
    targetFilePath = options.targetFilePath

    if directory is not None:
        if targetFilePath is not None:
            workbook = pyExcelerator.Workbook()
            for dirname in os.listdir(directory):
                if not dirname.startswith('.'):
                    # print directory + dirname
                    addOneSheet(directory,dirname,workbook)
            filePath = targetFilePath + "/Localizable_Android.xls"
            workbook.save(filePath)
            print "Convert successfully! you can see xls file in %s" % (filePath)

        else:
            print "Target file path can not be empty! try -h for help."
    else:
        print "StringsXml files directory can not be empty! try -h for help."

def addOneSheet(parent,module,workbook):
    directory = parent + module + '/' + module + '/src/main/res/'
    if not os.path.exists(directory + 'values'):
        return

    ws = workbook.add_sheet(module)
    index = 0
    for parent, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            if not dirname.startswith('values'):
                continue

            # KeyName & CountryCode
            if index == 0:
                ws.write(0,0,'keyName')

            conturyCode = 'en'
            dirSplit = dirname.split('values-')
            if len(dirSplit)>1 :
                conturyCode = dirSplit[1]

            ws.write(0,index+1,conturyCode)

            # Key & Value
            path = directory+'/'+dirname+'/strings.xml'
            (keys, values) = StringsXmlFileUtil.getKeysAndValues(path)
            for x in range(len(keys)):
                key = keys[x]
                value = values[x]
                if (index == 0):
                    ws.write(x+1, 0, key)
                    ws.write(x+1, 1, value)
                else:
                    ws.write(x+1, index + 1, value)

            pos = len(keys)
            (ks, vs) = StringsXmlFileUtil.getStringArray(path)
            for i in range(len(ks)):
                k = ks[i]
                v = vs[i]
                if (index == 0):
                    ws.write(pos+i+1, 0, k)
                    ws.write(pos+i+1, 1, v)
                else:
                    ws.write(pos+i+1, index + 1, v)

            index += 1



def main():
    options = addParser()
    startConvert(options)

main()