Enabling transport security
===========================

Possible Architectures:

- Create one self-signed sertificate and key, distribute it and use it with
  all agents -> quick and dirty

- Create one root CA which signs a CSR for each machine.  Each machine has its
  own certificate and key

- Create one root CA and several intermediate CAs for each agent type.  Each
  agent uses a certificate signed by the corresponding CA.  Agents only trust
  the subset of intermediate CA that they need to connect to.

Create Root CA, 2048 bits might also be okay.  You should use a good
passphrase. The key should never leave the machine.  Depending on your security
needs you may need to be more or less paranoid:

.. code-block:: bash

   $ openssl genrsa -aes256 -out ca.key 4096

Sigh the key and create a root certificate.  You use this for signing each
machines public key:

.. code-block:: bash

   $ openssl req  -new -x509 -nodes -key ca.key -out ca.crt -days 1000

Create a key and a certificate signing request (CSR) on a machine:

.. code-block:: bash

   $ openssl req -new -nodes -newkey rsa:2048 -keyout device.key -out device.csr -days 365

Now you can sign the device key with your CA cert:

.. code-block:: bash

   $ openssl x509 -CA ca.crt -CAkey ca.key -CAcreateserial -req -in device.csr -out device.pem -days 365

Create SSL Context:

.. code-block:: python

   import ssl
   c = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
   c.verify_mode = ssl.CERT_REQUIRED
   c.verify_flags = ssl.VERIFY_CRL_CHECK_CHAIN
   c.check_hostname = True
   c.options |= ssl.OP_SINGLE_DH_USE
   c.options |= ssl.OP_SINGLE_ECDH_USE
   c.options |= ssl.OP_NO_COMPRESSION
   c.load_cert_chain('device.pem', 'device.key')
   c.load_verify_locations(cafile='ca.crt')
   c.set_ciphers('ECDH+AESGCM')
