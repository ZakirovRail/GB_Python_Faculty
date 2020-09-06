'use strict';

/**
 * Функция сложения.
 * @param {number} number_1 первое число.
 * @param {number} number_2 второе число.
 * @returns {number}
 */
function sumTwoNumbers(number_1, number_2){
    return number_1 + number_2;
}

/**
 * Функция вычитания.
 * @param {number} number_1 первое число.
 * @param {number} number_2 второе число.
 * @returns {number}
 */
function subtractionTwoNumbers(number_1, number_2){
    return number_1 - number_2;
}

/**
 * Функция умножения.
 * @param {number} number_1 первое число.
 * @param {number} number_2 второе число.
 * @returns {number}
 */
function multiplicationTwoNumbers(number_1, number_2){
    return number_1 * number_2;
}

/**
 * Функция деления.
 * @param {number} number_1 первое число.
 * @param {number} number_2 второе число.
 * @returns {number}
 */
function divisionTwoNumbers(number_1, number_2){
    return number_1 / number_2;
}



/**
 * Функция возвращения результата операции с двумя числами в зависимости от выбранного операции(+, -, *, /).
 * @param {number} arg1 первое число.
 * @param {number} arg2 второе число.
 * @param {Object} operation второе число.
 * @returns {number}
 */
    let arg1 = prompt('Enter value for a first variable: ');
    let arg2 = prompt('Enter value for a second variable: ');
    let operation = prompt('Enter type of operation (+, -, * or /): ');

function mathOperation(arg1, arg2, operation){
    switch(operation) {
        case "+":
            console.log("sum of two numbers is: " + (arg1 + arg2));
            alert(arg1 + arg2);
            return sumTwoNumbers(arg1, arg2);
        case "-":
            console.log("subtraction of two numbers is: " + (arg1 - arg2));
            alert(arg1 - arg2);
            return subtractionTwoNumbers(arg1, arg2);
        case "*":
            console.log("multiplication of two numbers is: " + (arg1 * arg2));
            alert(arg1 * arg2);
            return multiplicationTwoNumbers(arg1, arg2);
        case "/":
            console.log("division of two numbers is: " + (arg1 / arg2));
            alert(arg1 / arg2);
            return divisionTwoNumbers(arg1, arg2);
        default:
            console.log("something is wrong");
    }
}