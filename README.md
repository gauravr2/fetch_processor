## How to Run the Project

1. Navigate to the project directory:
   ```bash
   cd /path/to/fetch_processor
   ```

2. Build the Docker image:
   ```bash
   docker build -t receipt_processor .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 8080:8080 receipt_processor
   ```

---

## Example Use Case

### Process a Receipt
Use the following `curl` command to process a receipt:
```bash
curl -X POST http://localhost:8080/receipts/process \
-H "Content-Type: application/json" \
-d '{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    { "shortDescription": "Mountain Dew 12PK", "price": "6.49" }
  ],
  "total": "6.49"
}'
```

### Retrieve Receipt Points
Replace `<receipt_id>` with the ID of the receipt to get the associated points:
```bash
curl http://localhost:8080/receipts/<receipt_id>/points
```
