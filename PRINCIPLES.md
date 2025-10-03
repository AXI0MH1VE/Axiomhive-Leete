# Project Principles

## Universal Hash Validator CLI

### Core Principles

#### 1. **Simplicity First**
- Minimize dependencies (use Python standard library)
- Clear, straightforward API
- Easy to understand, easy to verify

#### 2. **Verifiability**
- Every claim must be verifiable
- Transparent operations (no hidden behavior)
- Reproducible results across platforms

#### 3. **Security by Design**
- Support multiple hash algorithms (defense in depth)
- Fail securely (explicit error handling)
- No silent failures

#### 4. **Usability**
- Intuitive command-line interface
- Helpful error messages
- Sensible defaults

#### 5. **Maintainability**
- Clean, documented code
- Standard Python practices
- Minimal technical debt

### Design Philosophy

**Trust Through Transparency**: Users should be able to understand exactly what the tool does by reading the code. No magic, no surprises.

**Verification Over Convention**: Don't assume integrity—verify it. Every file's authenticity should be provable.

**Fail Fast, Fail Clear**: When something goes wrong, report it immediately with actionable information.

### Development Standards

- **Code Quality**: All code follows PEP 8 guidelines
- **Testing**: Core functionality must be testable
- **Documentation**: Every public function must have a docstring
- **Version Control**: Meaningful commit messages that explain "why"

### Security Considerations

1. **No External Network Calls**: Tool operates entirely offline
2. **Read-Only Operations**: Never modifies input files
3. **Explicit Permission**: Users must explicitly request verification
4. **Algorithm Diversity**: Support multiple hash standards for flexibility

---

*These principles guide all development decisions and should be referenced when evaluating new features or changes.*
