# CTF Challenge: ReadMyCert

## Challenge Description
How about we take you on an adventure on exploring certificate signing requests? Take a look at this CSR file here.

**Hint:** Download the certificate signing request and try to read it.

## Solution Approach

### Understanding Certificate Signing Requests (CSR)

A Certificate Signing Request (CSR) is a message sent from an applicant to a Certificate Authority (CA) in order to apply for a digital identity certificate. It contains information that will be included in the certificate such as the organization name, common name (domain name), locality, and country. It also contains the public key that will be included in the certificate.

### Examining the CSR File

After downloading the provided CSR file, I opened it to examine its contents:

```
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF81N2Y1
ODgzMn0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBANZde4bKP/88bBY0RM2b+EyGoxWqWsADa7QIPRZM4jTAxPTC39Ld
6iDZwfA6Cu33KvkZbu1JpAFk/6O/lY+iwSCcZnBTp1p+Skn/BpIwW7KBEjnczulA
c/u4GYQgpU5Pxxd/gvOHLNtWHw8FjcHAV78Y23cwwfO1Gfae5eYrxHMa/nCiQmjC
9GwRsj2+cPmWiyFs1ntLREBGUKWBIHGoTR+ZMXv9aBeasIUlzWap/4ZsSOqoqzAL
3geZ9TfWd/pHtYgqA1jV60ogmWD2LKMU9F4s+5dJveO/5kV7kkpk+7VX3xlE1t/S
0/ThtcNU51WdfmFREr2hCUJgicQHbkkwq00CAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAHihiiyg
z69vMceQR0gOoTZS1RQKafdyX64IxwEuHdV8I0To+3VQp+3yp2yHNAjLxLEIam6f
4dlTZlWSSttHSjp1WjoabpQrSp7ANgTuLFwBsQkbXY72wm0LVrdSi1tuKTnl82vM
mXccuWLUXy71wmzKR+Wekf5JXX9AwFAEVedyAW5EP+bNOP/hQr1kiOCWge3pmGUq
9fVYITJs6gZ6aiDwx4O2jdJuP3CG1QRrKer89mgw5GkgvcVn38s7BF24kRddcBK1
RGSntFXy1CDUd55IhSoADxrZoXT5+5+GokM85JKTkwS9L/VGe2ZQuym+NyIkbfBm
I+FejxNz7x4Fmzg=
-----END CERTIFICATE REQUEST-----
```

This is a PEM-encoded Certificate Signing Request (CSR), which contains information about the entity requesting a certificate and their public key.

### Using OpenSSL to Read the CSR

Since we are dealing with certificate files, OpenSSL is the appropriate tool to decode and read the contents of the CSR file. I used the following command:

```bash
openssl req -in readmycert.csr -noout -text
```

This command tells OpenSSL to:
- `req`: Work with PKCS#10 certificate requests
- `-in readmycert.csr`: Read from the file named "readmycert.csr"
- `-noout`: Don't output the encoded version
- `-text`: Output the decoded request in text format

### Extracting the Flag

Running the OpenSSL command revealed the following detailed information about the CSR:

```
Certificate Request:
    Data:
        Version: 0 (0x0)
        Subject: CN=picoCTF{read_mycert_57f58832}/name=ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:d6:5d:7b:86:ca:3f:ff:3c:6c:16:34:44:cd:9b:
                    f8:4c:86:a3:15:aa:5a:c0:03:6b:b4:08:3d:16:4c:
                    e2:34:c0:c4:f4:c2:df:d2:dd:ea:20:d9:c1:f0:3a:
                    0a:ed:f7:2a:f9:19:6e:ed:49:a4:01:64:ff:a3:bf:
                    95:8f:a2:c1:20:9c:66:70:53:a7:5a:7e:4a:49:ff:
                    06:92:30:5b:b2:81:12:39:dc:ce:e9:40:73:fb:b8:
                    19:84:20:a5:4e:4f:c7:17:7f:82:f3:87:2c:db:56:
                    1f:0f:05:8d:c1:c0:57:bf:18:db:77:30:c1:f3:b5:
                    19:f6:9e:e5:e6:2b:c4:73:1a:fe:70:a2:42:68:c2:
                    f4:6c:11:b2:3d:be:70:f9:96:8b:21:6c:d6:7b:4b:
                    44:40:46:50:a5:81:20:71:a8:4d:1f:99:31:7b:fd:
                    68:17:9a:b0:85:25:cd:66:a9:ff:86:6c:48:ea:a8:
                    ab:30:0b:de:07:99:f5:37:d6:77:fa:47:b5:88:2a:
                    03:58:d5:eb:4a:20:99:60:f6:2c:a3:14:f4:5e:2c:
                    fb:97:49:bd:e3:bf:e6:45:7b:92:4a:64:fb:b5:57:
                    df:19:44:d6:df:d2:d3:f4:e1:b5:c3:54:e7:55:9d:
                    7e:61:51:12:bd:a1:09:42:60:89:c4:07:6e:49:30:
                    ab:4d
                Exponent: 65537 (0x10001)
        Attributes:
        Requested Extensions:
            X509v3 Extended Key Usage:
                TLS Web Client Authentication
    Signature Algorithm: sha256WithRSAEncryption
         78:a1:8a:2c:a0:cf:af:6f:31:c7:90:47:48:0e:a1:36:52:d5:
         14:0a:69:f7:72:5f:ae:08:c7:01:2e:1d:d5:7c:23:44:e8:fb:
         75:50:a7:ed:f2:a7:6c:87:34:08:cb:c4:b1:08:6a:6e:9f:e1:
         d9:53:66:55:92:4a:db:47:4a:3a:75:5a:3a:1a:6e:94:2b:4a:
         9e:c0:36:04:ee:2c:5c:01:b1:09:1b:5d:8e:f6:c2:6d:0b:56:
         b7:52:8b:5b:6e:29:39:e5:f3:6b:cc:99:77:1c:b9:62:d4:5f:
         2e:f5:c2:6c:ca:47:e5:9e:91:fe:49:5d:7f:40:c0:50:04:55:
         e7:72:01:6e:44:3f:e6:cd:38:ff:e1:42:bd:64:88:e0:96:81:
         ed:e9:98:65:2a:f5:f5:58:21:32:6c:ea:06:7a:6a:20:f0:c7:
         83:b6:8d:d2:6e:3f:70:86:d5:04:6b:29:ea:fc:f6:68:30:e4:
         69:20:bd:c5:67:df:cb:3b:04:5d:b8:91:17:5d:70:12:b5:44:
         64:a7:b4:55:f2:d4:20:d4:77:9e:48:85:2a:00:0f:1a:d9:a1:
         74:f9:fb:9f:86:a2:43:3c:e4:92:93:93:04:bd:2f:f5:46:7b:
         66:50:bb:29:be:37:22:24:6d:f0:66:23:e1:5e:8f:13:73:ef:
         1e:05:9b:38
```

Looking at the "Subject" field, I found the flag embedded in the Common Name (CN):

```
Subject: CN=picoCTF{read_mycert_57f58832}/name=ctfPlayer
```

## Tools Used
- OpenSSL - Versatile command-line tool for working with certificates, keys, and cryptographic operations

## Conclusion
This challenge introduced the concept of Certificate Signing Requests (CSRs) and how to examine their contents using OpenSSL. CSRs are an important part of Public Key Infrastructure (PKI) and are used in the process of obtaining SSL/TLS certificates for secure communications. Understanding how to read and interpret CSRs is a valuable skill in cybersecurity, particularly for those working with web security and encryption.

## Flag
`picoCTF{read_mycert_57f58832}`
