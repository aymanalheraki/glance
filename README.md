### **Setup Instructions**

1️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

2️⃣ Run the application:

```bash
uvicorn main:app --reload
```

3️⃣ API Endpoints:

- **Shorten URL:** `POST /shorten`
- **Redirect URL:** `GET /<short_code>`