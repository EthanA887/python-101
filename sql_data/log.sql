CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL,
    level INTEGER NOT NULL DEFAULT 1
);

/* Created by Ethan Ali */