public class AnimalSoundOriginal {
    public static String getSound(String animal) {
        if (animal == null) {
            System.out.println("Oops! A null animal?");
        } else if (animal.equalsIgnoreCase("Dog")) {
            return "Bark";
        } else if ( animal.equalsIgnoreCase("Cat")) {
            return "Meow";
        } else if ( animal.equalsIgnoreCase("Bird")) {
            return "Tweet";
        }
        return "Unknown";
    }

    public static void main(String[] args) {
        System.out.println(getSound("Dog"));
        System.out.println(getSound("Cat"));
        System.out.println(getSound(null));
    }
}
