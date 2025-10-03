#!/usr/bin/env python3
"""
Universal Hash Validator CLI
Verifies file integrity across multiple hash algorithms (MD5, SHA1, SHA256, SHA512)
"""

import hashlib
import sys
import argparse
from pathlib import Path


class HashValidator:
    """Validates file integrity using multiple hash algorithms"""
    
    SUPPORTED_ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512']
    
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
    
    def calculate_hash(self, algorithm):
        """Calculate hash for the file using specified algorithm"""
        if algorithm not in self.SUPPORTED_ALGORITHMS:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        hash_obj = hashlib.new(algorithm)
        
        with open(self.filepath, 'rb') as f:
            # Read file in chunks to handle large files efficiently
            for chunk in iter(lambda: f.read(8192), b''):
                hash_obj.update(chunk)
        
        return hash_obj.hexdigest()
    
    def calculate_all_hashes(self):
        """Calculate all supported hashes for the file"""
        results = {}
        for algorithm in self.SUPPORTED_ALGORITHMS:
            results[algorithm] = self.calculate_hash(algorithm)
        return results
    
    def verify_hash(self, expected_hash, algorithm=None):
        """Verify if expected hash matches calculated hash"""
        # Auto-detect algorithm if not specified
        if algorithm is None:
            algorithm = self._detect_algorithm(expected_hash)
        
        calculated = self.calculate_hash(algorithm)
        return calculated.lower() == expected_hash.lower()
    
    def _detect_algorithm(self, hash_string):
        """Detect hash algorithm based on hash length"""
        hash_length = len(hash_string)
        length_map = {
            32: 'md5',
            40: 'sha1',
            64: 'sha256',
            128: 'sha512'
        }
        
        if hash_length not in length_map:
            raise ValueError(f"Cannot detect algorithm from hash length: {hash_length}")
        
        return length_map[hash_length]


def main():
    parser = argparse.ArgumentParser(
        description='Universal Hash Validator - Verify file integrity using multiple hash algorithms',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s file.txt --all
  %(prog)s file.txt --verify abc123... --algorithm sha256
  %(prog)s file.txt --sha256
        """
    )
    
    parser.add_argument('file', help='File to validate')
    parser.add_argument('--all', action='store_true', help='Calculate all supported hashes')
    parser.add_argument('--md5', action='store_true', help='Calculate MD5 hash')
    parser.add_argument('--sha1', action='store_true', help='Calculate SHA1 hash')
    parser.add_argument('--sha256', action='store_true', help='Calculate SHA256 hash')
    parser.add_argument('--sha512', action='store_true', help='Calculate SHA512 hash')
    parser.add_argument('--verify', metavar='HASH', help='Verify against expected hash')
    parser.add_argument('--algorithm', choices=HashValidator.SUPPORTED_ALGORITHMS,
                        help='Specify algorithm for verification (auto-detected if not provided)')
    
    args = parser.parse_args()
    
    try:
        validator = HashValidator(args.file)
        
        # Verification mode
        if args.verify:
            algorithm = args.algorithm
            is_valid = validator.verify_hash(args.verify, algorithm)
            
            if is_valid:
                print(f"✓ Hash verification PASSED")
                print(f"  File: {args.file}")
                print(f"  Algorithm: {algorithm or 'auto-detected'}")
                sys.exit(0)
            else:
                print(f"✗ Hash verification FAILED")
                print(f"  File: {args.file}")
                print(f"  Expected: {args.verify}")
                calculated = validator.calculate_hash(algorithm or validator._detect_algorithm(args.verify))
                print(f"  Calculated: {calculated}")
                sys.exit(1)
        
        # Calculate mode
        results = {}
        
        if args.all:
            results = validator.calculate_all_hashes()
        else:
            # Check individual algorithm flags
            if args.md5:
                results['md5'] = validator.calculate_hash('md5')
            if args.sha1:
                results['sha1'] = validator.calculate_hash('sha1')
            if args.sha256:
                results['sha256'] = validator.calculate_hash('sha256')
            if args.sha512:
                results['sha512'] = validator.calculate_hash('sha512')
            
            # Default to SHA256 if no specific algorithm selected
            if not results:
                results['sha256'] = validator.calculate_hash('sha256')
        
        # Output results
        print(f"File: {args.file}")
        for algorithm, hash_value in results.items():
            print(f"{algorithm.upper()}: {hash_value}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
