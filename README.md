# 🐍 Python Learning Journey + AWS Security Projects

> My path from Python basics to real-world AWS security automation

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![AWS SDK](https://img.shields.io/badge/AWS-boto3-orange.svg)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 👨‍💻 About Me

AWS Cloud Support Engineer learning Python to automate security tasks and improve cloud operations efficiency.

## 📚 Repository Overview

This repository documents my journey learning Python from fundamentals to building production-ready AWS security automation tools. It's structured to be both a learning resource and a portfolio of practical security scripts.

```
python-learning/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── basics/                    # Python fundamentals
├── fundamentals/              # Core Python concepts
└── projects/                  # Real-world applications
    ├── aws-security-scripts/  # Security auditing tools
    └── incident-response/     # IR automation
```

---

## 📖 Learning Path

### 🔰 Stage 1: Python Basics (`basics/`)

Foundational Python concepts with security-focused examples.

| File | Topic | Key Concepts |
|------|-------|--------------|
| `01_variables.py` | Variables & Data Types | Variable assignment, naming conventions, type hints |
| `02_data_types.py` | Core Data Types | Strings, integers, floats, booleans, type conversion |
| `03_conditions.py` | Conditional Logic | if/elif/else, comparison operators, logical operators |
| `04_loops.py` | Iteration | for loops, while loops, break, continue, enumerate |
| `05_functions.py` | Functions | Function definition, parameters, return values, scope |
| `06_lists.py` | Lists | List operations, indexing, slicing, list comprehensions |
| `07_dictionaries.py` | Dictionaries | Key-value pairs, methods, iteration, nested structures |
| `08_file_handling.py` | File I/O | Reading, writing, context managers, file formats |
| `09_error_handling.py` | Exception Handling | try/except blocks, custom exceptions, error logging |
| `10_classes.py` | Object-Oriented Programming | Classes, objects, methods, inheritance |

**How to Run:**
```bash
cd basics
python 01_variables.py
```

**Key Learnings:**
- Python is dynamically typed but supports type hints
- Indentation defines code blocks (not brackets!)
- Use `snake_case` for variables and functions
- Functions should have a single, clear purpose
- Lists are ordered and mutable; dictionaries provide fast lookups

---

### 🔧 Stage 2: AWS with Boto3 (`fundamentals/`)

AWS SDK for Python with security-focused examples.

| File | Topic | AWS Services |
|------|-------|--------------|
| `01_boto3_intro.py` | Boto3 Setup | Sessions, clients, resources, credentials |
| `02_iam_basics.py` | Identity & Access Management | Users, roles, policies, permissions |
| `03_s3_basics.py` | Simple Storage Service | Buckets, objects, encryption, access control |
| `04_ec2_basics.py` | Elastic Compute Cloud | Instances, security groups, key pairs |

**Prerequisites:**
```bash
pip install boto3
aws configure
```

**Security Best Practices:**
- ✅ Use least privilege IAM roles
- ✅ Enable MFA for privileged accounts
- ✅ Encrypt S3 buckets by default
- ✅ Restrict security group rules to specific IPs
- ✅ Rotate access keys regularly

---

## 🚀 Projects

### 🔐 Project 1: AWS Security Scripts

Comprehensive security auditing toolkit for AWS environments.

**Directory Structure:**
```
aws-security-scripts/
├── README.md                      # Project documentation
├── security_audit_report.py       # Complete security audit
├── iam/
│   ├── who_am_i.py               # Check current identity
│   └── list_users.py             # List IAM users with details
├── s3/
│   ├── list_buckets.py           # List all S3 buckets
│   └── check_public_buckets.py   # Find publicly accessible buckets
├── ec2/
│   ├── list_instances.py         # List EC2 instances
│   └── check_security_groups.py  # Find risky security group rules
└── kms/
    └── check_public_keys.py      # Find KMS keys with public access
```

**Features:**
- 🔍 **Security Audit Report**: Comprehensive AWS security posture check
- 🪣 **S3 Bucket Scanner**: Identify public buckets and encryption status
- 🔑 **IAM Analyzer**: List users, check for unused credentials
- 🛡️ **Security Group Auditor**: Find overly permissive rules (0.0.0.0/0)
- 🔐 **KMS Key Inspector**: Check key policies for public access

**Usage:**
```bash
cd projects/aws-security-scripts

# Run full security audit
python security_audit_report.py

# Check for public S3 buckets
python s3/check_public_buckets.py

# Audit security groups
python ec2/check_security_groups.py
```

**Sample Output:**
```
🔍 AWS Security Audit Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ IAM Users: 12 active users
⚠️  Public S3 Buckets: 3 found
❌ Risky Security Groups: 5 groups allow 0.0.0.0/0
✅ KMS Keys: All keys properly secured
```

---

### 🚨 Project 2: Incident Response Automation

Automated containment for AWS credential compromise scenarios.

**Directory Structure:**
```
incident-response/
├── README.md                 # Project documentation
├── contain_credentials.py    # Main containment script
└── ssm_document.yaml        # SSM Automation document
```

**What It Does:**

When AWS credentials are compromised (e.g., leaked to GitHub), this script automatically:

1. ✋ **Disables** the compromised IAM user
2. 🔒 **Revokes** all active sessions
3. 🗑️ **Removes** all access keys
4. 🚫 **Attaches** an explicit deny policy

**Usage:**
```bash
cd projects/incident-response

# Run with parameters
python contain_credentials.py \
  --username compromised-user \
  --access-key AKIA...

# Interactive mode
python contain_credentials.py
```

**SSM Automation:**
The included `ssm_document.yaml` can be deployed to AWS Systems Manager for automated response:
```bash
aws ssm create-document \
  --name ContainCompromisedCredentials \
  --document-type Automation \
  --content file://ssm_document.yaml
```

---

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/master-coder1998/python.git
cd python
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials
```bash
aws configure
```

You'll need:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-1`)
- Output format (e.g., `json`)

### 4. Set Up Python Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📋 Requirements

- **Python**: 3.8 or higher
- **AWS Account**: With appropriate IAM permissions
- **AWS CLI**: Configured with credentials
- **Boto3**: AWS SDK for Python

See `requirements.txt` for full dependency list.

---

## 🎯 Learning Goals

- [x] Master Python fundamentals
- [x] Learn AWS SDK (Boto3)
- [x] Build security automation scripts
- [x] Implement incident response automation
- [ ] Add CloudWatch monitoring
- [ ] Build a web dashboard with Flask
- [ ] Implement multi-account security scanning
- [ ] Add automated remediation

---

## 🔒 Security Considerations

**IAM Permissions Required:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:List*",
        "iam:Get*",
        "s3:List*",
        "s3:GetBucketPolicy",
        "ec2:Describe*",
        "kms:List*",
        "kms:GetKeyPolicy"
      ],
      "Resource": "*"
    }
  ]
}
```

**Best Practices:**
- Never commit AWS credentials to Git
- Use IAM roles instead of access keys when possible
- Enable CloudTrail for audit logging
- Review IAM policies regularly
- Use AWS Secrets Manager for sensitive data

---

## 📚 Resources

**Python Learning:**
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python for Everybody](https://www.py4e.com/)

**AWS & Boto3:**
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS Security Best Practices](https://aws.amazon.com/architecture/security-identity-compliance/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

**Security:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [AWS Security Hub](https://aws.amazon.com/security-hub/)
- [CIS AWS Foundations Benchmark](https://www.cisecurity.org/benchmark/amazon_web_services)

---

## 🤝 Contributing

This is a personal learning repository, but suggestions and feedback are welcome! Feel free to:

- Open an issue for bugs or suggestions
- Submit a pull request with improvements
- Share your own learning resources

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Master Coder**
- Role: AWS Cloud Support Engineer
- Focus: Cloud Security Automation
- GitHub: [@master-coder1998](https://github.com/master-coder1998)

---

## 🙏 Acknowledgments

- AWS documentation team for excellent Boto3 docs
- Python community for amazing learning resources
- Fellow AWS Cloud Support Engineers for inspiration

---

## 📈 Progress Tracker

| Topic | Status | Notes |
|-------|--------|-------|
| Python Basics | ✅ Complete | 10 core scripts |
| Boto3 Fundamentals | ✅ Complete | IAM, S3, EC2, KMS |
| Security Scripts | ✅ Complete | 8 audit scripts |
| Incident Response | ✅ Complete | Credential containment |
| Web Dashboard | 🚧 In Progress | Flask + Bootstrap |
| Multi-Account | 📋 Planned | AWS Organizations |

---

**Last Updated:** January 2026

⭐ If you find this repository helpful, consider giving it a star!
