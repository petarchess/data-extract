# Receipt OCR Service: Technical Documentation & Guide

## Part I: Project Vision
The Receipt OCR Service is a specialized document intelligence tool designed to transform unstructured images of receipts into structured, machine-readable JSON data. Unlike traditional OCR that reads line-by-line, this service uses the **Document Understanding Transformer (Donut)** model to understand the visual hierarchy and layout of financial documents.

This service acts as a high-performance backend for **Oracle APEX** applications, enabling automated expense reporting and data extraction.

### Problem & Solution
*   **The Problem**: Manual data entry of receipts is slow, prone to human error, and creates a visibility gap in financial tracking.
*   **The Solution**: A "Snap and Confirm" workflow where the AI extracts metadata (Merchant, Date, PIB, Total) and the user simply validates the result.

---

## Part II: Getting Started

### 1. Prerequisites
*   Python 3.8 or higher.
*   CUDA-enabled GPU (optional but recommended for performance).
*   OpenSSL (for generating security certificates).

### 2. Installation & Setup

#### Clone the repository
```bash
git clone [https://github.com/petarchess/data-extract.git](https://github.com/petarchess/data-extract.git)
cd receipt-ocr-service
Set up a virtual environment
Bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Linux/macOS:
source venv/bin/activate
Install dependencies
Bash
pip install fastapi uvicorn transformers torch Pillow python-multipart
Generate SSL Certificates
To enable HTTPS for secure communication with Oracle APEX:

Bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -nodes
Part III: Usage
Running the Service
Launch the FastAPI server using Uvicorn with the generated SSL certificates:

Bash
uvicorn main:app --host 0.0.0.0 --port 8000 --ssl-keyfile ./key.pem --ssl-certfile ./cert.pem
API Endpoint
Endpoint: POST /extract

Request Type: multipart/form-data

Payload: file (Image of the receipt)

Example Response
JSON
{
  "store_name": "Example Market",
  "date": "2026-05-03",
  "pib": "123456789",
  "total_amount": "1500.00",
  "currency": "RSD"
}
Part IV: Integration with Oracle APEX
REST Data Source: Configure a REST Data Source in APEX pointing to your hosted HTTPS URL.

Payload: Pass the receipt image as a BLOB in the body of the POST request.

Parsing: Use the JSON_TABLE function in SQL to parse the returned attributes directly into your application tables.

License
MIT License
