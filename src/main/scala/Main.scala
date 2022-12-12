import scala.io.Source

@main def main() = {
    val elvesString: Array[String] = Source.fromFile("data.txt").mkString.split("\n\n")
    

}