const { getPuzzleInput } = require("../SetupSolutions/SetupSolutions.js");

const year = "2022";
const day = "02";
const puzzleInput = getPuzzleInput(year, `Day_${day}.txt`);
const puzzle = puzzleInput.filter(el => el);

const POINTS = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
};

const SHAPES_MAP_1 = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
};

const SHAPES_MAP_2 = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
};

const PLAYS_STRAT_ONE = {
    "Rock": {
        "Rock": 3,
        "Paper": 6,
        "Scissors": 0
    },
    "Paper": {
        "Rock": 0,
        "Paper": 3,
        "Scissors": 6
    },
    "Scissors": {
        "Rock": 6,
        "Paper": 0,
        "Scissors": 3
    },
};

const PLAYS_STRAT_TWO = {
    "Rock": {
        "Lose": "Scissors",
        "Draw": "Rock",
        "Win": "Paper"
    },
    "Paper": {
        "Lose": "Rock",
        "Draw": "Paper",
        "Win": "Scissors"
    },
    "Scissors": {
        "Lose": "Paper",
        "Draw": "Scissors",
        "Win": "Rock"
    },
}

const getScoreForStrategyOne = (puzzle) => {
    return puzzle.map(el => {
        const [one, two] = el.split(" ");
        
        const player_one = SHAPES_MAP_1[one];
        const player_two = SHAPES_MAP_1[two];

        return POINTS[player_two] + PLAYS_STRAT_ONE[player_one][player_two];
    }). reduce((prev, curr) => prev + curr, 0);
};

const getScoreForStrategyTwo = (puzzle) => {
    return puzzle.map(el => {
        const [one, two] = el.split(" ");
        
        const player_one = SHAPES_MAP_1[one];
        const player_two = PLAYS_STRAT_TWO[player_one][SHAPES_MAP_2[two]];

        return POINTS[player_two] + PLAYS_STRAT_ONE[player_one][player_two];
    }). reduce((prev, curr) => prev + curr, 0);
};

// Script runs here
console.log(`Advent of Code - ${year}: Day ${day}`);
console.log("Part-One Answer:", getScoreForStrategyOne(puzzle));
console.log("Part-Two Answer:", getScoreForStrategyTwo(puzzle));