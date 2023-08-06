nitor-vault
===========

Command line tools and libraries for encrypting keys and values using client-side encryption with AWS KMS keys.

# Installation

The easiest install is the python package from pypi:
```
pip install nitor-vault
```

Javascript and java versions are available from npm and maven central respectively and installation will depend on your needs.

# Example usage

Initialize vault bucket and other infrastructure: `vault --init`. Will create a CloudFormation stack.

Encrypt a file and store in vault bucket: `vault -s my-key -f <file>`

Decrypt a file: `vault -l <file>`

Encrypt a single value and store in vault bucket `vault -s my-key -v my-value`

Decrypt a single value `vault -l my-key`

## Using encrypted CloudFormation stack parameters

Encrypt a value like this: `$ vault -e 'My secret value'`

The command above will print the base64 encoded value encrypted with your vault KMS key. Use that value in a CF parameter. The value is then also safe to commit into version control and you can use it in scripts for example like this:

```
#!/bin/bash

MY_ENCRYPTED_SECRET="AQICAHhu3HREZVp0YXWZLoAceH1Nr2ZTXoNZZKTriJY71pQOjAHKtG5uYCdJOKYy9dhMEX03AAAAbTBrBgkqhkiG9w0BBwagXjBcAgEAMFcGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMYy/tKGJFDQP6f9m1AgEQgCq1E1q8I+btMUdwRK8wYFNyE/5ntICNM96VPDnYbeTgcHzLoCx+HM1cGvc"


UNENCRYPTED_SECRET="$(vault -y $MY_ENCRYPTED_SECRET)"
```

Obviously you need to make sure that in the context of running vault there is some sort of way for providing kms permissions by for example adding the decryptPolicy managed policy from the vault cloudformation stack to the ec2 instance or whatever runs the code.

To decrypt the parameter value at stack creation or update time, use a custom resource:

```
Parameters:
  MySecret:
    Type: String
    Description: Param value encrypted with KMS
Resources:
  DecryptSecret:
    Type: "Custom::VaultDecrypt"
    Properties:
      ServiceToken: "arn:aws:lambda:<region>:<account-id>:function:vault-decrypter"
      Ciphertext: { "Ref": "MySecret" }
  DatabaseWithSecretAsPassword:
    Type: "AWS::RDS::DBInstance"
    Properties:
      ...
      MasterUserPassword:
        Fn::Sub: ${DecryptSecret.Plaintext}
```

# Licence

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
