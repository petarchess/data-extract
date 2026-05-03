# Receipt OCR Service

## Project Overview
The Receipt OCR Service is a specialized document intelligence tool designed to transform unstructured images of receipts into structured, machine-readable JSON data. Unlike traditional OCR that reads line-by-line, this service uses the **Document Understanding Transformer (Donut)** model to understand the visual hierarchy and layout of financial documents.

This service is built to act as a high-performance backend for **Oracle APEX** applications, enabling automated expense reporting and data extraction.

## Key Features
*   **OCR-Free Extraction**: Uses the Donut model to map pixels directly to structured data.
*   **Visual Understanding**: Identifies Merchant Name, Date, Tax ID (PIB), and Total Amount based on visual context.
*   **GPU Accelerated**: Optimized for CUDA-enabled systems for near-instant processing.
*   **Secure API**: Built with FastAPI and HTTPS/SSL support for secure data transmission.
*   **Developer Friendly**: Automatically generated Swagger documentation for easy integration.

## Technical Stack
*   **Language**: Python 3.8+
*   **Framework**: FastAPI
*   **AI Model**: `naver-clova-ix/donut-base-finetuned-cord-v2`
*   **Machine Learning**: PyTorch, Hugging Face Transformers
*   **Image Processing**: Pillow (PIL)

## Getting Started

### Prerequisites
*   Python 3.8 or higher.
*   CUDA-enabled GPU (optional but highly recommended).
*   OpenSSL (for generating security certificates).

### Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/petarchess/data-extract.git](https://github.com/petarchess/data-extract.git)
   cd receipt-ocr-service
