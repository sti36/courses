const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input) => {
    // -- ваш код начинается тут

    //const result = 0;
    let [x, y] = input.split(" ").map(Number);

    result = x + y;

    // -- ваш код заканчивается тут

    console.log(result);
    rl.close();
});

/*У вас есть переменные x, y, которые содержат входные пользовательские данные.

Исправьте JavaScript код, так чтобы он складывал два числа x и y и записывал результат в переменную result. */