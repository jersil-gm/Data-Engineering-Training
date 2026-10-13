use expense_monitoring_db;

// Clean collection
db.scanned_receipts.drop();

// Store user notes or scanned receipts as JSON
db.scanned_receipts.insertMany([
  {
    receipt_id: "RCPT-2026-001",
    user_id: 1,
    expense_id: 101,
    merchant_name: "Fresh Mart Supermarket",
    receipt_date: ISODate("2026-01-05T14:30:00Z"),
    total_amount: 125.50,
    user_notes: "Weekly supermarket run for groceries and household essentials.",
    scanned_data: {
      ocr_status: "SUCCESS",
      confidence: 0.96,
      items: [
        { name: "Organic apples", price: 15.50 },
        { name: "Almond milk", price: 10.00 },
        { name: "Whole grain bread", price: 100.00 }
      ]
    }
  },
  {
    receipt_id: "RCPT-2026-002",
    user_id: 1,
    expense_id: 102,
    merchant_name: "City Power Supply",
    receipt_date: ISODate("2026-01-12T09:15:00Z"),
    total_amount: 85.00,
    user_notes: "Electricity utility bill paid via online portal.",
    scanned_data: {
      ocr_status: "SUCCESS",
      confidence: 0.99,
      items: [
        { name: "Residential Electricity 250 kWh", price: 85.00 }
      ]
    }
  },
  {
    receipt_id: "RCPT-2026-003",
    user_id: 2,
    expense_id: 105,
    merchant_name: "Skyline Properties",
    receipt_date: ISODate("2026-01-28T18:00:00Z"),
    total_amount: 1200.00,
    user_notes: "January house rent wire transfer receipt.",
    scanned_data: {
      ocr_status: "SUCCESS",
      confidence: 0.98,
      items: [
        { name: "Apartment Monthly Rent", price: 1200.00 }
      ]
    }
  }
]);

// Add indexing for quick user and receipt lookup
db.scanned_receipts.createIndex({ user_id: 1 });
db.scanned_receipts.createIndex({ receipt_id: 1 }, { unique: true });
db.scanned_receipts.createIndex({ user_id: 1, receipt_date: -1 });

// Verification queries
print("Configured Indexes:");
printjson(db.scanned_receipts.getIndexes());

print("Lookup by user_id:");
printjson(db.scanned_receipts.find({ user_id: 1 }).toArray());