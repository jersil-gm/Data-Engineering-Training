-- Database Initialization
CREATE DATABASE IF NOT EXISTS smart_home_energy;
USE smart_home_energy;

-- 1. Rooms Table
CREATE TABLE IF NOT EXISTS rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(50) NOT NULL,
    floor INT DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Devices Table
CREATE TABLE IF NOT EXISTS devices (
    device_id VARCHAR(50) PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    room_id INT NOT NULL,
    device_type VARCHAR(50) NOT NULL,
    status ENUM('ONLINE', 'OFFLINE', 'STANDBY') DEFAULT 'ONLINE',
    rated_wattage DECIMAL(8, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
);

-- 3. Energy Logs Table
CREATE TABLE IF NOT EXISTS energy_logs (
    log_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    timestamp DATETIME NOT NULL,
    energy_kwh DECIMAL(10, 4) NOT NULL,
    voltage DECIMAL(6, 2),
    power_factor DECIMAL(3, 2) DEFAULT 1.00,
    FOREIGN KEY (device_id) REFERENCES devices(device_id) ON DELETE CASCADE,
    INDEX idx_device_time (device_id, timestamp)
);


-- CRUD Operations

-- CREATE: Rooms
INSERT INTO rooms (room_name, floor) VALUES 
('Living Room', 1),
('Kitchen', 1),
('Master Bedroom', 2);

-- CREATE: Devices
INSERT INTO devices (device_id, device_name, room_id, device_type, status, rated_wattage) VALUES 
('DEV_HVAC_01', 'Central AC', 1, 'HVAC', 'ONLINE', 3500.00),
('DEV_FRIDGE_01', 'Smart Refrigerator', 2, 'Refrigeration', 'ONLINE', 250.00),
('DEV_WASH_01', 'Washing Machine', 2, 'Laundry', 'STANDBY', 1200.00),
('DEV_HEATER_01', 'Space Heater', 3, 'Heating', 'ONLINE', 1500.00);

-- CREATE: Energy Logs
INSERT INTO energy_logs (device_id, timestamp, energy_kwh, voltage, power_factor) VALUES
('DEV_HVAC_01', '2026-10-08 08:00:00', 1.7500, 230.1, 0.95),
('DEV_HVAC_01', '2026-10-08 12:00:00', 2.1000, 229.8, 0.96),
('DEV_FRIDGE_01', '2026-10-08 08:00:00', 0.1250, 230.5, 0.98),
('DEV_FRIDGE_01', '2026-10-08 12:00:00', 0.1300, 230.2, 0.98),
('DEV_WASH_01', '2026-10-08 10:00:00', 0.6000, 228.9, 0.91),
('DEV_HEATER_01', '2026-10-08 06:00:00', 1.2000, 231.0, 0.99);

-- READ: Retrieve online devices mapped to room names
SELECT d.device_id, d.device_name, r.room_name, d.status, d.rated_wattage
FROM devices d
JOIN rooms r ON d.room_id = r.room_id
WHERE d.status = 'ONLINE';

-- UPDATE: Modify device operating status
UPDATE devices SET status = 'STANDBY' WHERE device_id = 'DEV_HVAC_01';

-- DELETE: Sample cleanup for logs older than a threshold
DELETE FROM energy_logs WHERE timestamp < '2026-01-01 00:00:00';


-- Stored Procedure: Room Daily Energy Usage

DELIMITER $$

DROP PROCEDURE IF EXISTS GetRoomDailyEnergyUsage$$

CREATE PROCEDURE GetRoomDailyEnergyUsage(
    IN target_date DATE
)
BEGIN
    SELECT 
        r.room_id,
        r.room_name,
        DATE(el.timestamp) AS usage_date,
        COUNT(DISTINCT el.device_id) AS active_devices_count,
        ROUND(SUM(el.energy_kwh), 4) AS total_energy_kwh,
        ROUND(AVG(el.energy_kwh), 4) AS avg_reading_kwh
    FROM rooms r
    JOIN devices d ON r.room_id = d.room_id
    JOIN energy_logs el ON d.device_id = el.device_id
    WHERE DATE(el.timestamp) = target_date
    GROUP BY r.room_id, r.room_name, DATE(el.timestamp)
    ORDER BY total_energy_kwh DESC;
END$$

DELIMITER ;