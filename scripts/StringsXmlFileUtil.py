#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from Log import Log
import  xml.dom.minidom

class StringsXmlFileUtil:
    'android strings.xml file util'

    @staticmethod
    def writeToFile(keys, values,directory,additional):
        if not os.path.exists(directory):
            os.makedirs(directory)

        Log.info("Creating android file:" + directory + "/strings.xml")

        fo = open(directory + "/strings.xml", "wb")

        stringEncoding = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n"
        fo.write(stringEncoding)

        for x in range(len(keys)):
            if values[x] is None or values[x] == '' :
                Log.error("Key:" + keys[x] + "\'s value is None. Index:" + str(x + 1))
                continue

            key = keys[x]
            value = values[x]
            content = ''
            if value.endswith('|'):
                content = "   <array name=\"" + key + "\">\n"
                items = value.split('|')
                for i in range(len(items)-1):
                    content += "      <item>" + items[i] + "</item>\n"

                content += "   </array>\n"
            else:
                content = "   <string name=\"" + key + "\">" + value + "</string>\n"

            fo.write(content);

        if additional is not None:
            fo.write(additional)

        fo.write("</resources>");
        fo.close()

    @staticmethod
    def getKeysAndValues(path):
        if path is None:
            Log.error('file path is None')
            return

        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        itemlist = root.getElementsByTagName('string')

        keys = []
        values = []
        for index in range(len(itemlist)):
            item = itemlist[index]
            key = item.getAttribute("name")
            if item.firstChild == None:
                value = ''
            else:
                value = item.firstChild.data

            Log.info("key:" + key + " value:" + value)
            keys.append(key)
            values.append(value)

        return (keys,values)

    @staticmethod
    def getStringArray(path):
        if path is None:
            Log.error('file path is None')
            return

        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        itemlist = root.getElementsByTagName('array')

        keys = []
        values = []

        for index in range(len(itemlist)):
            item = itemlist[index]
            key = item.getAttribute("name")
            value = ''
            valuelist = item.getElementsByTagName('item')
            for i in range(len(valuelist)):
                vv = valuelist[i]
                value += vv.firstChild.data
                value += '|'

            keys.append(key)
            values.append(value)
            #print 'key=' + key +',value=' + value
            #print '#######################'

        return (keys,values)
