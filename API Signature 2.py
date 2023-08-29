from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Sig_pk
import base64
import os
import json

def get_sign(data):
    path = os.path.dirname(os.path.abspath(__file__))
    doc = os.path.join(path, 'private_key.pem')
    with open(doc) as pk:
        key_data = pk.read()

    output_file_path = os.path.join(path, 'output.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        print("key_data:", key_data, file=output_file)

    rsakey = RSA.importKey(key_data)
    en_data = SHA.new(data.encode())
    sig_pk = Sig_pk.new(rsakey)
    sign = sig_pk.sign(en_data)
    result = base64.b64encode(sign)
    data = result.decode()

    with open(output_file_path, 'a', encoding='utf-8') as output_file:
        print("get_sgin接收到用例报文：", data, file=output_file)
        print("生成的decode-sign:", data, file=output_file)

    return data

def format_data(data):
    return data.replace(' ', '')

if __name__ == '__main__':
    data3 = {"nonce": "82", "timestamp": "1689693881000", "x-sign-uri": "/cube/v4/sims/89882390000370600614"}
    sx_data = json.dumps(data3, sort_keys=True, ensure_ascii=False)
    fdata = format_data(sx_data)

    output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        print("fdata:", fdata, file=output_file)

    get_sign(fdata)
