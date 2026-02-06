import xml.etree.ElementTree as ET

rang = '''<car>
    <specs> 
    <model> Audi </model>
    <year> 2021 </year>
    </specs>
</car>'''

audi = ET.fromstring(rang)
print('The car specifications are:', audi.find('specs/model').text)
