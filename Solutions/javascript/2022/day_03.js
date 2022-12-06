const { getPuzzleInput } = require("../SetupSolutions/SetupSolutions.js");

const year = "2022";
const day = "03";
const puzzleInput = getPuzzleInput(year, `Day_${day}.txt`).filter(el => el);
const puzzle = puzzleInput;

const getCommonItems = (rucksackOne, rucksackTwo) => {
    let common = "";
    for (letter of rucksackOne) {
        if (rucksackTwo.includes(letter) && !common.includes(letter)) {
            common += letter;
        }
    }

    return common;
}

const getCommonItemsThree = (rucksackOne, rucksackTwo, rucksackThree) => {
    let common = "";
    for (letter of rucksackOne) {
        if (rucksackTwo.includes(letter) && rucksackThree.includes(letter) && !common.includes(letter)) {
            common += letter;
        }
    }

    return common;
}

const getItemTypePriority = (item) => {
    const value = item.charCodeAt(0);
    if (value >= "A".charCodeAt(0) && value <= "Z".charCodeAt(0)) {
        return value - 38;
    } else {
        return value - 96;
    }
}

const sumOfPrioritiesOfCommonItems = (puzzle) => {
    let totalCommonItems = [];
    for (line of puzzle) {
        const middlePoint = line.length / 2;
        const sackOne = line.slice(0, middlePoint);
        const sackTwo = line.slice(middlePoint);
        const commonItems = getCommonItems(sackOne, sackTwo);

        totalCommonItems.push(commonItems);
    }

    return totalCommonItems.reduce((prev, curr) => prev + getItemTypePriority(curr), 0);
}

const sumOfPrioritiesOfCommonItemsThreeElves = (puzzle) => {
    let totalCommonItems = [];
    for (let i = 0; i < puzzle.length; i+=3) {
        const commonItems = getCommonItemsThree(puzzle[i], puzzle[i+1], puzzle[i+2]);

        totalCommonItems.push(commonItems);
    }

    return totalCommonItems.reduce((prev, curr) => prev + getItemTypePriority(curr), 0);
}

// Script runs here
console.log(`Advent of Code - ${year}: Day ${day}`);
console.log("Part-One Answer:", sumOfPrioritiesOfCommonItems(puzzle));
console.log("Part-Two Answer:", sumOfPrioritiesOfCommonItemsThreeElves(puzzle));