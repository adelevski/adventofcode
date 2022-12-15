import scala.io.Source


var part_one_char_map = Map('A' -> 'X', 'B' -> 'Y', 'C' -> 'Z')
var part_one_base_map = Map('X' -> 1, 'Y' -> 2, 'Z' -> 3)
var part_two_outcome_map = Map('X' ->  0, 'Y' -> 3, 'Z' -> 6)
var part_two_win_base_map = Map('A' -> 2, 'B' -> 3, 'C' -> 1)
var part_two_lose_base_map = Map('A' -> 3, 'B' -> 1, 'C' -> 2)
var part_two_draw_base_map = Map('A' -> 1, 'B' -> 2, 'C' -> 3)

def scoreOne(x: String): Int = {
    // Init
    var score: Int = 0

    // Draw
    if (part_one_char_map.get(x(0)).get == x(2)) score += 3

    // Win
    if (x(0) == 'A' && x(2) == 'Y') score += 6 // Rock
    if (x(0) == 'B' && x(2) == 'Z') score += 6 // Paper
    if (x(0) == 'C' && x(2) == 'X') score += 6 // Scissors

    // Base
    score += part_one_base_map.get(x(2)).get

    // Return
    score
}

def scoreTwo(x: String): Int = {
    // Init
    var score: Int = 0

    // Win, Lose, Draw
    score += part_two_outcome_map.get(x(2)).get

    // Base
    if (x(2) == 'Z') score += part_two_win_base_map.get(x(0)).get
    if (x(2) == 'X') score += part_two_lose_base_map.get(x(0)).get
    if (x(2) == 'Y') score += part_two_draw_base_map.get(x(0)).get

    // Return 
    score
}

@main def day2() = {
    val lines: List[String] = Source.fromFile("day2.txt").getLines.toList
    println("Part 1: " + lines.map(scoreOne).sum)
    println("Part 2: " + lines.map(scoreTwo).sum)
}
