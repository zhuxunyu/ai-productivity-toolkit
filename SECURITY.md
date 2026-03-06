# Security Policy

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of AI Productivity Toolkit seriously. If you believe you've found a security vulnerability, please follow these steps:

### How to Report

1. **DO NOT** create a public GitHub issue for security vulnerabilities
2. Email your findings to: **zhuxunyu98@gmail.com**
3. Include "Security Vulnerability" in the subject line
4. Provide detailed information about the vulnerability:
   - Type of vulnerability
   - Full paths of affected source files
   - Step-by-step reproduction instructions
   - Potential impact

### What to Expect

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Resolution Timeline**: Depends on severity (critical issues prioritized)

### Security Best Practices We Follow

- ✅ No hardcoded API keys or secrets in source code
- ✅ Environment variable configuration for sensitive data
- ✅ `.env` files excluded from version control
- ✅ Regular dependency updates and security patches
- ✅ Code review for all contributions
- ✅ Automated security scanning in CI/CD

### User Responsibilities

When using this toolkit, please follow these security best practices:

1. **Never commit `.env` files** to version control
2. **Use environment variables** for API keys and secrets
3. **Keep dependencies updated** (`pip install --upgrade`)
4. **Review code** before running in production
5. **Use secure networks** when making API calls
6. **Rotate API keys** regularly

### Security Updates

Security updates will be released as patch versions (e.g., 1.0.1, 1.0.2). We recommend:

- Subscribing to release notifications
- Updating to the latest version promptly
- Reviewing CHANGELOG.md for security-related updates

## Acknowledgments

We appreciate responsible disclosure and will acknowledge security researchers who help improve our security (with permission).

---

**Last Updated**: March 7, 2026
