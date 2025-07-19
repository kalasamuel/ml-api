# ML Discount Prediction API

This is a Flask-based API to serve a trained ML model predicting discounts.

## Endpoints

- `GET /` → health check
- `POST /predict`

### Sample POST body:
```json
{
  "stock": 30,
  "salesVelocity": 1.2,
  "daysToExpiry": 5,
  "category": "dairy"
}
