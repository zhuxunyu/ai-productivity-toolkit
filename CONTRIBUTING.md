# Contributing to AI Productivity Toolkit

First off, thank you for considering contributing to AI Productivity Toolkit! It's people like you that make this toolkit such a great tool for the community.

## 🎯 Our Principles

When contributing, please keep these principles in mind:

1. **Usability** - Make it easy to use
2. **Security** - Never compromise on security
3. **Innovation** - Bring fresh ideas
4. **Practicality** - Solve real problems
5. **Aesthetics** - Make it beautiful
6. **Attraction** - Make it engaging

## 📋 Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to zhuxunyu98@gmail.com.

## 🚀 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed and what behavior you expected**
* **Include screenshots if possible**
* **Include environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Explain why this enhancement would be useful**
* **List some examples of how this enhancement would be used**

### Pull Requests

* Fill in the required template
* Follow the Python style guide (PEP 8)
* Include tests for new features
* Update documentation as needed
* Ensure all tests pass

## 💻 Development Setup

### Prerequisites

- Python 3.8+
- pip
- git

### Setting Up Your Local Environment

```bash
# Fork the repository
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-productivity-toolkit.git
cd ai-productivity-toolkit

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development

# Run tests
pytest
```

## 📝 Style Guidelines

### Python Code Style

- Follow [PEP 8](https://pep8.org/)
- Use type hints where possible
- Write docstrings for public functions and classes
- Keep functions small and focused
- Use meaningful variable names

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(prompt): add auto-optimization for writing tasks

- Implement writing-specific optimization rules
- Add examples for writing prompts
- Update documentation

Closes #123
```

## 🔒 Security Guidelines

**IMPORTANT**: Security is our top priority!

- **NEVER** commit API keys, passwords, or secrets
- **ALWAYS** use environment variables for sensitive data
- **ALWAYS** add new sensitive files to `.gitignore`
- Review dependencies for known vulnerabilities
- Report security issues privately via email (see SECURITY.md)

## 🧪 Testing

We strive for high test coverage. When contributing:

- Write tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage
- Include both unit tests and integration tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=toolkit --cov-report=html

# Run specific test file
pytest tests/test_prompt_optimizer.py
```

## 📚 Documentation

Good documentation is crucial. When contributing:

- Update README.md if you change functionality
- Add docstrings to new functions/classes
- Update examples if you change APIs
- Write clear commit messages

## 🎨 Design Principles

When designing new features:

1. **Simple** - Easy to understand and use
2. **Consistent** - Follow existing patterns
3. **Documented** - Clear usage examples
4. **Tested** - Comprehensive test coverage
5. **Secure** - No security compromises

## 🏷️ Issue Labels

We use the following labels to organize issues:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Documentation improvements
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `question` - Further information needed
- `security` - Security-related issues
- `triage` - Needs review

## 💬 Questions?

Feel free to open an issue for questions, or contact us at zhuxunyu98@gmail.com.

## 🙏 Thank You!

Every contribution, no matter how small, makes a difference. We appreciate your help in making AI Productivity Toolkit better for everyone!

---

**Inspired by**: [Atom Contributing Guide](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)

**Last Updated**: March 7, 2026
