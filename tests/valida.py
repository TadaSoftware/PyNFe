from lxml import etree

xmlschema_doc = etree.parse('nfse_v202.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

xml = etree.parse('funfa.xml')
print(xmlschema.validate(xml))
xmlschema.assertValid(xml)
