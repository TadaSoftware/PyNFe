# To export the private key without a passphrase or password.
# Type: openssl pkcs12 -in filename.pfx -nocerts -nodes -out key.pem
#  
# To Generate a public version of the private RSAkey
# Type: openssl rsa -in key.pem -out server.key
#  
# To export the Certificate
# Type: openssl pkcs12 -in filename.pfx -clcerts -nokeys -out cert.pem
#  
# The directory will now have a file cert.pem and a key.pem.

openssl pkcs12 -in JC.pfx -nocerts -nodes -out key.pem -passin pass:12345678
openssl pkcs12 -in JC.pfx -clcerts -nokeys -out cert.pem -passin pass:12345678