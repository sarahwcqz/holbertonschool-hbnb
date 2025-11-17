-- Insert Admin user
INSERT INTO
    users (
        id,
        email,
        first_name,
        last_name,
        password,
        is_admin
    )
VALUES
    (
        "36c9050e-ddd3-4c3b-9731-9f487208bbc1",
        "admin@hbnb.io",
        "Admin",
        "HBnB",
        "$2b$12$rd6eohZP9Q7Pc0/PppgyI.gGcNFl7fMrt.lmC0DawC38O1QpImL6S",
        TRUE
    );

-- Insert 3 amenities
INSERT INTO
    amenities (id, name)
VALUES
    ("298cd0f9-9713-479f-b14b-ac4f5a9d97fe", "WiFi");