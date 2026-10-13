// Switch to telemetry database
use smart_home_telemetry;

// Drop collection if resetting
db.sensor_logs.drop();

// Insert Semi-Structured IoT Sensor Logs
db.sensor_logs.insertMany([
  {
    "device_id": "DEV_HVAC_01",
    "timestamp": ISODate("2026-10-08T08:00:00Z"),
    "readings": {
      "voltage_v": 230.4,
      "current_a": 15.2,
      "power_w": 3502.08,
      "energy_kwh": 1.7500
    },
    "environmental": {
      "ambient_temp_c": 24.5,
      "humidity_pct": 55.0
    },
    "network_health": {
      "rssi_dbm": -62,
      "firmware_version": "v2.4.1"
    }
  },
  {
    "device_id": "DEV_FRIDGE_01",
    "timestamp": ISODate("2026-10-08T08:00:00Z"),
    "readings": {
      "voltage_v": 231.1,
      "current_a": 1.08,
      "power_w": 249.58,
      "energy_kwh": 0.1250
    },
    "environmental": {
      "internal_temp_c": 3.8
    },
    "network_health": {
      "rssi_dbm": -70,
      "firmware_version": "v1.8.0"
    }
  },
  {
    "device_id": "DEV_WASH_01",
    "timestamp": ISODate("2026-10-08T10:00:00Z"),
    "readings": {
      "voltage_v": 228.9,
      "current_a": 5.24,
      "power_w": 1200.00,
      "energy_kwh": 0.6000
    },
    "environmental": {
      "water_flow_rate_lpm": 12.4
    },
    "network_health": {
      "rssi_dbm": -55,
      "firmware_version": "v3.0.2"
    }
  }
]);

// 1. Compound Index: device_id (ascending) + timestamp (descending)
db.sensor_logs.createIndex({ "device_id": 1, "timestamp": -1 }, { name: "idx_device_time" });

// 2. TTL Index: Automatic log expiration after 30 days (2592000 seconds)
db.sensor_logs.createIndex({ "timestamp": 1 }, { expireAfterSeconds: 2592000, name: "idx_ttl_30d" });

// 3. Query verification using index
db.sensor_logs.find({ "device_id": "DEV_HVAC_01" }).sort({ "timestamp": -1 });