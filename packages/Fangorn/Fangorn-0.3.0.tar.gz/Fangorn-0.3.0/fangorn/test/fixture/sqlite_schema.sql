CREATE TABLE big ( 
    node_id   INTEGER PRIMARY KEY AUTOINCREMENT
                      NOT NULL,
    parent_id INTEGER DEFAULT 'NULL'
                      REFERENCES big ( node_id ) ON DELETE CASCADE
                                                   ON UPDATE CASCADE,
    l         INTEGER NOT NULL,
    r         INTEGER NOT NULL,
    value     INTEGER
);
CREATE TABLE [small] ([node_id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, [parent_id] INTEGER DEFAULT 'NULL' REFERENCES [small] ([node_id]) ON UPDATE CASCADE ON DELETE CASCADE, [l] INTEGER NOT NULL, [r] INTEGER NOT NULL, [name] TEXT);
CREATE INDEX big_l ON `big`(`l`);
CREATE INDEX big_parent_id ON `big`(`parent_id`);
CREATE INDEX big_r ON `big`(`r`);
CREATE INDEX small_l ON [small] ( l );
CREATE INDEX small_parent_id ON [small] ( parent_id );
CREATE INDEX small_r ON [small] ( r );
