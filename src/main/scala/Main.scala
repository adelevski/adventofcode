import scala.io.Source

@main def main() = {
    val elvesString: Array[String] = Source.fromFile("data.txt").mkString.split("\n\n")

    val elves: Array[Array[Int]] = elves.map { x => x.split("\n").map(_.toInt) }

    println(elves(0)(0))

    // println(lines)
}