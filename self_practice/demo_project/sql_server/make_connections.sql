USE demo_project;
GO


/* Users with Card */
ALTER TABLE users
ALTER COLUMN id BIGINT NOT NULL;

ALTER TABLE users
ADD CONSTRAINT PK_Users PRIMARY KEY (id);

ALTER TABLE cards
ADD CONSTRAINT FK_Cards_Users
FOREIGN KEY (user_id)
REFERENCES users(id);


/* Card with Scheduled_Payments */
ALTER TABLE cards
ALTER COLUMN id BIGINT NOT NULL;

ALTER TABLE cards
ADD CONSTRAINT PK_Cards PRIMARY KEY (id);

ALTER TABLE scheduled_payments
ADD CONSTRAINT FK_Scheduled_Payments__Cards
FOREIGN KEY (card_id)
REFERENCES cards(id);


/* User with Scheduled_Payments */
ALTER TABLE scheduled_payments
ADD CONSTRAINT FK_Scheduled_Payments__Users
FOREIGN KEY (user_id)
REFERENCES users(id);


/* Cards with Transactions(from card) */
ALTER TABLE transactions
ADD CONSTRAINT FK_Transactions_From_Cards
FOREIGN KEY (from_card_id)
REFERENCES cards(id);


/* Cards with Transactions(to card) */
ALTER TABLE transactions
ADD CONSTRAINT FK_Transactions_To_Cards
FOREIGN KEY (to_card_id)
REFERENCES cards(id);


/* Transactions with Logs */
ALTER TABLE transactions
ALTER COLUMN id BIGINT NOT NULL;

ALTER TABLE transactions
ADD CONSTRAINT PK_Transactions PRIMARY KEY (id);

ALTER TABLE logs
ADD CONSTRAINT FK_Logs_Transactions
FOREIGN KEY (transaction_id)
REFERENCES transactions(id);