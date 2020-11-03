import sqlite3
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
#cursor.execute('''CREATE TABLE "Players1" (
#	"Name"	TEXT NOT NULL UNIQUE,
#	"Country"	TEXT NOT NULL,
#	"Matches_Played"	INTEGER DEFAULT 0,
#	"INNINGS"	INTEGER DEFAULT 0,
#	"Runs"	INTEGER DEFAULT 0,
#	"Balls_Faced"	INTEGER DEFAULT 0,
#	"Fours"	INTEGER,
#	"Sixes"	INTEGER,
#	"High_Score"	INTEGER DEFAULT 0,
#	"Balls_Bowled"	INTEGER DEFAULT 0,
#	"Wickets"	INTEGER DEFAULT 0,
#	"Runs_Given"	INTEGER DEFAULT 0,
#	"Catches"	INTEGER DEFAULT 0,
#	"Player_ID"	INTEGER NOT NULL UNIQUE,
#	PRIMARY KEY("Player_ID"),
#	FOREIGN KEY("Country") REFERENCES "Teams1"("Name")
#);''')
#sqliteConnection.commit()
sqliteConnection = sqlite3.connect('example.db')
cursor = sqliteConnection.cursor()
cursor.execute('''INSERT INTO Players1 SELECT * FROM Players;''')
sqliteConnection.commit()


