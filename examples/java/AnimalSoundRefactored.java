/**
 * Demonstrates Java 21 switch expression with pattern matching and null handling.
 */
public class AnimalSoundRefactored {
    /**
     * Retrieves the sound made by a given animal.
     *
     * @param animal The name of the animal.
     * @return The sound made by the animal, or "Unknown" if the animal is not recognized.
     */
    public static String getAnimalSound(String animal) {
        return switch (animal) {
            case null -> {
                System.out.println("Oops! A null animal?");
                yield "Unknown";
            }
            case String a when a.equalsIgnoreCase("Dog") -> "Bark";
            case String a when a.equalsIgnoreCase("Cat") -> "Meow";
            case String a when a.equalsIgnoreCase("Bird") -> "Tweet";
            default -> "Unknown";
        };
    }

    public static void main(String[] args) {
        System.out.println(getAnimalSound("Dog"));
        System.out.println(getAnimalSound("Cat"));
        System.out.println(getAnimalSound(null));
    }
}
