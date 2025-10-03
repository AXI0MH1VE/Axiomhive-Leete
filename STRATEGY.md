# Deployment and Usage Strategy

## Universal Hash Validator CLI

### Quick Start

```bash
# Make executable
chmod +x ARTIFACTS/hash_validator.py

# Calculate SHA256 (default)
python3 ARTIFACTS/hash_validator.py myfile.txt

# Calculate all hashes
python3 ARTIFACTS/hash_validator.py myfile.txt --all

# Verify a file
python3 ARTIFACTS/hash_validator.py myfile.txt --verify <hash> --algorithm sha256
```

### Installation Strategy

#### Option 1: Direct Usage (Recommended for Verification)
```bash
# Clone repository
git clone https://github.com/AXI0MH1VE/Axiomhive-Leete.git
cd Axiomhive-Leete

# Use directly (no installation needed)
python3 ARTIFACTS/hash_validator.py --help
```

#### Option 2: System-Wide Installation
```bash
# Create symlink in PATH
sudo ln -s $(pwd)/ARTIFACTS/hash_validator.py /usr/local/bin/hash-validator

# Now use from anywhere
hash-validator myfile.txt
```

#### Option 3: Virtual Environment (Development)
```bash
python3 -m venv venv
source venv/bin/activate
cd ARTIFACTS
python hash_validator.py --help
```

### Distribution Strategy

**Goal**: Maximize verifiability and minimize trust requirements

1. **GitHub as Source of Truth**
   - Repository tagged with version releases
   - Each release includes SHA256 hashes of all artifacts
   - Commit signatures for authenticity

2. **Multi-Channel Distribution**
   - Direct from GitHub (primary)
   - Mirror on personal website (backup)
   - Archive on Internet Archive (longevity)

3. **Verification Chain**
   ```
   User downloads hash_validator.py
     ↓
   Verifies against published hash
     ↓
   Uses tool to verify other files
     ↓
   Trust established through verification, not assumption
   ```

### Use Cases

#### 1. File Integrity Verification
```bash
# Download a file and its published hash
wget https://example.com/software.tar.gz
wget https://example.com/software.tar.gz.sha256

# Verify
python3 hash_validator.py software.tar.gz --verify $(cat software.tar.gz.sha256)
```

#### 2. Backup Verification
```bash
# Before backup
python3 hash_validator.py important_file.pdf --all > checksums.txt

# After restore
python3 hash_validator.py important_file.pdf --verify <hash>
```

#### 3. Build Artifact Verification (CI/CD)
```bash
# In CI pipeline
python3 hash_validator.py build/output.bin --sha256 > release/checksums.txt
```

#### 4. Multi-Algorithm Verification
```bash
# For critical files, verify with multiple algorithms
python3 hash_validator.py critical.data --all
# Manually cross-reference all hashes
```

### Deployment Checklist

- [ ] Repository cloned or files downloaded
- [ ] Python 3.7+ available
- [ ] hash_validator.py verified against known-good hash
- [ ] Test run completed successfully
- [ ] PATH configured (if using system-wide)
- [ ] Documentation reviewed

### Testing Strategy

```bash
# Test with a known file
echo "test content" > test.txt

# Calculate hash
python3 hash_validator.py test.txt --sha256

# Verify hash
python3 hash_validator.py test.txt --verify <calculated_hash>

# Should output: ✓ Hash verification PASSED
```

### Integration Patterns

#### Shell Script Integration
```bash
#!/bin/bash
FILE=$1
EXPECTED_HASH=$2

if python3 hash_validator.py "$FILE" --verify "$EXPECTED_HASH"; then
    echo "File verified, proceeding..."
    # Continue with operations
else
    echo "Verification failed, aborting!"
    exit 1
fi
```

#### Makefile Integration
```makefile
.PHONY: verify
verify:
	python3 ARTIFACTS/hash_validator.py build/artifact.bin --verify $(EXPECTED_HASH)
```

### Security Best Practices

1. **Always verify the validator first**
   - Get hash_validator.py hash from multiple independent sources
   - Compare with published hashes in repository

2. **Use multiple hash algorithms for critical verification**
   - Collision attacks become exponentially harder

3. **Store verification hashes separately**
   - Don't store checksums in same location as files

4. **Automate where possible**
   - Integrate into CI/CD pipelines
   - Use in backup scripts

### Troubleshooting

**Issue**: "File not found" error
- **Solution**: Check file path, use absolute paths if needed

**Issue**: "Cannot detect algorithm" error
- **Solution**: Hash length doesn't match known algorithms, specify explicitly

**Issue**: Permission denied
- **Solution**: Ensure file is readable, check permissions

**Issue**: Hash mismatch
- **Solution**: File may be corrupted or modified, re-download from source

---

*This strategy emphasizes verifiability and practical deployment patterns for maximum security and usability.*
