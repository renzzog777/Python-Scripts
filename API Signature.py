from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
import base64
import os
import json

def get_sgin():
    rsa = RSA.generate(1024)
    private_key.pem = rsa.exportKey()
    print(private_key.pem)
    with open('private_key.pem', 'wb') as f:
        f.write(private_key.pem)
    print(private_key.pem)
    public_pem = rsa.publickey().exportKey()
    with open('public.pem', 'wb') as f:
        f.write(public_pem)
    print(public_pem)
    name = "musen"
    rsakey = RSA.importKey(private_key.pem)
    data = SHA.new(name.encode())
    sig_pk = Sig_pk.new(rsakey)
    sign = sig_pk.sign(data)
    result = base64.b64encode(sign)
    data = result.decode()
    print(data)

def get_sign(data):
    path = os.path.dirname(os.path.abspath(__file__))
    doc = os.path.join(path, 'private_key.pem')
    with open(doc) as pk:
        key_data = pk.read()
    print("key_data:", key_data)
    rsakey = RSA.importKey(key_data)
    print("get_sgin接收到用例报文：", data)
    en_data = SHA.new(data.encode())
    sig_pk = Sig_pk.new(rsakey)
    sign = sig_pk.sign(en_data)
    result = base64.b64encode(sign)
    data = result.decode()
    print("生成的decode-sign:", data)
    return data

def format_data(data):
    return data.replace(' ','')

if __name__ =='__main__':
    #set the data here
    data3={"nonce":"82","timestamp":"1689693881000","x-sign-uri":"/cube/v4/sims/89860202303 20011XXXX"}
    sx_data = json.dumps(data3, sort_keys=True, ensure_ascii=False)
    # print(type(sx_data))
    fdata = format_data(sx_data)
    print("fdata:", fdata)
    get_sign(fdata)

  