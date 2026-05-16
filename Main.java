import java.io.*;
import java.util.*;

public class Main {
    // ANSI colors
    static final String RESET = "\u001B[0m";
    static final String RED = "\u001B[31m";
    static final String GREEN = "\u001B[32m";
    static final String YELLOW = "\u001B[33m";
    static final String BLUE = "\u001B[34m";
    static final String MAGENTA = "\u001B[35m";

    static class Model {
        String name, diverse, oversight, explain, highRisk, bias, desc, domain;
        double score;
        String rating;

        Model(String[] p) {
            name = p[0];
            diverse = p[1];
            oversight = p[2];
            explain = p[3];
            highRisk = p[4];
            bias = p[5];
            desc = p[7];
            domain = p[8];
            computeScore();
        }

        void computeScore() {
            double risk = 0;
            if (diverse.equals("no")) risk += 2;
            if (oversight.equals("no")) risk += 2;
            if (explain.equals("no")) risk += 1;
            if (highRisk.equals("yes")) risk += 3;
            if (bias.equals("medium")) risk += 1;
            if (bias.equals("high")) risk += 2;

            double mult = switch (domain) {
                case "neurology", "oncology", "emergency", "critical_care" -> 1.3;
                case "cardiology", "neonatology" -> 1.2;
                case "pediatrics", "infection_control" -> 1.1;
                default -> 1.0;
            };
            score = risk * mult;

            if (score <= 3) rating = "SAFE";
            else if (score <= 6) rating = "NEEDS REVIEW";
            else rating = "HIGH RISK";
        }

        String colorRating() {
            return switch (rating) {
                case "SAFE" -> GREEN + rating + RESET;
                case "NEEDS REVIEW" -> YELLOW + rating + RESET;
                default -> RED + rating + RESET;
            };
        }

        String recommendations() {
            StringBuilder r = new StringBuilder();
            if (diverse.equals("no")) r.append("- Improve demographic diversity.\n");
            if (oversight.equals("no")) r.append("- Add human-in-the-loop oversight.\n");
            if (explain.equals("no")) r.append("- Implement explainability tools.\n");
            if (highRisk.equals("yes")) r.append("- Increase monitoring and audits.\n");
            if (bias.equals("high")) r.append("- Conduct fairness and bias mitigation.\n");
            if (r.length() == 0) r.append("- Maintain current governance controls.\n");
            return r.toString();
        }

        void printModelCard() {
            System.out.println(BLUE + "====================================" + RESET);
            System.out.println(BLUE + "MODEL CARD" + RESET);
            System.out.println("Name: " + name);
            System.out.println("Domain: " + domain);
            System.out.println("Description: " + desc);
            System.out.println("Governance Score: " + score);
            System.out.println("Safety Rating: " + colorRating());
            System.out.println("Recommendations:\n" + recommendations());
            System.out.println("JSON-style card:");
            System.out.println("{");
            System.out.println("  \"name\": \"" + name + "\",");
            System.out.println("  \"domain\": \"" + domain + "\",");
            System.out.println("  \"description\": \"" + desc + "\",");
            System.out.println("  \"score\": " + score + ",");
            System.out.println("  \"rating\": \"" + rating + "\"");
            System.out.println("}");
        }
    }

