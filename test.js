#!/usr/bin/node
//import * as crypto from 'crypto';
crypto = require('crypto')

let secret = "sneee"
if (process.argv[2] == "-E") {
    const algorithm = "aes-192-cbc";
    //const salt = "h";
    let key = crypto.scryptSync(secret, 'salt', 24);
    let cipher = crypto.createCipher(algorithm, key)

    let encrypted = '';
    cipher.on('readable', () => {
        let chunk;
        while (null !== (chunk = cipher.read())) {
            encrypted += chunk.toString('hex')
        }
        //console.log('cookie',encrypted)
    })

    cipher.on('end', () => {
        //encrypted = 'decrypt_it='+encrypted
        //resp.writeHead(200,{'Set-Cookie':encrypted})
        //resp.write(str)
        console.log(encrypted)
    })
    cipher.write(process.argv[3]);
    cipher.end()
}

else if (process.argv[2] == "-D") {
    const algorithm_ = "aes-192-cbc";
    let key = crypto.scryptSync(secret, 'salt', 24)
    let decipher = crypto.createDecipher(algorithm_, key);

    let decrypted = '';
    decipher.on('readable', () => {
        let chunk;
        while (null !== (chunk = decipher.read())) {
            decrypted += chunk.toString('utf-8')
        }
    })
    decipher.on('end', () => {
        console.log(decrypted)
    })
    decipher.write(process.argv[3], 'hex');
    decipher.end()
}
else {
    console.log("invalid argument")
}
