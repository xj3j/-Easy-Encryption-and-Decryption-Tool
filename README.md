# Basic Encryption and Decryption Tool 🔒

## Overview
This tool provides a simple way to encrypt and decrypt messages using the Caesar Cipher technique. It’s a classic encryption method that shifts characters by a specified amount, allowing you to encode and decode messages easily!

## How It Works

### 1. Encryption Process
- **Input**: The user provides a message and a shift value (an integer between 1 and 25).
- **Output**: The tool shifts each letter in the message by the provided shift value to create an encrypted message.

### 2. Decryption Process
- **Input**: The user provides the encrypted message and the same shift value used during encryption.
- **Output**: The tool reverses the shift, converting the encrypted message back into the original message.

## Example Usage

### Encrypting a Message
- **User Input**: 
  - Message: `"Hello, World!"` 
  - Shift Value: `3`
- **Output**: `"Khoor, Zruog!"`

### Decrypting a Message
- **User Input**:
  - Encrypted Message: `"Khoor, Zruog!"`
  - Shift Value: `3`
- **Output**: `"Hello, World!"`

## How to Run
1. Clone the repository.
2. Run the script with your message and shift value.

```bash
# Example command to run the tool
python cryptoo.py
