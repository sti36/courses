CREATE TABLE book(
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(50),
    author	VARCHAR(30),
    price DECIMAL(8, 2),
    amount INT
); -- Создание таблицы

INSERT INTO book (title, author, price, amount)
VALUES ('Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3); -- Создание записи в таблицу

INSERT INTO book (title, author, price, amount)
VALUES ('Белая гвардия', 'Булгаков М.А.', 540.50, 5), ('Идиот', 'Достоевский Ф.М.', 460.00, 10), ('Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 2); -- Добавление нескольких записей в таблицу
