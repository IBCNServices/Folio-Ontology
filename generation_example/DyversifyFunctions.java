import java.util.ArrayList;
import java.util.List;

public class DyversifyFunctions {

    public static String renson = "http://IBCNServices.github.io/Folio-Ontology/renson#";
    public static String m3lite = "http://purl.org/iot/vocab/m3-lite#";

    public static String generateIRI(String str, String prefix) {
        if (str == null || prefix == null) {
            return null;
        } else {
            String[] words = str.split(" ");

            for (int i = 0; i < words.length; i ++) {
                String word = words[i];

                word = word.substring(0, 1).toUpperCase() + word.substring(1);
                word = word.replaceAll("[^a-zA-Z0-9]", "");

                words[i] = word;
            }

            StringBuilder strBuilder = new StringBuilder();
            for (int i = 0; i < words.length; i++) {
                strBuilder.append(words[i]);
            }

            String newString = strBuilder.toString();

            return prefix + newString;
        }
    }
}
