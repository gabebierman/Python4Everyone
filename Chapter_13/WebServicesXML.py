import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Gabe</name>
    <phone type="intl">
        +1 402 305 8311
    </phone>
    <email hide="yes"/>
</person> '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
