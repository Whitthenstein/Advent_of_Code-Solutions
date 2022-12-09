const { getPuzzleInput } = require("../SetupSolutions/SetupSolutions.js");

const year = "2022";
const day = "01";
const puzzleInput = getPuzzleInput(year, `Day_${day}.txt`);
const puzzle = puzzleInput;

const getMostCaloriesElf = (puzzle) => {
    let mostCalories = 0;
    let count = 0;
    for (calories of puzzle) {
        if (calories === "") {
            if (count >= mostCalories) mostCalories = count;
            count = 0;
        }
        else {
            count += parseInt(calories);
        }
    }

    return mostCalories;
};

const getTopThreeElves = (puzzle) => {
    let elves = [];
    let count = 0;
    for (calories of puzzle) {
        if (calories === "") {
            elves.push(count);
            count = 0;
        }
        else {
            count += parseInt(calories);
        }
    }

    return elves.sort((a,b) => b - a)
                .slice(0, 3)
                .reduce((prev, curr) => prev + curr, 0)
};

// Script runs here
console.log(`Advent of Code - ${year}: Day ${day}`);
console.log("Part-One Answer:", getMostCaloriesElf(puzzle));
console.log("Part-Two Answer:", getTopThreeElves(puzzle));