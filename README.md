# AXIOMHIVE-LEETE
## Universal Hash Validator CLI

**Production-grade file integrity verification with zero AI dependencies.**

---

### CREATORS

**Alexis Adams**  
X (Twitter): [@DevdollzAi](https://x.com/DevdollzAi)

**Eric Adams**  
Brand Platform: [AxiomHive](https://axiomhive.com)

---

## PROJECT PURPOSE

Axiomhive-Leete is a **portable, deterministic hash validation tool** designed for:

- **Universal File Integrity** — Generate and verify MD5, SHA-256, and SHA-512 hashes for any file type
- **Production Reliability** — Streaming architecture handles files of any size without memory overflow
- **Zero External Dependencies** — Pure Python 3 implementation with no AI, cloud services, or frameworks
- **Audit-Ready Operations** — Deterministic exit codes and structured logging for CI/CD integration

---

## ARCHITECTURAL DISCIPLINE

### Core Engineering Principles

- **Streaming File Processing** — Memory-efficient chunked I/O prevents system resource exhaustion
- **Deterministic Exit Codes**
  - `0` Success (validation passed or hash generated)
  - `1` Validation failure (hash mismatch detected)
  - `2` Runtime error (file not found, permission denied, etc.)
- **Automated Test Coverage** — 15+ test scenarios including edge cases (empty files, large binaries, concurrent operations)
- **Security First** — No command execution, no network calls, no filesystem traversal beyond specified files

### Quality Assurance

- **Continuous Integration** — Automated test suite validates every commit
- **Known Test Vectors** — Verifies against NIST cryptographic standards
- **Cross-Platform Validation** — Linux, macOS, Windows compatibility
- **Production Monitoring** — Exit code propagation enables automated alerting

---

## PROFESSIONAL VALUE

> **For Collaborators**
>
> - Clean, maintainable codebase demonstrates software engineering best practices
> - Comprehensive documentation enables immediate onboarding
> - Test-driven development workflow supports safe contributions

> **For Recruiters**
>
> - Showcases production-ready code architecture (not prototype/demo quality)
> - Demonstrates security consciousness and resource management
> - Exhibits CI/CD integration expertise and operational thinking
> - Proves ability to ship complete, deployable software solutions

---

## QUICKSTART GUIDE

### Prerequisites

```bash
# Requires Python 3.6+ (no additional packages needed)
python3 --version
```

### Installation

```bash
# Clone repository
git clone https://github.com/AXI0MH1VE/Axiomhive-Leete.git
cd Axiomhive-Leete

# Make validator executable (Linux/macOS)
chmod +x ARTIFACTS/hashval.py
```

### Basic Usage

#### Generate Hash

```bash
# Single algorithm
python3 ARTIFACTS/hashval.py myfile.txt --sha256

# Multiple algorithms
python3 ARTIFACTS/hashval.py myfile.txt --md5 --sha256 --sha512
```

#### Verify Hash

```bash
# Verify file integrity
python3 ARTIFACTS/hashval.py myfile.txt --verify <expected_hash>

# Example with SHA-256
python3 ARTIFACTS/hashval.py document.pdf --verify 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

### Validation Flow

```
┌──────────────┐
│ Input File   │
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│ Streaming Hash Engine   │  ← Memory-efficient chunking
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Hash Comparison          │  ← Constant-time comparison
│ (if --verify flag set)   │
└──────┬───────────────────┘
       │
       ▼
┌──────────────────────────┐
│ Exit Code + Output       │  ← Deterministic result
└──────────────────────────┘
```

---

## COMPLETE COMMAND REFERENCE

```bash
# Display help
python3 ARTIFACTS/hashval.py --help

# Supported flags:
#   --md5       Generate MD5 hash
#   --sha256    Generate SHA-256 hash
#   --sha512    Generate SHA-512 hash
#   --verify    Verify file against expected hash
```

---

## RUNNING TESTS

```bash
# Execute full test suite
cd VALIDATION/ci
./test_script.sh

# Expected output:
# ===================================================
# Test Summary
# ===================================================
# Total tests:  15
# Passed:       15
# Failed:       0
# ===================================================
# ✓ All tests passed!
```

---

## REPOSITORY STRUCTURE

```
Axiomhive-Leete/
├── ARTIFACTS/
│   └── hashval.py          # Core validator implementation
├── VALIDATION/
│   └── ci/
│       └── test_script.sh  # Automated test suite
├── DEPLOYMENT.md           # Production deployment guide
├── PRINCIPLES.md           # Engineering philosophy
├── STRATEGY.md             # Development roadmap
└── LICENSE                 # MIT License
```

---

## SECURITY CONSIDERATIONS

- **No Command Injection** — All inputs validated before processing
- **Path Traversal Protection** — File access restricted to explicit arguments
- **Constant-Time Comparison** — Prevents timing-based hash extraction attacks
- **No Network Operations** — Fully offline with no telemetry or external calls

---

## LICENSE

MIT License — See [LICENSE](LICENSE) for details.

---

## CONTRIBUTING

Contributions welcome. Please:

1. Review [PRINCIPLES.md](PRINCIPLES.md) for coding standards
2. Run test suite before submitting PRs
3. Maintain deterministic exit code contract
4. Add test coverage for new features

---

## CONTACT & SUPPORT

### Creators

**Alexis Adams**  
X (Twitter): [@DevdollzAi](https://x.com/DevdollzAi)

**Eric Adams**  
AxiomHive (brand platform)

### Project Resources

- **Issues** — [GitHub Issues](https://github.com/AXI0MH1VE/Axiomhive-Leete/issues)
- **Strategy** — See [STRATEGY.md](STRATEGY.md) for roadmap
- **Deployment** — See [DEPLOYMENT.md](DEPLOYMENT.md) for production setup

---

## ABOUT

### Authors/Operators

**Alexis Adams**

**Eric Adams**

Axiomhive-Leete is developed and maintained by **Alexis Adams** and **Eric Adams** as part of the AxiomHive engineering initiative. For professional inquiries and collaboration opportunities, reach out via [@DevdollzAi](https://x.com/DevdollzAi) or through AxiomHive brand platforms.

---

**Built with engineering discipline. Ready for production deployment.**
