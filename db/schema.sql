-- Raw ingestion table
CREATE TABLE deliveries_raw (
    delivery_id TEXT,
    delivery_partner TEXT,
    package_type TEXT,
    vehicle_type TEXT,
    delivery_mode TEXT,
    region TEXT,
    weather_condition TEXT,
    distance_km TEXT,
    package_weight_kg TEXT,
    delivery_time_hours TEXT,
    expected_time_hours TEXT,
    delayed TEXT,
    delivery_status TEXT,
    delivery_rating TEXT,
    delivery_cost TEXT
);

-- Clean analytics table
CREATE TABLE deliveries (
    delivery_id INTEGER,
    delivery_partner VARCHAR(50),
    package_type VARCHAR(50),
    vehicle_type VARCHAR(50),
    delivery_mode VARCHAR(50),
    region VARCHAR(50),
    weather_condition VARCHAR(50),
    distance_km NUMERIC,
    package_weight_kg NUMERIC,
    delivery_time_hours NUMERIC,
    expected_time_hours NUMERIC,
    delayed BOOLEAN,
    delivery_status VARCHAR(50),
    delivery_rating NUMERIC,
    delivery_cost NUMERIC
);
