from lxml import etree


def parse():

    xml_string = open('objects.xml', 'rb').read()
    print(xml_string)

    root = etree.XML(xml_string)
    print(etree.tostring(root))

    objects = root
    for object in objects:
        print(etree.tostring(object))
        object_id = object.get('object_id')
        name = object.get('name').text
        location = object.get('location')

        lattitude = location.get('lattituide')
        longitude = location.get('longitude')

        address = location.get('address').text

        print(object_id, name, lattitude, longitude, address)

if __name__ == "__main__":
    parse()


