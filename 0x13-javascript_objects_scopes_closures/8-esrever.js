#!/usr/bin/node

exports.esrever = function (list) {
    const arr = [];
    const lenList = list.length;

    for (let i = lenList - 1; i >= 0; i--) {
        arr.push(list[i]);
    }
    return (arr);
}
