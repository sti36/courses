const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    let result;
    let str = input;

    // -- ваш код начинается тут

    result = str;

    // -- ваш код заканчивается тут

    console.log(result);
    rl.close();
});

/*У вас есть переменная str, которая содержит входные пользовательские данные.

Исправьте JavaScript код, так чтобы он записывал значение переменной str в переменную result. */