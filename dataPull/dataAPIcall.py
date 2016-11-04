from urllib2 import Request, urlopen, URLError
import xml.etree.ElementTree as ET
import requests
import xml.dom.minidom

class Player(object):

    def __init__(self, attrs):
        self.attrs = attrs

    def get_attrs(self):
        return self.attrs

players = requests.get('https://www.fantasybasketballnerd.com/service/players')

try:
    # print players.content
    xml = xml.dom.minidom.parse(players.content)
    players = str(players.content)
    root = ET.fromstring(players)
    print xml.toprettyxml()
except URLError, e:
    print 'Did not work: ', e# coding=utf-8
