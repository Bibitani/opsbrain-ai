## Database Setup (OpsBrain AI)

1. Install PostgreSQL
2. Create database:
   CREATE DATABASE opsbrain_db;

3. Connect to opsbrain_db
4. Run schema.sql to create tables
5. Download Kaggle dataset:
   Delivery Logistics Dataset (India – Multi-Partner)

6. Import CSV using psql:
   \copy deliveries_raw FROM 'path/to/Delivery_logistics.csv' CSV HEADER;

7. Transform data into deliveries table
