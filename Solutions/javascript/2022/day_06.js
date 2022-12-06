const { getPuzzleInput } = require("../SetupSolutions/SetupSolutions.js");

const year = "2022";
const day = "06";
const puzzleInput = getPuzzleInput(year, `Day_${day}.txt`);
const puzzle = puzzleInput[0];

const allDifferentChars = (s) => {
    const existingChars = {};
    for (c of s.split("")) {
        if (c in existingChars) return false;
        else existingChars[c] = c;
    }
    
    return true;
}

const getStartOfMarker = (puzzle, interval) => {
    for (let i = 0; i <= puzzle.length; i++) {
        let latest = i + interval;
        let snip = puzzle.slice(i, latest)
        if (allDifferentChars(snip)) return latest;
    }
}

// Script runs here
console.log(`Advent of Code - ${year}: Day ${day}`);
console.log("Part-One Answer:", getStartOfMarker(puzzle, 4));
console.log("Part-Two Answer:", getStartOfMarker(puzzle, 14));