    public static void main(String[] args) throws Exception {
        List<Model> models = loadModels("models.csv");
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println(MAGENTA + "\n=== Healthcare AI Governance Console ===" + RESET);
            System.out.println("1. View all model cards");
            System.out.println("2. Search by model name");
            System.out.println("3. Filter by domain");
            System.out.println("4. View summary analytics");
            System.out.println("5. View top 10 highest-risk models");
            System.out.println("6. View ASCII bias heatmap");
            System.out.println("7. View ASCII risk trend graph");
            System.out.println("8. Exit");
            System.out.print("Choose an option: ");

            String choice = sc.nextLine().trim();
            switch (choice) {
                case "1" -> showAll(models);
                case "2" -> searchByName(models, sc);
                case "3" -> filterByDomain(models, sc);
                case "4" -> summaryAnalytics(models);
                case "5" -> top10(models);
                case "6" -> biasHeatmap();
                case "7" -> riskTrend(models);
                case "8" -> { System.out.println("Goodbye."); return; }
                default -> System.out.println("Invalid choice.");
            }
        }
    }

    static List<Model> loadModels(String path) throws Exception {
        List<Model> list = new ArrayList<>();
        BufferedReader br = new BufferedReader(new FileReader(path));
        String line = br.readLine(); // header
        while ((line = br.readLine()) != null) {
            String[] p = line.split(",");
            list.add(new Model(p));
        }
        return list;
    }

    static void showAll(List<Model> models) {
        for (Model m : models) m.printModelCard();
    }

    static void searchByName(List<Model> models, Scanner sc) {
        System.out.print("Enter model name (or part of it): ");
        String q = sc.nextLine().toLowerCase();
        boolean found = false;
        for (Model m : models) {
            if (m.name.toLowerCase().contains(q)) {
                m.printModelCard();
                found = true;
            }
        }
        if (!found) System.out.println("No models found.");
    }

    static void filterByDomain(List<Model> models, Scanner sc) {
        System.out.print("Enter domain (e.g., oncology, neurology): ");
        String d = sc.nextLine().toLowerCase();
        boolean found = false;
        for (Model m : models) {
            if (m.domain.toLowerCase().equals(d)) {
                m.printModelCard();
                found = true;
            }
        }
        if (!found) System.out.println("No models in that domain.");
    }

    static void summaryAnalytics(List<Model> models) {
        System.out.println(MAGENTA + "\n=== Summary Analytics ===" + RESET);
        double sum = 0;
        Map<String, Integer> domainCount = new HashMap<>();
        Map<String, Double> domainTotal = new HashMap<>();
        for (Model m : models) {
            sum += m.score;
            domainCount.put(m.domain, domainCount.getOrDefault(m.domain, 0) + 1);
            domainTotal.put(m.domain, domainTotal.getOrDefault(m.domain, 0.0) + m.score);
        }
        double avg = sum / models.size();
        System.out.println("Governance Maturity Score (avg risk): " + avg);

        System.out.println("\nDomain Risk Distribution:");
        for (String d : domainCount.keySet()) {
            double a = domainTotal.get(d) / domainCount.get(d);
            System.out.println(" - " + d + ": " + a);
        }

        System.out.println("\nPolicy Compliance Checklist (high-level):");
        System.out.println("- Data diversity considered: YES");
        System.out.println("- Human oversight considered: YES");
        System.out.println("- Explainability considered: YES");
        System.out.println("- High-risk tasks flagged: YES");
        System.out.println("- Bias indicators tracked: YES");
    }

    static void top10(List<Model> models) {
        System.out.println(RED + "\n=== Top 10 Highest-Risk Models ===" + RESET);
        List<Model> copy = new ArrayList<>(models);
        copy.sort((a, b) -> Double.compare(b.score, a.score));
        for (int i = 0; i < Math.min(10, copy.size()); i++) {
            Model m = copy.get(i);
            System.out.println((i + 1) + ". " + m.name + " — " + m.score + " (" + m.domain + ") " + m.colorRating());
        }
    }

    static void biasHeatmap() {
        System.out.println(BLUE + "\n=== Bias Heatmap (ASCII) ===" + RESET);
        System.out.println("Low Bias:    ###");
        System.out.println("Medium Bias: #######");
        System.out.println("High Bias:   ##########");
        System.out.println("(Conceptual visualization, not per-model counts.)");
    }

    static void riskTrend(List<Model> models) {
        System.out.println(BLUE + "\n=== Risk Trend (ASCII) ===" + RESET);
        List<Double> scores = new ArrayList<>();
        for (Model m : models) scores.add(m.score);
        Collections.sort(scores);
        int idx = 1;
        for (double s : scores) {
            int bars = (int)Math.round(s);
            StringBuilder b = new StringBuilder();
            for (int i = 0; i < bars; i++) b.append("#");
            System.out.println(idx++ + ": " + b + " (" + s + ")");
        }
    }
}