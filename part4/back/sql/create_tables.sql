-- create_tables.sql

-- suppress if existing, to be removed!!!

DROP TABLE IF EXISTS places;


-- Users table
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Amenities table
CREATE TABLE IF NOT EXISTS amenities (
    id TEXT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Places table
CREATE TABLE IF NOT EXISTS places (
    id TEXT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(5000),
    image_path VARCHAR(255),
    price REAL NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    owner_id TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(owner_id) REFERENCES users(id)
);

-- Reviews table
CREATE TABLE IF NOT EXISTS reviews (
    id TEXT PRIMARY KEY,
    text VARCHAR(5000) NOT NULL,
    rating INTEGER NOT NULL,
    place_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

-- Place_Amenity association table
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id TEXT NOT NULL,
    amenity_id TEXT NOT NULL,
    PRIMARY KEY(place_id, amenity_id),
    FOREIGN KEY(place_id) REFERENCES places(id),
    FOREIGN KEY(amenity_id) REFERENCES amenities(id)
);
