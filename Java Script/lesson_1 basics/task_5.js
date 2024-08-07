const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    let result;
    let number = Number(input);

    // -- ваш код начинается тут

    result = String(number)

    // -- ваш код заканчивается тут

    console.log(result + ' is ' + typeof result);
    rl.close();
});

/*У вас есть переменная number, которая содержит входные пользовательские данные.

Напишите JavaScript код, который преобразует числовое значение переменной number в строковое и записывает результат в переменную result. */