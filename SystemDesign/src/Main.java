import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {

        //main card
        PlayingCard ace = new PlayingCard("ACE","hearts");

        // similar cards
        PlayingCard two = new PlayingCard(2,"diamonds");
        PlayingCard three = new PlayingCard(3,"clubs");
        PlayingCard ten = new PlayingCard(10,"spades");
        PlayingCard eight = new PlayingCard(8,"hearts");
        PlayingCard nine = new PlayingCard(9,"diamonds");
        PlayingCard queen = new PlayingCard("QUEEN","clubs");


        List<PlayingCard> list = new ArrayList<>();
        list.add(three);
        list.add(nine);
        list.add(two);
        list.add(eight);
        list.add(ten);
        list.add(queen);

        ace.SortedSimilarCards(list);

        for(PlayingCard p: list){
            System.out.println(p.toString());
        }
    }
}
