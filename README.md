# Invoice Parser & Extraction API

A robust FastAPI application designed for managing invoice documents and automatically extracting structured data using OCR and LLMs. This project provides a secure backend for uploading, storing, and analyzing invoices with advanced data extraction capabilities.

## 🚀 Features

*   **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
*   **File Management**:
    *   Upload invoices (PDF, PNG, JPG supported).
    *   Secure storage with **encryption at rest** using Fernet.
    *   List, retrieve (decrypted), and delete files.
*   **Intelligent Data Extraction**:
    *   **OCR Integration**: Uses Tesseract OCR to convert scanned documents and images into text.
    *   **LLM Parsing**: Leverages Google's Generative AI (Gemini) to intelligently parse unstructured OCR text into JSON.
    *   **Regex Fallback**: Includes robust regex-based extraction as a backup if LLM parsing fails.
*   **Database**: PostgreSQL integration via SQLAlchemy for persistent storage of user data, file metadata, and extraction results.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3.8+**
*   **PostgreSQL**: A running instance of PostgreSQL.
*   **Tesseract OCR**:
    *   **Windows**: [Download Installer](https://github.com/UB-Mannheim/tesseract/wiki)
    *   **Linux**: `sudo apt-get install tesseract-ocr`
    *   **macOS**: `brew install tesseract`

## 📦 Installation

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd Invoice_Parser_llm
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Configuration**
    Create a `.env` file in the root directory and configure the following variables:

    ```env
    # Security
    JWT_KEY=your_super_secret_jwt_key

    # Database
    DATABASE_URL=postgresql://user:password@localhost:5432/invoice_db

    # AI & OCR
    GOOGLE_API_KEY=your_google_gemini_api_key
    TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe  # Adjust path based on your installation

    # Optional
    LOCAL_STORAGE_DIR=invoices_data
    ```

## 🏃‍♂️ Running the Application

1.  **Initialize the Database**
    Ensure your PostgreSQL server is running and the database exists. The application will automatically create tables on startup, but you can also run:
    ```bash
    python init_db.py
    ```

2.  **Start the Server**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation:

*   **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
*   **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📂 Project Structure

```
Invoice_Parser_llm/
├── auth/               # Authentication logic and JWT handling
├── db/                 # Database models, connection, and CRUD operations
│   ├── database.py     # Database session setup
│   ├── table_models.py # SQLAlchemy models (User, File, ExtractedFile)
│   ├── extracted.py    # Logic for OCR and LLM extraction
│   └── ...
├── models/             # Pydantic models for request/response validation
├── routers/            # API Endpoints
│   ├── users.py        # Auth & User routes
│   ├── files.py        # File upload & management routes
│   └── extracted.py    # Extraction trigger routes
├── config.py           # Environment variable configuration
├── main.py             # Application entry point
├── init_db.py          # Script to initialize database tables
└── requirements.txt    # Python dependencies
```

## 🔒 Security Note

*   Files saved to the disk are **encrypted** using a key derived from the user's credentials. This ensures that even if storage is compromised, the raw invoice files remain secure.
*   Ensure `JWT_KEY` is kept secret and processed files in `tmp/` are cleaned up (handled automatically by the application).

## 🤝 Contributing

1.  Fork the repository.
2.  Create a new feature branch.
3.  Commit your changes.
4.  Push to the branch.
5.  Open a Pull Request.
