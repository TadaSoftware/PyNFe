from lxml import etree
import signxml
from signxml import xmldsig

cert = open("cert.pem").read()
key = open("key.pem", "rb").read()

root = etree.parse('texte.xml').getroot()
signer = xmldsig(root, digest_algorithm="sha1")
signer.sign(method=signxml.methods.enveloped, key=key, cert=cert,
            algorithm="rsa-sha1", c14n_algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315',
            reference_uri='#NFe41150715380524000122651010000000271333611649')
#verified_data = signer.verify(require_x509=True, ca_pem_file="cert.pem")
e = etree.tostring(signer.data)
open("testesig.xml", "wb").write(e)

