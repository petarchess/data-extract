# Receipt OCR Service: Strategic Documentation

## Part I: The Vision – Problem, Strategy, and Business Impact

### 1. Introduction: The Digital Transformation of Physical Proof
The **Receipt OCR Service** (internally known as the `data-extract` project) is not just a software utility; it is a strategic bridge between the chaotic physical world and the structured digital enterprise. In an era where data is a primary asset, most companies are still losing efficiency through paper-based workflows. 

Every year, businesses lose thousands of man-hours to a process that hasn't fundamentally changed in decades: moving numbers from a small slip of thermal paper into a database. This project implements a **Document Understanding Transformer (Donut)** to solve this, moving beyond simple character recognition into the realm of visual document intelligence.

### 2. The Problem: The "Administrative Tax" on Talent
The core problem this project addresses is the hidden cost of manual data entry, categorized into three main pain points:

*   **The Productivity Leak:** When a senior developer or a high-level consultant spends time typing invoice numbers into a system, the company is effectively paying developer rates for clerical work. Over a month, across a whole team, this adds up to hundreds of lost billable hours.
*   **The Fragility of Manual Data:** Human fingers are imperfect. A misplaced decimal point on an expense report (typing 1500 instead of 15.00) can trigger a chain reaction of errors, leading to incorrect tax filings, budget overruns, and audit failures.
*   **The Visibility Gap:** In a traditional system, a receipt sits in a wallet for weeks before it is uploaded. Management lacks a real-time view of project spending, making financial forecasting a guessing game.

### 3. The Solution: Reimagining the Workflow
The Receipt OCR Service introduces a "Capture-First" philosophy. Instead of waiting for the end of the month, the process starts the second the transaction happens.

*   **Immediate Digitization:** By using a smartphone camera as the primary input device, the service captures the context of the expense immediately.
*   **The AI as the First Reader:** Instead of a human reading the receipt, the Donut AI model acts as the initial auditor. It identifies the merchant, the date, and the tax details instantly.
*   **Validation Over Entry:** We transform the user experience. The user no longer creates the record; they simply approve the AI’s work. This shifts the mental burden from active production to passive verification.

---

## Part II: The Technical Build – Architecture, AI, and Integration

### 1. The Engine: Why "Donut" Beats Traditional OCR
Historically, developers used Tesseract. While Tesseract is a great tool for character recognition, it is poor at document understanding. It has no idea what a receipt is and requires fragile code to guess where the data is.

**The Donut Advantage:**
We utilize the `naver-clova-ix/donut-base-finetuned-cord-v2` model. This is an **End-to-End Transformer**:
*   **Visual Encoder:** It uses a Swin Transformer to see the image as a whole, noticing the structure, the bold text, and the lines.
*   **Text Decoder:** It uses a BART-like decoder to generate a JSON response directly from pixels.
*   **Robustness:** Because it maps pixels directly to meaning, it is much more robust against wrinkled receipts, low light, or tilted photos.

### 2. The Tech Stack: Modular and Modern
The project is built using a microservices mindset, ensuring that the AI logic is independent of the frontend.

*   **Python:** The language of choice due to its native support for PyTorch and the Hugging Face Transformers library.
*   **FastAPI:** Chosen over Flask for its asynchronous support, high performance, and automatic Swagger documentation generation.

### 3. The Pipeline: The Journey of a Receipt
When a file is sent to the `/extract` endpoint, it goes through a sophisticated lifecycle:

1.  **Image Pre-processing:** Using the Pillow library, the raw image is normalized, resized, and converted to RGB color space.
2.  **Tensor Conversion:** The `DonutProcessor` converts pixels into Tensors, which are moved to the **GPU (CUDA)** for sub-second extraction times.
3.  **Generative Extraction:** The model generates a sequence of text based on the visual cues in the receipt.
4.  **Post-Processing:** Regular Expressions (Regex) are used to strip special tokens and format the output into a valid JSON structure.

### 4. Security and Enterprise Integration
A project handling financial receipts must be secure.

*   **HTTPS and Encryption:** We implement SSL/TLS encryption using `.pem` certificates, ensuring the image data is encrypted during transmission.
*   **Oracle APEX Handshake:** The final piece is the REST handshake. APEX posts the image, and the Python service returns a JSON object. APEX then uses `JSON_TABLE` to instantly turn that output into a row in an Oracle table.

### 5. Conclusion: Scalability and the Future
The current build is the foundation. Because we are using a Transformer-based model, the system can eventually be fine-tuned on specific regional receipts to increase accuracy further. This project is an evolving AI asset that grows more intelligent over time, making manual data entry a distant memory.
