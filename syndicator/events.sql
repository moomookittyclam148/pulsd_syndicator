DROP TABLE IF EXISTS event;

CREATE TABLE event (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    event_name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    country TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    event_img TEXT,
    event_desc TEXT,
    event_type TEXT,
    ticket_type TEXT,
    date_created TEXT
);
