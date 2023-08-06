Pythia PRF Protocol
--------------------
Pythia provides a secure, updateable, verifiable, rate-limited psuedorandom
function service for clients and servers. Essentially, we can turn weak 
passwords into strong cyrptographic keys and use rate-limiting to detect and
prevent an attacker from guessing your password.

Requirements
--------------
Pythia requires the Charm Crypto Library for Python: 
http://www.charm-crypto.com/Download.html
If there was a PIP package, we'd automatically install upon installing Pythia, but there isn't: sorry.