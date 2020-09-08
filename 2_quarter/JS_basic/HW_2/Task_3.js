'use strict';

let a = prompt('Enter value for variable a: ');
let b = prompt('Enter value for variable b: ');


if (a >= 0 && b >= 0)
{
    alert("Сумма чисел равна: " + (a - b))
}
else if (a < 0 && b < 0)
{
    alert("Произведение чисел равно: " + (a * b))
}
else if ((a > 0 && b < 0) || (a < 0 && b > 0))
{
    alert("Произведение чисел равно: " + (+a + +b))
}
