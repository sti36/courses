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

SELECT * FROM book -- выборка всех данных из таблицы book

SELECT author, title, price
FROM book -- выборка отдельных столбцов (author, title, price)

SELECT 
title AS Название, 
author AS Автор
FROM book -- присвоил новые имена для столбцов при формировании выборки

SELECT title, amount,
    amount * 1.65 AS pack
FROM book -- произвёл выборку с вычисляемым столбцом

SELECT title, author, amount,
    ROUND(price - (price/100 * 30), 2) AS new_price
FROM book; -- произвёл выборку с вычисляемым столбцом


SELECT title, amount, price,
    ROUND(IF(amount < 4, price * 0.5, IF(amount < 11, price * 0.7, price * 0.9)), 2) AS sale,
    IF(amount < 4, 'скидка 50%', IF(amount < 11, 'скидка 30%', 'скидка 10%')) AS Ваша_скидка
FROM book;

SELECT author, title,
    ROUND(IF(author = 'Булгаков М.А.', price * 1.1, IF(author = 'Есенин С.А.', price * 1.05, price)), 2) AS new_price
FROM book; -- произвёл выборку с вычисляемым столбцом и логической функцией