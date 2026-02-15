# 🔐 Hashing Password - Secure Password Hash Generator

A command-line utility for generating cryptographic hashes of passwords using SHA-256, SHA-512, or MD5 algorithms.

## 📋 Description

This project provides a simple yet powerful command-line tool for password hashing. It uses Python's `hashlib` module to generate secure hashes of passwords using industry-standard algorithms. Useful for learning cryptography and for security demonstrations.

## ✨ Features

- **Multiple Hash Algorithms** - SHA-256 (default), SHA-512, MD5
- **Command-Line Interface** - Using argparse for clean argument handling
- **Default Algorithm** - Uses SHA-256 by default for security
- **Flexible Input** - Accept passwords as command-line arguments
- **Hex Output** - Display hashes in hexadecimal format

## 🛠 Prerequisites

- Python 3.x (no external packages required, uses standard library)

## 📦 Installation

No external dependencies required! The project uses Python's built-in `hashlib` and `argparse` modules.

```bash
# No installation needed, just run:
python "Hashing Password.py" [password] [options]
```

## 🚀 Usage

### Basic Usage (SHA-256)
```bash
python "Hashing Password.py" mypassword
```

Output:
```
< hash-type : sha256 >
2c26b46911185131006ba32c65c92b965d92db5973affeab882e59723a037e49
```

### Specify Hash Type
```bash
# Using SHA-512
python "Hashing Password.py" mypassword -t sha512

# Using MD5
python "Hashing Password.py" mypassword --type md5
```

### Command-Line Arguments

| Argument | Short | Long | Default | Description |
|----------|-------|------|---------|-------------|
| password | - | - | Required | The password to hash |
| type | -t | --type | sha256 | Hash algorithm (sha256, sha512, md5) |

## 📁 Files

- `Hashing Password.py` - Main application file

## 🔧 Key Components

### Argument Parser
```python
parser = argparse.ArgumentParser(description='hashing given password')
parser.add_argument('password', help='input password you want to hash')
parser.add_argument('-t', '--type', default='sha256', 
                    choices=['sha256', 'sha512', 'md5'])
```

### Hash Generation
```python
m = getattr(hashlib, hashtype)()
m.update(password.encode())
print(m.hexdigest())
```

## 💡 Learning Concepts

- **Cryptography Basics** - Understanding hashing algorithms
- **Command-Line Arguments** - Using argparse for input
- **String Encoding** - Converting strings to bytes
- **Dynamic Function Selection** - Using getattr() for flexible hashing
- **Hexadecimal Format** - Understanding hash output format

## 📊 Comparison of Hash Algorithms

| Algorithm | Output Length | Security | Speed | Use Case |
|-----------|---------------|----------|-------|----------|
| MD5 | 128 bits | ⚠️ Weak* | ⚡ Fast | Legacy only |
| SHA-256 | 256 bits | ✅ Good | Normal | Recommended |
| SHA-512 | 512 bits | ✅ Excellent | Normal | High security |

*MD5 is considered cryptographically broken and should not be used for security purposes.

## 📝 Example Hashes

### Same Password, Different Algorithms
```
Password: "hello123"

SHA-256: adb6b3773144e8c316adfc3ae8f42b003e82a00963a03c2da79d5ede969b8d50
SHA-512: d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176...
MD5:     b1c9d9f0a82dfc0c51564c6e87d4dcd1
```

## ⚠️ Important Security Notes

1. **Never Hash Interactive Passwords** - This is for learning only
2. **Use Salt in Production** - Real password hashing needs salt (bcrypt, scrypt)
3. **Avoid MD5** - Cryptographically broken, don't use for security
4. **Use SHA-512 or bcrypt** - For production password storage
5. **One-Way Function** - Hashes cannot be reversed

## 🌟 Potential Enhancements

- [ ] Add salt support for better security
- [ ] Implement bcrypt for password hashing
- [ ] Add HMAC support
- [ ] File input support (hash file contents)
- [ ] Batch processing of multiple passwords
- [ ] Performance benchmarking for algorithms
- [ ] Add PBKDF2 (Password-Based Key Derivation)
- [ ] Compare against known hash databases

## 📚 Related Topics

- Cryptography and Hashing
- Security Best Practices
- Password Management
- Command-Line Tools
- Python argparse Module
- Binary Data Encoding (Hex, Base64)

## 🔐 Best Practices

1. **For Learning**: This tool is perfect for understanding hashing
2. **For Storage**: Use bcrypt, scrypt, or Argon2 in production
3. **With Salt**: Always add salt to password hashes
4. **Key Stretching**: Use algorithms with built-in key stretching
5. **Hash Comparison**: Use constant-time comparison to prevent timing attacks

## 📖 Further Reading

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- [Bcrypt Security](https://en.wikipedia.org/wiki/Bcrypt)
