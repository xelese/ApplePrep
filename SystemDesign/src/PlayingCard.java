import java.util.*;

public class PlayingCard implements Comparable<PlayingCard> {

    private String Suite = null;
    private String faceCard = null;
    private int cardValue = -1;

    // Constructor 1 for face card
    public PlayingCard(String faceCard, String suite) throws Exception {

        if (!checkSuit(suite)) throw new Exception("Invalid suite");

        if (null == faceCard) {
            throw new Exception("Invalid input cannot be null");
        }

        faceCard = faceCard.trim().toLowerCase();

        // Check if card type is empty
        if (faceCard.equals("")) {
            throw new Exception("Card type cannot be empty");
        }

        // Check the type of face card.
        if (faceCard.equals("ace")) {
            this.cardValue = 1;
        } else if (faceCard.equals("jack")) {
            this.cardValue = 11;
        } else if (faceCard.equals("queen")) {
            this.cardValue = 12;
        } else if (faceCard.equals("king")) {
            this.cardValue = 13;
        }

        // otherwise throw exception
        else {
            throw new Exception("Invalid card type");
        }

        // after sanity checks add it to the type of card
        this.faceCard = faceCard;

    }

    // constructor 2 for just numbered card
    public PlayingCard(int cardValue, String suite) throws Exception {

        if (!checkSuit(suite)) throw new Exception("Invalid suite");

        // Check if the value is invalid
        if (cardValue <= 1 || cardValue > 13) {
            throw new Exception("Invalid card value");
        }

        // otherwise set the cardValue
        this.cardValue = cardValue;
    }

    private boolean checkSuit(String suite) throws Exception {
        if (null == suite) return false;

        suite = suite.trim().toLowerCase();

        if (suite.equals("")) return false;

        switch (suite) {
            case "diamonds":
            case "clubs":
            case "spades":
            case "hearts":
                this.Suite = suite;
                return true;
            default:
                return false;
        }
    }

    @Override
    public String toString() {
        return "Face: " + this.faceCard + "\n" +"Suite: " + this.Suite + "\n" + "Value: " + cardValue;
    }

    @Override
    public int compareTo(PlayingCard p1) {
        return this.cardValue - p1.cardValue;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof PlayingCard)) return false;
        PlayingCard that = (PlayingCard) o;
        return cardValue == that.cardValue && faceCard.equals(that.faceCard) && this.Suite.equals(that.Suite);
    }

    @Override
    public int hashCode() {
        return Objects.hash(faceCard, cardValue, Suite);
    }

    public void SortedSimilarCards(List<PlayingCard> playingCards) {
        Collections.sort(playingCards);

        Map<PlayingCard, Integer> map = new HashMap<>();

        for (PlayingCard p : playingCards) {
            map.put(p, p.cardValue);
        }

        Set<PlayingCard> set = map.keySet();
        for (PlayingCard p : set) {
            Integer i = map.getOrDefault(p, -1);
            if (i < 0) {
                return;
            } else {
                System.out.println(i);
            }
        }
    }
}

