import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl>
        +1 734 303 4465
    </phone>
    <emial hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)