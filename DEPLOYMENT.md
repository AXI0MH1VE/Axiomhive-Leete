# Deployment Guide

## Universal Hash Validator CLI - Production Deployment

### Pre-Deployment Verification

Before deploying to production, verify the integrity of all artifacts:

```bash
# Clone repository
git clone https://github.com/AXI0MH1VE/Axiomhive-Leete.git
cd Axiomhive-Leete

# Verify commit signatures (if available)
git log --show-signature

# Check repository integrity
git fsck
```

### Deployment Environments

#### 1. Local Development

**Purpose**: Testing and development

```bash
# Direct usage
python3 ARTIFACTS/hash_validator.py --help

# Run tests
cd VALIDATION/ci
bash test_script.sh
```

#### 2. Server Deployment

**Purpose**: Production file verification server

```bash
# Install to /opt
sudo mkdir -p /opt/hash-validator
sudo cp -r ARTIFACTS /opt/hash-validator/
sudo chmod +x /opt/hash-validator/ARTIFACTS/hash_validator.py

# Create system-wide symlink
sudo ln -s /opt/hash-validator/ARTIFACTS/hash_validator.py /usr/local/bin/hash-validator

# Verify installation
hash-validator --help
```

#### 3. CI/CD Integration

**Purpose**: Automated build verification

**GitHub Actions Example:**

```yaml
name: Verify Build Artifacts

on:
  push:
    branches: [ main ]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Calculate artifact hashes
        run: |
          python3 ARTIFACTS/hash_validator.py build/output.bin --all > checksums.txt
          cat checksums.txt
      
      - name: Verify against known good hash
        run: |
          python3 ARTIFACTS/hash_validator.py build/output.bin --verify ${{ secrets.EXPECTED_HASH }}
```

**GitLab CI Example:**

```yaml
verify_artifacts:
  stage: test
  script:
    - python3 ARTIFACTS/hash_validator.py build/artifact.tar.gz --sha256
    - python3 ARTIFACTS/hash_validator.py build/artifact.tar.gz --verify $EXPECTED_HASH
  only:
    - main
```

#### 4. Docker Container

**Purpose**: Portable verification environment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY ARTIFACTS/ /app/

ENTRYPOINT ["python3", "hash_validator.py"]
CMD ["--help"]
```

**Build and use:**

```bash
# Build image
docker build -t hash-validator .

# Use container
docker run -v $(pwd):/data hash-validator /data/myfile.txt --sha256
```

### Production Checklist

- [ ] Python 3.7+ available in target environment
- [ ] Repository cloned from official source
- [ ] Commit signatures verified (if applicable)
- [ ] Test script executed successfully
- [ ] Tool verified against known good hash
- [ ] Documentation accessible to team
- [ ] Backup/rollback plan established

### Security Hardening

#### File Permissions

```bash
# Make hash_validator.py read-only
chmod 555 ARTIFACTS/hash_validator.py

# Prevent modifications
sudo chattr +i ARTIFACTS/hash_validator.py  # Linux
```

#### Integrity Monitoring

```bash
# Create baseline hash
python3 hash_validator.py ARTIFACTS/hash_validator.py --sha256 > validator.hash

# Periodic verification (add to cron)
*/30 * * * * python3 /opt/hash-validator/ARTIFACTS/hash_validator.py /opt/hash-validator/ARTIFACTS/hash_validator.py --verify $(cat /opt/hash-validator/validator.hash) || echo "ALERT: Validator integrity compromised!"
```

### Rollback Procedures

If issues are discovered post-deployment:

```bash
# Identify last known good commit
git log --oneline

# Checkout specific version
git checkout <commit-hash>

# Or revert to previous release
git checkout v1.0.0

# Verify rolled-back version
python3 ARTIFACTS/hash_validator.py --help
```

### Monitoring and Alerting

#### Basic Health Check

```bash
#!/bin/bash
# health_check.sh

if python3 /opt/hash-validator/ARTIFACTS/hash_validator.py --help &>/dev/null; then
    echo "OK: Hash validator operational"
    exit 0
else
    echo "CRITICAL: Hash validator failed health check"
    exit 2
fi
```

#### Usage Logging

```bash
# Wrapper script with logging
#!/bin/bash
LOGFILE="/var/log/hash-validator/usage.log"
echo "[$(date)] User: $USER, File: $1" >> "$LOGFILE"
python3 /opt/hash-validator/ARTIFACTS/hash_validator.py "$@"
```

### Multi-Environment Deployment

#### Development → Staging → Production

**Development:**
```bash
# Use latest from main branch
git pull origin main
```

**Staging:**
```bash
# Use tagged releases
git checkout tags/v1.0.0
# Test thoroughly
```

**Production:**
```bash
# Deploy only after staging validation
git checkout tags/v1.0.0
# Deploy with monitoring
```

### Backup Strategy

```bash
# Before deployment, create backup
sudo tar -czf /backup/hash-validator-$(date +%Y%m%d).tar.gz /opt/hash-validator/

# Retain last 10 backups
find /backup -name "hash-validator-*.tar.gz" -mtime +300 -delete
```

### Performance Considerations

- **Large files**: Tool uses streaming (8KB chunks), memory efficient
- **Concurrent usage**: Python GIL may limit, consider multiple processes
- **Disk I/O**: Performance depends on disk speed, not CPU

### Troubleshooting Production Issues

**Issue**: Import errors
- **Solution**: Ensure Python 3.7+ with hashlib in stdlib

**Issue**: Permission denied on files
- **Solution**: Check file ownership and read permissions

**Issue**: Tool not found in PATH
- **Solution**: Verify symlink exists and points to correct location

### Post-Deployment Validation

```bash
# Test basic functionality
echo "test" > /tmp/test.txt
hash-validator /tmp/test.txt --sha256

# Expected output:
# File: /tmp/test.txt
# SHA256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

# Verify against known hash
hash-validator /tmp/test.txt --verify 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
# Expected: ✓ Hash verification PASSED
```

---

## Maintenance

### Regular Updates

```bash
# Check for updates
git fetch origin
git log HEAD..origin/main --oneline

# Review changes
git diff HEAD origin/main

# Update if appropriate
git pull origin main
```

### Version Management

- Tag releases with semantic versioning
- Maintain changelog
- Document breaking changes

---

*This deployment guide ensures reliable, secure, and maintainable production deployments of the Universal Hash Validator CLI.*
